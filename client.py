import socket
import threading

def receive_msg(client):
    while True:
        try:
            response = client.recv(1024).decode()
            print(response)
        except:
            pass

def send_msg(client, user):
    while True:
        try:
            message = input()
            client.send(f"{user}: {message}".encode())
        except:
            pass

def connect_client(IP, PORT):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP, PORT))


        print("Welcome To CLI-Chat\n")
        userName = input("Enter Your Name: \n")

        #Recive Message
        rec_thread = threading.Thread(target=receive_msg, args=(client,))
        #Send Message
        send_thread = threading.Thread(target=send_msg, args=(client, userName))

        rec_thread.start()
        send_thread.start()

        rec_thread.join()
        send_thread.join()
    except:
        print("Unable to connect to server.")
    try:
        pass
    except:
        pass
IP = "127.0.0.1"
PORT = 8080
connect_client(IP, PORT)