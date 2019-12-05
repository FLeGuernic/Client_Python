
from scapy.layers.inet import *
import requests as req
import json;



resp = req.get("https://aqueous-dusk-24314.herokuapp.com/ip/all", timeout=20)

#Stock IP addresses in a list
li = []
res = resp.text ;
loaded_json = json.loads(res);
for  x in loaded_json :
   li.append(x['address']);

"""
traceroutes = []
for address in li:
    chemin= []
    chemin.append(address) ;
    for address_dst in li:
        if(address_dst != address):
            for i in range(1, 28):
                pkt = IP(dst=address, ttl=i) / UDP(dport=33434)
                # Send the packet and get a reply
                reply = sr1(pkt, verbose=0)
                if reply is None:
                    # No reply =(
                    break
                elif reply.type == 3:
                    # We've reached our destination
                    print("Done!", reply.src)
                    break
                else:
                    # We're in the middle somewhere
                    print("%d hops away: " % i, reply.src)
                    chemin.append(reply.src)


"""

hostname = "google.com"
chemin=[];
for i in range(1, 28):
    pkt = IP(dst=hostname, ttl=i) / UDP(dport=33434)
    # Send the packet and get a reply
    reply = sr1(pkt, verbose=0)
    if reply is None:
        # No reply =(
        break
    elif reply.type == 3:
        # We've reached our destination
        print("Done!", reply.src)
        break
    else:
        # We're in the middle somewhere
        print( "%d hops away: " % i , reply.src)
        chemin.append(reply.src)


print(chemin)

