import socket

# Create a TCP socket (same as server)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(("127.0.0.1", 9999))

# Receive data from the server
data = client.recv(1024)
print(f"Received: {data.decode()}")

# Send a response
client.send(b"Hello from client!")

# Clean up
client.close()