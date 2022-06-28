import socket
from threading import Thread
from tkinter import Text, Button, Tk, END

def sendMsg():
    textBox = your_msg.get("1.0", END)
    message = f"User 2: {textBox}"
    message = message.encode()
    client_socket.send(message)
    print("message has been sent...")


def receive():
    while True:
        incoming_message = client_socket.recv(1024)
        incoming_message = incoming_message.decode()
        mainScreen.insert(END, f"{incoming_message}\n")
        mainScreen.tag_add("tag_name", "1.0", "end")



window = Tk()
window.geometry("800x700")
window.title("My Chat App")

mainScreen = Text(width="80",height="25", padx="50", bg="white")
mainScreen.tag_configure("tag_name", justify="center")
mainScreen.pack()



your_msg = Text(window, width="30", height="5")
your_msg.pack()

send = Button(width=10, text="Send", bg="#e0fbfc", command=sendMsg)
send.pack()


client_socket = socket.socket()
host = socket.gethostname()
port = 8080

client_socket.connect((host, port))

print("Connected to chat server")

thread = Thread(target=receive)
thread.start()

window.mainloop()

