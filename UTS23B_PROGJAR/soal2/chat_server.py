import socket
import threading

HOST = "0.0.0.0"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(conn, addr):
    print(f"Client baru: {addr}")
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            broadcast(msg, conn)
        except:
            break

    clients.remove(conn)
    conn.close()
    print(f"Client keluar: {addr}")

print(f"Chat Server berjalan di port {PORT}...")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()