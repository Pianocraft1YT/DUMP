#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.title('Authentication')
# create empty frame
def Login(password, username):
    if username == "Genshin" and password == "Impact":
        print("Login success!")
    else:
        print("wrong")
def get_text():
    password = password_entry.get()
    username = username_entry.get()
    Login(password, username)
frame_login = tk.Frame(root)
frame_login.grid(column=0, row=0)
lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()
username = ""
username_entry = tk.Entry(frame_login, width=7, textvariable=username)
username_entry.pack()
lbl_password = tk.Label(frame_login,text="Password:",font="Courier")
lbl_password.pack()
password = ""
password_entry = tk.Entry(frame_login, width=7, textvariable=password)
password_entry.pack()

Enter = tk.Button(frame_login, text="Login", command=get_text)

Enter.pack()
root.mainloop()