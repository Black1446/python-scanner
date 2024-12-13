import socket
from datetime import datetime

# ASCII Art Header
def ascii_banner():
    print("""
    ██████╗ ██████╗ ███████╗██████╗ 
    ██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██████╔╝██████╔╝█████╗  ██████╔╝
    ██╔═══╝ ██╔═══╝ ██╔══╝  ██╔═══╝ 
    ██║     ██║     ███████╗██║     
    ╚═╝     ╚═╝     ╚══════╝╚═╝     
      Simple Port Scanner      
    """)

# Main scanning function
def scan(target, ports):
    print(f"\n[+] Scanning Target: {target}")
    print("[+] Scan started at:", datetime.now())
    
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            sock.close()
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user.")
            break
        except Exception as e:
            print(f"[!] Error scanning port {port}: {e}")
            break

# User input
if __name__ == "__main__":
    ascii_banner()
    target = input("[*] Enter Target IP Address: ")
    port_range = input("[*] Enter Port Range (e.g., 20-100): ")

    try:
        start_port, end_port = map(int, port_range.split('-'))
        ports = range(start_port, end_port + 1)
        scan(target, ports)
    except ValueError:
        print("[!] Invalid port range. Use format: start-end (e.g., 20-100).")
