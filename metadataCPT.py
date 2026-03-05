#Any line WITHOUT a comment about where it came from is from me.
from PIL import Image, UnidentifiedImageError
import os
from pathlib import Path
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

video_types = [".mp4", ".mov", ".avi", ".mkv", ".webm", ".wmv"]
directory_path = None
output_path = None

def set_dir():
    global directory_path
    #Googled how to do this
    directory_path = filedialog.askdirectory(title="Select a Directory")

def set_output():
    global output_path
    #Googled how to do this
    output_path = filedialog.askdirectory(title="Select a Output Directory")

def get_exif_metadata(directory_path, output_path):
    i = 0 
    j = 0
    photos_before_video = 0
    video_present = False

    fixed_time = []
    fixed_date = []
    img_series = []
    list_of_dates = []
    list_of_images = []
    final_images = []
    final_dates = []
    final_times = []
    
    try:
        #Googled how to do this
        files_and_dirs = os.listdir(directory_path)
        #Googled how to do this
        files_and_dirs.sort(key=lambda x: os.path.splitext(x)[0].lower())
        for file in files_and_dirs:
            #Googled how to do this
            if not file.lower().endswith(tuple(video_types)):
                #ChatGPT helped with this stuff
                img = Image.open(Path(directory_path) / files_and_dirs[i])
                exif_data = img.getexif()
                dt = exif_data.get(306) or exif_data.get(36867)
                #Back to my own code
                filename = files_and_dirs[i]
                list_of_dates.append(dt)
                list_of_images.append(filename)
                i += 1
            else:
                if not video_present:
                    photos_before_video = i
                    video_present = True
                i += 1
    #Googled how to catch this type of error
    except UnidentifiedImageError as e:
        messagebox.showerror(
            "Image couldn't be scanned.",
            message="Image couldn't be scanned, is it corrupt? \nError caught: "
            + str(e)
            + "\nPlease delete the specified file.",
        )
        return
    except Exception as e:
        messagebox.showerror(
            "Invalid path(s) specified.", message="Invalid path(s) specified. \nError caught: "
            + str(e)
        )
        return

    for date in list_of_dates:
        dateslist = str(date).split(" ", maxsplit=1)
        fixed_date.append(dateslist[0])
        fixed_time.append(dateslist[1])

    df = pd.DataFrame({"Dates": fixed_date})
    #ChatGPT helped
    df["Date_Datetime"] = pd.to_datetime(df["Dates"], format="%Y:%m:%d")
    formatted_dates = df["Date_Datetime"].dt.strftime("%m/%d/%Y")
    fixed_date = formatted_dates.to_list()

    i = 1
    while i <= len(list_of_images):
        if video_present and photos_before_video > 0: 
            if (i % photos_before_video)==1:
                final_images.append(list_of_images[i-1])
                final_dates.append(fixed_date[i-1])
                final_times.append(fixed_time[i-1])
                img_series.append(str(i+j) + "-" + str((i + photos_before_video+j)))
                j+=1
            i+=1
        else:
            final_images.append(list_of_images[i-1])
            final_dates.append(fixed_date[i-1])
            final_times.append(fixed_time[i-1])
            img_series.append(i) 
            i+=1

    if len(img_series) == len(final_images):
        df = pd.DataFrame(
            {
                "Files": final_images,
                "Dates": final_dates,
                "Time": final_times,
                "Image # Series": img_series,
            }
        )
    else:
        messagebox.showwarning("No series column.", "No series column will be outputted, irregular pattern of photos + videos detected.")
        df = pd.DataFrame(
            {
                "Files": final_images,
                "Dates": final_dates,
                "Time": final_times,
            }
        )

    try:
        out_file = Path(output_path) / "output.xlsx"
        df.to_excel(out_file, sheet_name="Output", index=False)
        messagebox.showinfo(
            "Success!", message="Success, outputted at " + output_path + "/output.xlsx"
        )
        root.destroy()
    except:
        messagebox.showerror(
            "No output path set. (Fatal error)", message="No output path set. (Fatal error)"
        )
        root.destroy()


root = tk.Tk()
root.withdraw()
frame = tk.Frame(root)
execute_button = tk.Button(frame, command=lambda:get_exif_metadata(directory_path,output_path), text="Execute")
set_directory_button = tk.Button(frame, command=set_dir, text="Set folder with images")
set_output_button = tk.Button(frame, command=set_output, text="Set output folder")
frame.pack()
set_directory_button.pack()
set_output_button.pack()
execute_button.pack()
root.geometry("200x120")
root.deiconify()
root.mainloop()