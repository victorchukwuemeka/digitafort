# a socket
import socket

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = socket.gethostname()
port = 1111
cli.connect((socket.gethostname(), port))

cli.recv(1024)
print("rrrrr")

cli.send(b"Hello from client!")

# Clean up
cli.close()
