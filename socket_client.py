import socket

#constants
HOST = "127.0.0.1"
PORT = 42069


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = input("Enter your message (enter nothing to end connection):\n")
        if(message == ""):
                header = 0
        else:
                isCap = input("Do you want to capitalize your message? (y or yes for yes, anything else for no)").toupper()
                header = 1 if isCap == "Y" or isCap == "YE" or isCap == "YES" else 2
        package = str(header) + message
        s.sendall(package.encode('ASCII'))
        data = s.recv(1024)

print(f"Recieved: {data.decode("ASCII")}")



"""
def main():
        print("CLIENT")


if __name__ == "__main__":
        main()
        """