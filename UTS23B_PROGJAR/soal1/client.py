import socket

HOST = '127.0.0.1'
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

msg = "Tes Koneksi"
client.sendall(msg.encode())

data = client.recv(1024).decode()
print("Balasan dari server:", data)

client.close()