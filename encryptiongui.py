import tkinter as tk
from tkinter import *

def pre_process(string):
    string_ord = []
    binary_ord = []
    for c in string:
        string_ord.append(ord(c))
    for i in string_ord:
        binary_ord.append(bin(i))
    return binary_ord


def preprocess_key(string_key):
    int_key = int(string_key)
    binary_key = bin(int_key)
    return binary_key


def xor_cipher(password_binary, binary_key):
    cipher_list = []
    counter = 0
    for b in password_binary:
        x = int(password_binary[counter], 2)
        y = int(binary_key, 2)
        cipher_list.append(x ^ y)
        counter += 1
    return cipher_list


def conversion(binary_list):
    string_list = []
    for i in binary_list:
        string_list.append(chr(i))
    cipher_string = "".join(string_list)
    return cipher_string

def encrypt(key,password):
    cipher_object = conversion(xor_cipher(pre_process(password),preprocess_key(key)))
    print(cipher_object)
    return cipher_object




# creating root object
Default_Height = 500
Default_Width = 600
root = tk.Tk()

var = StringVar()

canvas = tk.Canvas(height=Default_Height, width=Default_Width)
canvas.pack()
background_image = tk.PhotoImage(file="modern.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relheight=1, relwidth=1)

frame = tk.Frame(root, bg="#000000",)
frame.place(relx = 0.5, rely = 0.1, relwidth=0.75, relheight=0.1, anchor="n")


entry = tk.Entry(frame, bg="#FF5733", font =40)
entry.grid(row=0, column=0)

key_entry = tk.Entry(frame, bg="#FF5733", font =40)
key_entry.grid(row=0, column=2)

button = tk.Button(frame, bg="#C70039", text="Set Unencrypted String", activebackground="#C70039", activeforeground="#C70039")
button.grid(row=1, column=0, sticky="w", columnspan=1, rowspan=33)

key_button = tk.Button(frame, bg="#C70039", text="Set Encryption Key", activebackground="#C70039", activeforeground="#C70039", command= lambda: var.set(encrypt(key_entry.get(),entry.get())))
key_button.grid(row=1, column=2, sticky="w", columnspan=1, rowspan=33)




Lower_frame = tk.Frame(root, bg = "#FFFFFF", bd = 10)
Lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(Lower_frame, bg = "#2B2424", textvariable=var, fg ="#C70003", font = "Helvetica 20")
label.place(relwidth=1, relheight=1)

root.mainloop()
