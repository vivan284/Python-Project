import socket
import datetime

target = input("Target IP: ")

def port_scan(target):
    try:
        ip = socket.gethostbyname(target)

        print(f"Scanning {target}...")
        print("Time started: ", datetime.datetime.now())

        for port in range(20,90):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port ))
            if result == 0:
                print("Port {} is open".format(port))
            sock.close()
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
    except socket.error:
        print("Couldn't connect to server")
port_scan(target)