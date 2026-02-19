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
    directory_path = filedialog.askdirectory(title="Select a Directory")

def set_output():
    global output_path
    output_path = filedialog.askdirectory(title="Select a Output Directory")

def get_exif_metadata():
    global root
    global directory_path
    global output_path

    # Local variables (previously globals)
    i = 0
    fixed_time = []
    fixed_date = []
    img_series = []
    photos_before_video = 0
    video_present = False
    j = 1
    list_of_dates = []
    list_of_images = []

    try:
        files_and_dirs = os.listdir(directory_path)
        files_and_dirs.sort(key=lambda p: os.path.getctime(directory_path + "/" + p))

        for file in files_and_dirs:
            if not file.lower().endswith(tuple(video_types)):
                img = Image.open(Path(directory_path) / files_and_dirs[i])
                exif_data = img.getexif()
                dt = exif_data.get(306) or exif_data.get(36867)
                filename = files_and_dirs[i]
                list_of_dates.append(dt)
                list_of_images.append(filename)
                i += 1
            else:
                if not video_present:
                    photos_before_video = i
                    video_present = True
                i += 1

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

    while j <= len(files_and_dirs):
        if video_present:
            img_series.append(str(j) + "-" + str((j + photos_before_video)))
            j += photos_before_video + 1
        else:
            img_series.append(j)
            j += 1

    df = pd.DataFrame({"Dates": fixed_date})
    df["Date_Datetime"] = pd.to_datetime(df["Dates"], format="%Y:%m:%d")
    formatted_dates = df["Date_Datetime"].dt.strftime("%m/%d/%Y")

    if len(img_series) == len(list_of_images):
        df = pd.DataFrame(
            {
                "Files": list_of_images,
                "Dates": formatted_dates,
                "Time": fixed_time,
                "Image # Series": img_series,
            }
        )
    else:
        messagebox.showwarning("No series column.", "No series column will be outputted, irregular pattern of photos + videos detected.")
        df = pd.DataFrame(
            {
                "Files": list_of_images,
                "Dates": formatted_dates,
                "Time": fixed_time,
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
execute_button = tk.Button(frame, command=get_exif_metadata, text="Execute")
set_directory_button = tk.Button(frame, command=set_dir, text="Set folder with images")
set_output_button = tk.Button(frame, command=set_output, text="Set output folder")
frame.pack()
set_directory_button.pack()
set_output_button.pack()
execute_button.pack()
root.geometry("200x80")
root.deiconify()
root.mainloop()