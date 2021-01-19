from vidstream import StreamingServer
import threading

ip = input("Insert sender ip: ")

receiver = StreamingServer(ip, 9999)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != "STOP":
    continue

receiver.stop_server()