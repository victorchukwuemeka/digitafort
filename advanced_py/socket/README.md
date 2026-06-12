# Socket Programming — Network Communication in Python

## 1. What is a Socket?
A socket is an endpoint for communication between two programs over a network. Every time you visit a website, your browser creates a socket to the server. Python's `socket` module lets you do this directly.

There are two types of sockets: **TCP** (reliable, ordered, connection-oriented — like a phone call) and **UDP** (fast, connectionless — like a letter). We'll focus on TCP first.

## 2. A Simple TCP Server
The server follows: `socket → bind → listen → accept → send/recv → close`

```python
import socket

# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to an address and port
server.bind(("0.0.0.0", 9999))

# Start listening for connections
server.listen(5)
print("Server listening on port 9999...")

# Wait for a client to connect (this blocks)
conn, addr = server.accept()
print(f"Connected by {addr}")

# Send a message to the client
conn.send(b"Welcome to the server!")

# Receive data from the client
data = conn.recv(1024)
print(f"Received: {data.decode()}")

# Clean up
conn.close()
server.close()
```

Run this in Terminal 1: `python server.py`

## 3. A Simple TCP Client
The client follows: `socket → connect → send/recv → close`

```python
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
```

Run this in Terminal 2: `python client.py`

You'll see the server print "Connected by ('127.0.0.1', XXXXX)" and the client print "Received: Welcome to the server!".

## 4. Handling Multiple Clients
Our server only handles one client. To handle many, we need a loop and threads:

```python
import socket
import threading

def handle_client(conn, addr):
    """Each client runs in its own thread."""
    print(f"New connection: {addr}")
    conn.send(b"Welcome!")

    while True:
        data = conn.recv(1024)
        if not data:  # client disconnected
            break
        conn.send(b"Message received")

    conn.close()
    print(f"Connection closed: {addr}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))
server.listen(5)
print("Server listening...")

while True:
    conn, addr = server.accept()
    # Start a new thread for each client
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
```

Now multiple clients can connect simultaneously. The server creates a new thread for each one.

## 5. UDP — Connectionless Communication
UDP skips the connection setup — just send data directly:

```python
# UDP Server
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("0.0.0.0", 9999))
data, addr = server.recvfrom(1024)  # receive from anyone
server.sendto(b"pong", addr)        # send back

# UDP Client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"ping", ("127.0.0.1", 9999))
data, addr = client.recvfrom(1024)
print(data.decode())
```

Notice: no `listen()`, `accept()`, or `connect()` — just `sendto()` and `recvfrom()`.

## 6. Sending an HTTP Request Manually
This is what browsers and `requests` do under the hood:

```python
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("example.com", 80))

request = "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n"
sock.sendall(request.encode())

response = b""
while True:
    chunk = sock.recv(4096)
    if not chunk:
        break
    response += chunk

print(response.decode())
sock.close()
```

High-level libraries like `requests` are just convenient wrappers around these socket calls.

## 7. Error Handling
Network code can fail in many ways — always handle exceptions:

```python
import socket
import errno

try:
    s = socket.socket()
    s.settimeout(5)
    s.connect(("10.0.0.1", 9999))
except socket.timeout:
    print("Server didn't respond in 5 seconds")
except ConnectionRefusedError:
    print("No server on that port")
except OSError as e:
    if e.errno == errno.ECONNRESET:
        print("Connection reset by server")
finally:
    s.close()
```

The key flow to remember: **Server = bind → listen → accept → send/recv → close. Client = connect → send/recv → close.**
