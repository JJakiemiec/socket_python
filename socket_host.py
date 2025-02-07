import socket

# constants
HOST = "127.0.0.1" #localhost
PORT = 42069

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"initiating server on {HOST}:{PORT}")
        s.bind((HOST, PORT))
        isRunning = True


        while(isRunning):
                print("listening...")
                s.listen()
                conn, addr = s.accept()
                print(f"connection from {addr[0]}:{addr[1]}")
                with conn:
                        print(f"Connected by {addr}")
                        while True:
                                data = conn.recv(1024)
                                if not data:
                                        break
                                package = data.decode('ASCII')
                                header = package[0]
                                print(header)
                                if header == '0':                         #stop server
                                        conn.sendall(b'stopping server')
                                        isRunning = False
                                elif header == '1':                       #capitalize message
                                        message = package[1:]
                                        message = message.upper()
                                        print(message)
                                        conn.sendall(message.encode('ASCII'))
                                else:                                   #echo message
                                        message = package[1:]
                                        print(message)
                                        conn.sendall(message.encode('ASCII'))
                                
                                
"""
def main():
        print("SERVER")


if __name__ == "__main__":
        main()
"""