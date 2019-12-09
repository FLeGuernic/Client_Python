
from scapy.layers.inet import *
import requests as req
import json;
from requests import get, post


def main():

    resp = req.get("https://aqueous-dusk-24314.herokuapp.com/ip/all", timeout=20)

    li = []
    res = resp.text
    loaded_json = json.loads(res)
    for x in loaded_json :
       li.append(x['address'])

    traceroutes = []

    ip = get('https://api.ipify.org').text
    print(ip)
    for address in li:
        chemin= []
        print("dst: " + address)
        for i in range(1, 20):
                pkt = IP(dst=address, ttl=i) / UDP(dport=33434)
                # Send the packet and get a reply
                reply = sr1(pkt, verbose=0, timeout=10)
                if reply is None:
                    # No reply =(
                    print("no reply")
                    # break
                elif reply.type == 3:
                    # We've reached our destination
                    print("Done!", reply.src)
                    break
                else:
                    # We're in the middle somewhere
                    print("%d hops away: " % i, reply.src)
                    chemin.append(reply.src)
        print(chemin)

        traceroutes.append({'src': ip, "dst": address, "route": chemin})
    post(url="https://aqueous-dusk-24314.herokuapp.com/traceroute/", data={"traceroutes": traceroutes})



if __name__ == '__main__':
    main()

