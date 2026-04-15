from openpyxl import Workbook
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
path = ""
def make_range():
    global path
    if path != "":
        wb = Workbook()
        ws = wb.active
        ws.title = "Ranges"
        try:
            stop = int(stop_entry.get())
            start = int(start_entry.get())
            increment = int(increment_entry.get())
        except:
            messagebox.showerror("One or more required fields are empty.", "One or more required fields are empty.")
        row = 1
        if stop > 0 and start > 0 and increment > 0:
            if start+increment < stop:
                while start < stop:
                    end = start + increment
                    ws.cell(row=row, column=1, value=f"{start}-{end}")
                    start += (increment+1)
                    row += 1

                wb.save(path+"/range.xlsx")
                messagebox.showinfo("Success!", "Success, outputted at " + path+"/range.xlsx")
                root.destroy()
            else:
                messagebox.showerror("Starting index + increment is bigger than stopping index.", "Starting index + increment is bigger than stopping index.")
        else:
            messagebox.showerror("Please enter values greater than zero.", "Please enter values greater than zero.")
    else:
        messagebox.showerror("No output destination set.", "No output destination set.")
def set_output():
    global path
    path = filedialog.askdirectory(title="Select a Directory")

def incrementFocusIn(event):
    if increment_entry.get() == "Increment amount":
        increment_entry.delete(0, "end")
        increment_entry.config(foreground="black")
def incrementFocusOut(event):
    if increment_entry.get() == "":
        increment_entry.insert(0, "Increment amount")
        increment_entry.config(foreground="gray")
def startFocusIn(event):
    if start_entry.get() == "Starting index":
        start_entry.delete(0, "end")
        start_entry.config(foreground="black")
def startFocusOut(event):
    if start_entry.get() == "":
        start_entry.insert(0, "Starting index")
        start_entry.config(foreground="gray")
def stopFocusIn(event):
    if stop_entry.get() == "Stopping index":
        stop_entry.delete(0, "end")
        stop_entry.config(foreground="black")
def stopFocusOut(event):
    if stop_entry.get() == "":
        stop_entry.insert(0, "Stopping index")
        stop_entry.config(foreground="gray")

root = tk.Tk()
frame = tk.Frame(root)
execute_button = tk.Button(frame, command=make_range, text="Execute")
set_output_button = tk.Button(frame, command=set_output, text="Set output folder")
increment_entry = tk.Entry(frame,width=20,foreground="gray")
increment_entry.insert(0, "Increment amount")
start_entry = tk.Entry(frame, width=20, foreground="gray")
start_entry.insert(0, "Starting index")
stop_entry = tk.Entry(frame, width=20, foreground="gray")
stop_entry.insert(0, "Stopping index")
increment_entry.bind("<FocusIn>", incrementFocusIn)
increment_entry.bind("<FocusOut>", incrementFocusOut)
start_entry.bind("<FocusIn>", startFocusIn)
start_entry.bind("<FocusOut>", startFocusOut)
stop_entry.bind("<FocusIn>", stopFocusIn)
stop_entry.bind("<FocusOut>", stopFocusOut)
frame.pack()
set_output_button.pack()
increment_entry.pack()
start_entry.pack()
stop_entry.pack()
execute_button.pack()
root.mainloop()