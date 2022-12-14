import sys
import socket

ip_addr = '127.0.0.1'
port_list = [ ] # write ports to scan

for port in port_list:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"port: {port} - OPEN")
        else:
            print(f"port: {port} - CLOSED")
        sock.close()

    except socket.error as err:
        print(f"connection error: {err}")
        sys.exit()