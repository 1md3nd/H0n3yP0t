#!/usr/local/bin/python3
import os
from scapy import all
from scapy.all import *
def packetcraft():
    print("Begining packet crafting:")
    while True:
        os.system("iptables-legacy -A OUTPUT -p tcp -o eth0 --sport 1:65535 --tcp-flags RST RST -j DROP")
        def packet(pkt):
            if pkt[TCP].flags == 2:
                if(str(pkt[TCP].dport)) == 22:
                    print("SYN packet detected port : " + str(pkt[TCP].sport) + " from IP Src : " + pkt[IP].src)
                    send(IP(dst=pkt[IP].src, src=pkt[IP].dst)/TCP(dport=pkt[TCP].sport, sport=pkt[TCP].dport,ack=pkt[TCP].seq + 1, flags='SA'))
                elif(str(pkt[TCP].dport)) == "445":
                    print("SYN packet detected port : " + str(pkt[TCP].sport) + " from IP Src : " + pkt[IP].src)
                    send(IP(dst=pkt[IP].src, src=pkt[IP].dst)/TCP(dport=pkt[TCP].sport, sport=pkt[TCP].dport,ack=pkt[TCP].seq + 1, flags='SA'))
        sniff(iface="eth0", prn=packet, filter="tcp[0xd]&18=2",count=10)
        os.system("iptables-legacy -D OUTPUT -p tcp -o eth0 --sport 1:65535 --tcp-flags RST RST -j DROP")
        
def logports():
    print("Starting T-Shark capture on ports 22 and 445:")
    os.system("sudo tshark -i eth0 -c 10 -f \"port 22 or port 445\" -w /home/capture/mycapt.pcap -F libpcap")
    print("T-Shark is now running")
    
def main():
    print("Starting HoneyPot Script")
    logports()
    packetcraft()
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Exiting as user request...')