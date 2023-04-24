import socket

def scan_ports(ip_address, start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip_address, port))
            s.close()
            print("Port {} is open".format(port))
        except socket.error:
            pass

if __name__ == "__main__":
    ip_address = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    scan_ports(ip_address, start_port, end_port)
