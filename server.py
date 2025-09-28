import socket
import threading

clients = []

def manage_client(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024)
            if not msg:
                break
            broadcast_msg(msg, client_socket)
        except:
            pass

def broadcast_msg(msg, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(msg)
        else:
            pass
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = "127.0.0.1"
    PORT = 8080

    server.bind((IP,PORT))
    server.listen(10)

    while True:
        client_socket, address = server.accept()
        clients.append(client_socket)
        print(f"Total Connected users is/are: {len(clients)}")

        thread = threading.Thread(target=manage_client, args=(client_socket,))

        thread.start()
start_server()