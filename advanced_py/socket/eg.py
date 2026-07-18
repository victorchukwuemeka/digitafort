import socket
from ipaddress import IPv4Address, IPv6Address

# we need a server that has socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(("0.0.0.0", 1111))
serv.listen(5)
print("is listening to port 9999 .... ")


conn, addr = serv.accept()

conn.send(b"welcome to our stupid server ")

data = conn.recv(1024)

print(f"Received: {data.decode()}")

conn.close()
serv.close()
