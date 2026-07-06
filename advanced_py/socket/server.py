import socket 


#create our socket 
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binding our port to the address 
serv.bind(("0.0.0.0",9999))


serv.listen(5)

print("it is hearing the stuff from port:" , {9999})

# Wait for a client to connect (this blocks)
conn, addr = serv.accept()
print(f"Connected by {addr}")

# Send a message to the client
conn.send(b"Welcome to the server!")

# Receive data from the client
data = conn.recv(1024)
print(f"Received: {data.decode()}")

# Clean up
conn.close()
serv.close()