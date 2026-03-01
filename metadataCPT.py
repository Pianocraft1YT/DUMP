#Any line WITHOUT a comment about where it came from is from me.
from PIL import Image, UnidentifiedImageError
import os
from pathlib import Path
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

#Common video file formats to check
video_types = [".mp4", ".mov", ".avi", ".mkv", ".webm", ".wmv"]
#Directory of images path
directory_path = None
#Directory to output .xlsx file to
output_path = None

#Gets called on set directory button press to set image directory
def set_dir():
    global directory_path
    #Googled how to do this
    directory_path = filedialog.askdirectory(title="Select a Directory")
#Gets called on set output button press
def set_output():
    global output_path
    #Googled how to do this
    output_path = filedialog.askdirectory(title="Select a Output Directory")
#Gets called on "Execute" button press 
#Paths supplied by user
def get_exif_metadata(directory_path, output_path):
    #Index and increment counters
    i = 0 
    j = 0
    photos_before_video = 0
    video_present = False

    #Lists to store image data, date, time, and name.
    fixed_time = []
    fixed_date = []
    img_series = []
    list_of_dates = []
    list_of_images = []
    final_images = []
    final_dates = []
    final_times = []
    
    try:
        #List all files in directory given
        #Googled how to do this
        files_and_dirs = os.listdir(directory_path)
        #Sorts files alphabetically, ignoring file extensions and capitalization
        #Googled how to do this
        files_and_dirs.sort(key=lambda x: os.path.splitext(x)[0].lower())
        #Iterates through every file in the directory
        for file in files_and_dirs:
            #If file is not a video, extract metadata from the image.
            #Googled how to do this
            if not file.lower().endswith(tuple(video_types)):
                #ChatGPT helped with this stuff
                img = Image.open(Path(directory_path) / files_and_dirs[i]) #open the image
                exif_data = img.getexif() #get the exif metadata
                dt = exif_data.get(306) or exif_data.get(36867) #only extract date and time
                #Back to my own code
                filename = files_and_dirs[i] #get filename
                list_of_dates.append(dt) #add to lists
                list_of_images.append(filename)
                i += 1 #increment
            else:
                if not video_present: #If a video hasn't been found before
                    photos_before_video = i #For Img # Series use
                    video_present = True #Do not update photos_before_video again
                i += 1 #increment, essentially skipping videos
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

    for date in list_of_dates: #Split the exif metadata into a date list and time list (24h)
        dateslist = str(date).split(" ", maxsplit=1)
        fixed_date.append(dateslist[0])
        fixed_time.append(dateslist[1])
    #Create dataframe to manipulate formatting of dates
    df = pd.DataFrame({"Dates": fixed_date})
    #ChatGPT helped
    df["Date_Datetime"] = pd.to_datetime(df["Dates"], format="%Y:%m:%d")
    formatted_dates = df["Date_Datetime"].dt.strftime("%m/%d/%Y")
    #Turn dataframe back into list for further use
    fixed_date = formatted_dates.to_list()
    i = 1 #Set i to 1 to start at image 1.
    while i <= len(list_of_images):
        if video_present and photos_before_video > 0: 
            if (i % photos_before_video)==1:   #For image + video folders, only add the first image data to the final lists    
                final_images.append(list_of_images[i-1])
                final_dates.append(fixed_date[i-1])
                final_times.append(fixed_time[i-1])
                img_series.append(str(i+j) + "-" + str((i + photos_before_video+j))) #For Img # Series to correctly count the series
                j+=1

            i+=1
        else: #If only images were found, add all photos and increment series normally
            final_images.append(list_of_images[i-1])
            final_dates.append(fixed_date[i-1])
            final_times.append(fixed_time[i-1])
            img_series.append(i) 
            i+=1

    if len(img_series) == len(final_images): #These should match, unless irregular pattern of images + videos was detected
        df = pd.DataFrame( #Create DataFrame
            {
                "Files": final_images,
                "Dates": final_dates,
                "Time": final_times,
                "Image # Series": img_series,
            }
        )
    else: #They didn't match, so show a warning of no series column outputted
        messagebox.showwarning("No series column.", "No series column will be outputted, irregular pattern of photos + videos detected.")
        df = pd.DataFrame( #Create DataFrame without Img # Series
            {
                "Files": final_images,
                "Dates": final_dates,
                "Time": final_times,
            }
        )

    try:
        out_file = Path(output_path) / "output.xlsx" #Output path
        df.to_excel(out_file, sheet_name="Output", index=False) #Make an Excel file for importing
        messagebox.showinfo(
            "Success!", message="Success, outputted at " + output_path + "/output.xlsx" #Tell user where file outputted
        )
        root.destroy() #End program
    except:
        messagebox.showerror( #If no output path was set, error and close
            "No output path set. (Fatal error)", message="No output path set. (Fatal error)"
        )
        root.destroy()


root = tk.Tk() #Tkinter root
root.withdraw() #Hide the root for Apple compatibility
frame = tk.Frame(root) #Tkinter frame window
execute_button = tk.Button(frame, command=lambda:get_exif_metadata(directory_path,output_path), text="Execute") #Buttons to click
set_directory_button = tk.Button(frame, command=set_dir, text="Set folder with images")
set_output_button = tk.Button(frame, command=set_output, text="Set output folder")
frame.pack() #Pack frame and buttons in order
set_directory_button.pack()
set_output_button.pack()
execute_button.pack()
root.geometry("200x120") #Set dimensions of window to open
root.deiconify() #Open window
root.mainloop() #Ensure window only closes by user choice