import socket
import threading

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            print(msg)
        except:
            print("Koneksi terputus.")
            break

def write():
    while True:
        pesan = input("")
        client.send(pesan.encode())

threading.Thread(target=receive).start()
threading.Thread(target=write).start()