from PIL import Image
from PIL.ExifTags import TAGS
import os
from pathlib import Path
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

i = 0
fixed_time = []
fixed_date = []



list_of_dates = []
list_of_images = []
def set_dir():
    global directory_path
    directory_path = filedialog.askdirectory(title="Select a Directory")
def set_output():
    global output_path
    output_path = filedialog.askdirectory(title="Select a Output Directory")
def get_exif_metadata():
    global root
    global i
    global directory_path
    global output_path
    try:
        files_and_dirs = os.listdir(directory_path)
        while (i < len(files_and_dirs)):
            for file in files_and_dirs:
                if file.find(".MOV") == -1:
                    # Open the image file
                    img = Image.open((directory_path) + (r'\\') +  files_and_dirs[i])
                    # Get the EXIF data
                    exif_data = img.getexif()
                    
                    dt = exif_data.get(306) or exif_data.get(36867)
                    filename = files_and_dirs[i]
                    list_of_dates.append(dt)
                    list_of_images.append(filename)
                    i+=1
                else:
                    i+=1
                
    except:
        messagebox.showerror("Invalid path(s) specified.", message="Invalid path(s) specified.")
        return
    for date in list_of_dates:
        dateslist = str(date).split(" ",maxsplit=1)
        fixed_date.append(dateslist[0])
        fixed_time.append(dateslist[1])
    df = pd.DataFrame({'Dates': fixed_date})
    df['Date_Datetime'] = pd.to_datetime(df['Dates'], format='%Y:%m:%d')
    formatted_dates = df['Date_Datetime'].dt.strftime('%m/%d/%Y')
    df = pd.DataFrame({'Files': list_of_images,'Dates': formatted_dates, 'Time': fixed_time})
    try:
        df.to_excel(output_path + "\\output.xlsx", sheet_name="Output", index=False)
        messagebox.showinfo("Success!", message="Success, outputted at " + output_path + "\\output.xlsx")
        root.destroy()
    except:
        messagebox.showerror("No output path set. (Fatal error)", message="No output path set. (Fatal error)")
        root.destroy()

root = tk.Tk()
frame = tk.Frame(root)
execute_button = tk.Button(frame, command=get_exif_metadata, text="Execute")
set_directory_button = tk.Button(frame, command=set_dir, text="Set folder with images")
set_output_button = tk.Button(frame, command=set_output, text="Set output folder")
frame.pack()
set_directory_button.pack()
set_output_button.pack()
execute_button.pack()
root.mainloop()
