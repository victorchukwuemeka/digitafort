#  import our sockect
import socket 
 
# create our socket instance
servs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
# bind our socket with the port 
servs.bind(('0.0.0.0', 9999))

#listening 
servs.listen(5)


print("Server listening on port 9999...")





#next is the client 
# create cli 
conn , addr = servs.accept()
print(addr)

conn.send(f"welcome to our server")

conn.recv(1024)


print(f"Received: {data.decode()}")


conn.close()
servs.close()

