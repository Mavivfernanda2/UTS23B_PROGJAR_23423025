import socket

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(3)

try:
    client.connect((HOST, PORT))
    print("Berhasil terhubung ke server!")

    client.settimeout(2)
    try:
        data = client.recv(1024)
        print("Data diterima:", data.decode())
    except socket.timeout:
        print("Koneksi timeout! (baca data)")

except socket.timeout:
    print("Koneksi timeout! (connect)")

client.close()