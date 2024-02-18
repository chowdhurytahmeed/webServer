from socket import *
import sys
def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind(("", port))
    serverSocket.listen(1)
    while True:
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message =  connectionSocket.recv(1024).decode()
            filename = message.split()[1]
            f=open(filename[1:],'r')
            outputdata=f.readlines()
            f.close()

            connectionSocket.send(b"HTTP/1.1 200 OK\r\n")
            connectionSocket.send(b"Content-Type: text/html; charset=UTF-8\r\n")
            connectionSocket.send(b"Connection: close\r\n\r\n")

            for index in range(0, len(outputdata)):
                connectionSocket.send(outputdata[index].encode())
            connectionSocket.send("\r\n".encode())

            connectionSocket.close()

        except IOError:
            connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n")
            connectionSocket.send(b"Content-Type: text/html\r\n\r\n")
            connectionSocket.close()
    serverSocket.close()
    sys.exit()

if __name__ == "__main__":
    webServer(13331)