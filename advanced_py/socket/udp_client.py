import socket

# UDP Client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"ping", ("127.0.0.1", 9999))
data, addr = client.recvfrom(1024)
print(data.decode())