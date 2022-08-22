import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox = None
filePathLabel = None
global soung_counter
song_counter = 0


def musicWindow():
    
    
    global song_counter
    global filePathLabel
    global listbox
    global infoLabel

    window = Tk()
    window.title('music Window')
    window.geometry("300x300")
    window.configure(bg = 'purple')

    selectlabel = Label(window, text = 'Select Song', bg = 'purple', font = ('Calbiri', 8))
    selectlabel.place(x = 2, y = 1)

    listbox = Listbox(window, height = 10, width = 39, activestyle = 'dotbox', bg = 'purple', borderwidth = 2, font = ('Calbiri', 10))
    listbox.place(x = 10, y = 10)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1, relx = 1)
    scrollbar1.config(command = listbox.yview)

    PlayButton = Button(window, text = 'Play', width = 10, bd = 1, bg = 'Skyblue', font = ('Calbiri', 10))
    PlayButton.place(x = 30, y = 200)

    Stop = Button(window, text = 'Stop', width = 10, bd = 1, bg = 'Skyblue', font = ('Calbiri', 10))
    Stop.place(x = 200, y = 200)

    Upload = Button(window, text = 'Upload', width = 10, bd = 1, bg = 'Skyblue', font = ('Calbiri', 10))
    Upload.place(x = 30, y = 250)

    Download = Button(window, text = 'play', width = 10, bd = 1, bg = 'Skyblue', font = ('Calbiri', 10))
    Download.place(x = 200, y = 250)

    infoLabel = Label(window, text = '', fg = 'blue', font = ('Calbiri', 8))
    infoLabel.place(x = 4, y = 280)
    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    musicWindow()

setup()
