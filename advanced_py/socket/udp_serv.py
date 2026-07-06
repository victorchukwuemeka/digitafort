import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("0.0.0.0", 9999))
data, addr = server.recvfrom(1024)  # receive from anyone
server.sendto(b"pong", addr)


