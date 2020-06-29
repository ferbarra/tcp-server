import socket

host = "127.0.0.1"
port = 5001

def get_user_input():
    return input('? ')

def main():
    
    print("Connecting to server...")
    socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_object.connect((host, port))
    print("Connection established")

    user_input = get_user_input()

    socket_object.send('caca'.encode())

    while user_input != 'q' and False:
        socket_object.send(user_input.encode())
        print("Message sent")

        # get the next message
        user_input = get_user_input()

    socket_object.close()

    

if __name__ == "__main__":
    main()
