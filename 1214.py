#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.title('Authentication')
# create empty frame
def showNewCorrect():
    root.withdraw()
    root2 = tk.Tk()
    root2.wm_geometry("200x200")
    root2.title("SUCCESS!")
    frame_correct = tk.Frame(root2)
    frame_correct.grid()
    lbl_correct = tk.Label(frame_correct, text="CORRECT!", font="Times, 20")
    lbl_correct.pack()
def showNewFrame(): 
    root.withdraw()
    root1 = tk.Tk()
    root1.wm_geometry("200x200")
    root1.title("WRONG!")
    
    frame_wrong = tk.Frame(root1)
    frame_wrong.grid()
    
    lbl_wrong = tk.Label(frame_wrong, text="WRONG!", font="Times, 26")
    lbl_wrong.pack()
def Login(password, username):
    if username == "Genshin" and password == "Impact":
        showNewCorrect()
    else:
        showNewFrame()
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