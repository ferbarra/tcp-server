import socket # tcp library
import sys
from decouple import config

host = config('HOST')
port = config('PORT', cast=int)
message_size = config('MESSAGE_SIZE', cast=int)

def main():

    try:
        # create the socket using tcp/ip
        socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket initated')
    except socket.error as error:
        print('Unable to initialize socket.')
        print(f'Error code: {error[0]}') 
        print(f'Error message: {error[1]}')
        sys.exit()

    socket_object.bind((host, port))

    socket_object.listen(0)

    connection, address = socket_object.accept()
    print(f'Accepted connection from {address}')
    
    while True: 
        data = connection.recv(message_size).decode()

        if not data:
            break

        print (f'Data received: {data}')
        


    print('Closing socket...')
    socket_object.close()
        

if __name__ == "__main__":
    main()
