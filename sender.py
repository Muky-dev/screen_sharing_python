from vidstream import ScreenShareClient
import threading
import socket

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

sender = ScreenShareClient(get_ip_address(), 9999)

t = threading.Thread(target=sender.start_stream)
t.start()

while input("") != "STOP":
    continue

sender.stop_server()