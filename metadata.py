from PIL import Image, UnidentifiedImageError
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
series_increment = 0
img_series = []
photos_before_video = 0
video_present = False
j = 1
list_of_dates = []
list_of_images = []
video_types = [".mp4",".mov",".avi",".mkv",".webm",".wmv"]
final_images = []
final_dates = []
final_series = []
final_times = []
def unNest(list, newList):
    for sublist in list:
        for item in sublist:
            newList.append(item)
def set_dir():
    global directory_path
    directory_path = filedialog.askdirectory(title="Select a Directory")
def set_output():
    global output_path
    output_path = filedialog.askdirectory(title="Select a Output Directory")
def get_exif_metadata():
    global root
    global i
    global j
    global video_present
    global series_increment
    global directory_path
    global output_path
    global photos_before_video
    try:
        files_and_dirs = os.listdir(directory_path)
        files_and_dirs.sort(key=lambda p: os.path.getctime(directory_path + "/" + p))
        for file in files_and_dirs:
            if not file.lower().endswith(tuple(video_types)):
                # Open the image file
                img = Image.open(Path(directory_path) / files_and_dirs[i])
                # Get the EXIF data
                exif_data = img.getexif()
                dt = exif_data.get(306) or exif_data.get(36867)
                filename = files_and_dirs[i]                   
                list_of_dates.append(dt)
                list_of_images.append(filename)
                img_series.append(i+1)
                photos_before_video+=1 #maybe should remove later
                i+=1
            else:
                for date in list_of_dates:
                    dateslist = str(date).split(" ",maxsplit=1)
                    fixed_date.append(dateslist[0])
                    fixed_time.append(dateslist[1])
                    split_time_big = fixed_time[i].split(":")
                    split_time_small = fixed_time[i-1]
                    if int(split_time_big[2]) - int(split_time_small[2]) < 2:
                        split_time_big = fixed_time[i-2]
                        if int(split_time_small[2]) - int(split_time_big[2]) < 2:
                            img_series.pop(i)
                            img_series.pop(i-1)
                            img_series.pop(i-2)
                            final_series.append(img_series)
                            final_series.append(i-2 + "-" + i)
                            fixed_date.pop(i-2)
                            fixed_time.pop(i-2)
                            final_dates.append(fixed_date)
                            final_times.append(fixed_time)
                            list_of_images.pop(i-2)
                            final_images.append(list_of_images)
                        else:
                            img_series.pop(i)
                            img_series.pop(i-1)
                            final_series.append(img_series)
                            final_series.append(i-1 + "-" + i)
                            fixed_date.pop(i-1)
                            final_dates.append(fixed_date)
                            fixed_time.pop(i-1)
                            final_times.append(fixed_time)
                            list_of_images.pop(i-1)
                            final_images.append(list_of_images)
                img_series = []
                list_of_dates = []
                list_of_images = []
                fixed_date = []
                fixed_time = []
                photos_before_video = 0
                i+=1
                
    except UnidentifiedImageError as e:
        messagebox.showerror("Image couldn't be scanned.", message="Image couldn't be scanned, is it corrupt? \nError caught: " + str(e) + "\nPlease delete the specified file.")
        return
    except Exception as e:
        messagebox.showerror("Invalid path(s) specified.", message="Invalid path(s) specified. \nError caught: " + str(e))
        return
    
    # while j <= len(files_and_dirs):
    #     if video_present:
    #         img_series.append(str(j)+"-"+str((j+photos_before_video)))
    #         j+=(photos_before_video+1)
    #     else:
    #         img_series.append(j)
    #         j+=1
    unNest(final_images, list_of_images)
    unNest(final_dates, fixed_date)
    unNest(final_times, fixed_time)
    unNest(final_series, img_series)
    df = pd.DataFrame({'Dates': fixed_date})
    df['Date_Datetime'] = pd.to_datetime(df['Dates'], format='%Y:%m:%d')
    formatted_dates = df['Date_Datetime'].dt.strftime('%m/%d/%Y')
    df = pd.DataFrame({'Files': list_of_images,'Dates': formatted_dates, 'Time': fixed_time, 'Image # Series': img_series})
    try:
        out_file = Path(output_path) / "output.xlsx"
        df.to_excel(out_file, sheet_name="Output", index=False)
        messagebox.showinfo("Success!", message="Success, outputted at " + output_path + "/output.xlsx")
        root.destroy()
    except:
        messagebox.showerror("No output path set. (Fatal error)", message="No output path set. (Fatal error)")
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
root.deiconify()
root.mainloop()
