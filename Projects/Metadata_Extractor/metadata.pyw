# Dear programmer:
# When I wrote this code, only God and I knew how it worked.
# Now, only God knows!
# 
# Therefore, if you trying to improve this,
# Please increment this counter as a warning
# For the next person:
# 
# hours_spent_here = 20

# Coded by Pianocraft1YT
# Tutorial: https://youtu.be/ruWNKBdbYoo

from PIL import Image, UnidentifiedImageError
import os
import sys
from pathlib import Path
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def nameFocusIn(event):
    if name_entry.get() == "Filename (default output.xlsx)":
        name_entry.delete(0, "end")
        name_entry.config(foreground="black")
def nameFocusOut(event):
    if name_entry.get() == "":
        name_entry.insert(0, "Filename (default output.xlsx)")
        name_entry.config(foreground="gray")

#Common video file formats to check
video_types = (".mp4", ".mov", ".avi", ".mkv", ".webm", ".wmv")
#Common and uncommon image formats to check
photo_types = ("jpg", "jpeg", "heic", "heif", "png", "tiff", "tif", "dng", "crw", "cr2", "cr3", "nef", "nrw", "arw", "srf", "sr2", "raf", "rw2", "raw", "orf", "ori", "pef", "ptx", "rwl", "3fr", "fff", "iiq", "mos", "x3f", "kdc", "dcr", "dcs", "srw", "mrw")
#Directory of images path
directory_path = None
#Directory to output .xlsx file to
output_path = None
#For debugging only, manually set
debug = False
#Gets called on set directory button press to set image directory
def reset():
    used.clear()
    results.clear()
def set_dir():
    global directory_path
    directory_path = Path(filedialog.askdirectory(title="Select a Directory"))
#Gets called on set output button press
def set_output():
    global output_path
    output_path = Path(filedialog.askdirectory(title="Select a Output Directory"))
def scan_image(directory_path, files_and_dirs, i, list_of_dates, list_of_images):
    img = Image.open(Path(directory_path) / files_and_dirs[i]) #Open the image in code
    exif_data = img.getexif() #Get the exif metadata
    dt = exif_data.get(306) or exif_data.get(36867) #Only extract date and time
    filename = files_and_dirs[i] #Get filename
    if dt is None:
        raise ValueError(f"No metadata found for {filename}")
    list_of_dates.append(dt) #Add to lists
    list_of_images.append(filename)
def find_directories(directory_path, final_output):
    global current_sheet_name
    name_index = 0
    directories_found = os.listdir(directory_path) #Only one level of recursion
    directories_to_scan = []
    sheet_names = []
    for directory in directories_found:
        current_directory = Path(directory_path.as_posix() + "/" + directory)
        if not current_directory.is_dir():
            continue
        with os.scandir(current_directory) as entries:
            photo_count = sum(1 for entry in entries if entry.is_file() and entry.name.lower().endswith((photo_types)))
            if photo_count > 0:
                directories_to_scan.append(current_directory)
                sheet_names.append(directory) #Just the directory name, not the full path
    for directory_path in directories_to_scan:
        current_sheet_name = sheet_names[name_index]
        name_index+=1
        sort_and_extract_irregular(directory_path, True, final_output)
    create_sheet(final_output, True, None)
def check_recursive(directory_path):
    global output_path
    if debug: #No need to set output_path every time
                output_path = Path.home() / "Downloads"
    if directory_path == None or output_path == None:
            messagebox.showerror( #If no output/directory path was set, error to allow for changes
                        "Invalid path(s) specified.", message="Please set an image/video directory path OR output path.")
            return
    reset()
    if name_entry.get() != "Filename (default output.xlsx)":
        final_output = Path(output_path) / clean_name(name_entry.get())
    else:
        final_output = Path(output_path) / "output.xlsx"
    recursive = recursive_var.get()
    if recursive:
        find_directories(directory_path, final_output)
    else:
        with os.scandir(directory_path) as entries:
                photo_count = sum(1 for entry in entries if entry.is_file() and entry.name.lower().endswith((photo_types)))
                if photo_count > 0:
                    sort_and_extract_irregular(directory_path, False, final_output)
                else:
                        messagebox.showerror("Empty directory", message="No files were found. Please select a valid directory")
                        return
#For verify_name
used = set()
def verify_name(name):
    illegal_chars = ("[", "]", ":", "*", "?", "/", "\\")
    for c in illegal_chars:
        name = name.replace(c, "_")
    name = name[:31]
    if len(name) < 1:
        name = "Sheet"
    if name.lower() not in used:
        used.add(name.lower())
        return name
    f = 2
    while True:
        suffix = "_" + str(f)
        candidate = name[:31 - len(suffix)] + suffix
        if candidate.lower() not in used:
            used.add(candidate.lower())
            return candidate
        f += 1
def clean_name(name):
    #Windows-illegal filename characters
    illegal_chars = ("<", ">", ":", "\"", "/", "\\", "|", "?", "*")
    for c in illegal_chars:
        name = name.replace(c, "_")
    #Trim whitespace and trailing dots (Windows strips trailing dots silently)
    name = name.strip().rstrip(".")
    #Fall back if the user typed only illegal chars or spaces
    if len(name) < 1:
        name = "output"
    #Append .xlsx if the user didn't include it
    if not name.lower().endswith(".xlsx"):
        name += ".xlsx"
    return name
#Gets called initially, assumes irregular pattern, calls sort_and_extract() if regular
def sort_and_extract_irregular(directory_path, recursive, final_output):
    global output_series
    output_series = True
    list_of_dates = []
    list_of_images = []
    img_series = []
    photos_before_video_updated = False
    i = 0 #Internal usage to scan files
    index = 1 #External usage for real indexing
    #last = None #For last filetype scanned
    pattern_check = 1
    regular_pattern_found = False
    video_first = False
    second_video = False
    initial_check = 1
    photos_before_video = 0
    try:
        #List all files in directory given
        all_files = os.listdir(directory_path)
        files_and_dirs = [f for f in all_files if f.lower().endswith((photo_types + video_types))]        #Sorts files alphabetically, ignoring file extensions and capitalization
        files_and_dirs.sort(key=lambda x: os.path.splitext(x)[0].lower())
        #Iterates through every file in the directory
        for file in files_and_dirs:
            #If file is not a video, extract metadata from the image.
            if not file.lower().endswith((video_types)):
                if i == 0:
                    photos_before_video+=1
                    while photos_before_video_updated == False:
                        if i+initial_check < len(files_and_dirs):
                            if files_and_dirs[i+initial_check].lower().endswith((photo_types)):
                                photos_before_video+=1
                                initial_check+=1
                            else:
                                photos_before_video_updated = True
                                if photos_before_video > 5: #Irregular pattern, unreliable. Do not output series.
                                    output_series = False
                        else:
                            photos_before_video_updated = True
                            photos_before_video = 0
                if (i == 0 and photos_before_video == 0) or output_series == False:
                    sort_and_extract(directory_path,recursive, final_output)
                    return
                if photos_before_video_updated and regular_pattern_found == False:
                    end = False
                    while pattern_check < photos_before_video:
                        if photos_before_video+i > len(files_and_dirs)-1:
                            regular_pattern_found=True
                            end = True
                            break
                        if files_and_dirs[pattern_check+i].lower().endswith((photo_types)):
                            pass
                        pattern_check+=1
                    if not end:
                        if (i+pattern_check < len(files_and_dirs) and files_and_dirs[i+pattern_check].lower().endswith((video_types))):
                            regular_pattern_found = True
                        else:
                            if not video_first:
                                img_series.append(str(index))
                                scan_image(directory_path, files_and_dirs, i, list_of_dates, list_of_images)
                            else:
                                img_series.append(str(index-1))
                                scan_image(directory_path, files_and_dirs, i, list_of_dates, list_of_images)
                    else:
                        for r in range(photos_before_video):
                            if (i+r<len(files_and_dirs)):
                                if files_and_dirs[i+r].lower().endswith(photo_types):
                                    scan_image(directory_path, files_and_dirs, i+r, list_of_dates, list_of_images)
                                    img_series.append(str(index+r))
                        # messagebox.showerror("Ended in an image", message="Please make sure the last images are cataloged as a set, if they are to be.")

                pattern_check = 1
                #last = "image"
                i += 1 #increment
                index+=1
            else:
                if (photos_before_video_updated == False and video_first):
                    photos_before_video = i-1
                    photos_before_video_updated = True
                if (photos_before_video_updated == False and i != 0):
                    photos_before_video = i  #For Img # Series use
                    photos_before_video_updated = True #Do not update photos_before_video again
                if video_first and second_video == False:
                    second_video = True
                    img_series.append(str(i-photos_before_video) + "-" + str(i))
                    scan_image(directory_path, files_and_dirs, i-1, list_of_dates, list_of_images)
                if (i==0):
                    video_first = True
                #last = "video"
                if regular_pattern_found:
                    if not video_first:
                        img_series.append(str(index-photos_before_video) + "-" + str(index)) #Image + video series
                        scan_image(directory_path, files_and_dirs, i-1, list_of_dates, list_of_images)
                    else:
                        img_series.append(str(i-photos_before_video) + "-" + str(i)) 
                        scan_image(directory_path, files_and_dirs, i-1, list_of_dates, list_of_images)
                    regular_pattern_found = False
                i += 1 #increment, essentially skipping videos
                index+=1
    except ValueError as e:
        messagebox.showerror("Metadata missing", message=str(e))
        return
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
            "An error occurred.", message="An error occurred. \nError caught: "
            + str(e)
        )
        return
    fixed_date, fixed_time = fix_time(list_of_dates)
    df = create_dataframe(img_series, list_of_images, fixed_date, fixed_time, recursive, directory_path)
    if not recursive:
        create_sheet(final_output, recursive, df)
#Gets called on "Execute" button press 
#Paths supplied by user or debug mode
#Assumes regular pattern
def sort_and_extract(directory_path, recursive, final_output):
    global output_series
    list_of_dates = []
    list_of_images = []
    video_first = False
    i = 0
    photos_before_video = 0
    photos_before_video_updated = False
    try:
        #List all files in directory given
        all_files = os.listdir(directory_path)
        files_and_dirs = [f for f in all_files if f.lower().endswith((photo_types + video_types))]
        #Sorts files alphabetically, ignoring file extensions and capitalization
        files_and_dirs.sort(key=lambda x: os.path.splitext(x)[0].lower())
        #Iterates through every file in the directory
        while i < len(files_and_dirs):
            #If file is not a video, extract metadata from the image.
            if not files_and_dirs[i].lower().endswith((video_types)):
                img = Image.open(Path(directory_path) / files_and_dirs[i]) #open the image
                exif_data = img.getexif() #get the exif metadata
                dt = exif_data.get(306) or exif_data.get(36867) #only extract date and time
                filename = files_and_dirs[i] #get filename
                list_of_dates.append(dt) #add to lists
                list_of_images.append(filename)
                i += 1 #increment
            else:
                if output_series:
                    if not photos_before_video_updated: #If a video hasn't been found before
                        if (photos_before_video_updated == False and video_first):
                                photos_before_video = i-1
                        if (i != 0):
                            photos_before_video = i  #For Img # Series use
                            photos_before_video_updated = True #Do not update photos_before_video again
                        else:
                            video_first = True #Video was found first
                            messagebox.showerror("Video found first.", message="Please manually catalog the first video file, which doesn't have an image pair.")
                i += 1 #increment, essentially skipping videos
    except ValueError as e:
        messagebox.showerror("Metadata missing", message=str(e))
        return
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
            "An error occurred.", message="An error occurred. \nError caught: "
            + str(e)
        )
        return
    fixed_date, fixed_time = fix_time(list_of_dates)
    img_series, final_images, final_dates, final_times = make_series(list_of_images,photos_before_video_updated,photos_before_video,fixed_date,fixed_time)
    df = create_dataframe(img_series, final_images, final_dates, final_times, recursive, directory_path)
    if not recursive:
        create_sheet(final_output, recursive, df)

#For regular patterns only
def make_series(list_of_images, photos_before_video_updated, photos_before_video, fixed_date, fixed_time):
    global output_series
    if output_series:
        i = 1 #Set i to 1 to start at image 1.
        j = 0
        final_images = []
        final_dates = []
        final_times = []
        img_series = []
        while i <= len(list_of_images):
            if photos_before_video_updated and photos_before_video > 0: 
                if (i % photos_before_video)==0:   #For image + video folders, only add the first image data to the final lists    
                    final_images.append(list_of_images[i-1])
                    final_dates.append(fixed_date[i-1])
                    final_times.append(fixed_time[i-1])
                    img_series.append(str(i - photos_before_video + 1) + "-" + str(i + 1)) #For Img # Series to correctly count the series
                    j+=1

                i+=1
            else: #If only images were found, add all photos and increment series normally
                final_images.append(list_of_images[i-1])
                final_dates.append(fixed_date[i-1])
                final_times.append(fixed_time[i-1])
                img_series.append(i) 
                i+=1
    else:
        final_images = list_of_images
        final_dates = fixed_date
        final_times = fixed_time
        img_series = None
    return img_series, final_images, final_dates, final_times

def fix_time(list_of_dates):
    fixed_time = []
    fixed_date = []
    for date in list_of_dates: #Split the exif metadata into a date list and time list (24h)
        dateslist = str(date).split(" ", maxsplit=1)
        fixed_date.append(dateslist[0])
        fixed_time.append(dateslist[1])
    #Create dataframe to manipulate formatting of dates
    df = pd.DataFrame({"Dates": fixed_date})
    df["Date_Datetime"] = pd.to_datetime(df["Dates"], format="%Y:%m:%d")
    formatted_dates = df["Date_Datetime"].dt.strftime("%m/%d/%Y")
    #Turn dataframe back into list for further use
    fixed_date = formatted_dates.to_list()
    return fixed_date, fixed_time

#Variable for use with recursive directories
results = []
def create_dataframe(img_series, final_images, final_dates, final_times, recursive, directory_path):
        global output_series
        if not recursive:
            if output_series:
                df = pd.DataFrame( #Create DataFrame
                    {
                        "Files": final_images,
                        "Dates": final_dates,
                        "Time": final_times,
                        "Image # Series": img_series,
                    }
                )
            else:
                df = pd.DataFrame( #Create DataFrame
                    {
                        "Files": final_images,
                        "Dates": final_dates,
                        "Time": final_times,
                    }
                )
                messagebox.showerror( #If irregular pattern starts with more than 5 images in a row, will break program, so error.
                    "An error occurred.", message="Unpredictable pattern found with directory\n" + directory_path.as_posix() + ".\nPlease add mock files to the beginning to set correct pattern." \
                    " For example, if the pattern is 3 photos and 1 video, choose 3 photos and 1 video and duplicate them, naming them to be first when sorted, like DCSF0000."
                )
            return df
        else:
            global current_sheet_name
            if output_series:
                df = pd.DataFrame( #Create DataFrame
                    {
                        "Files": final_images,
                        "Dates": final_dates,
                        "Time": final_times,
                        "Image # Series": img_series,
                    }
                )
            else:
                df = pd.DataFrame( #Create DataFrame
                    {
                        "Files": final_images,
                        "Dates": final_dates,
                        "Time": final_times,
                    }
                )
                messagebox.showerror( #If irregular pattern starts with more than 5 images in a row, will break program, so error.
                    "An error occurred.", message="Unpredictable pattern found with directory\n" + directory_path.as_posix() + ".\nPlease add mock files to the beginning to set correct pattern." \
                    " For example, if the pattern is 3 photos and 1 video, choose 3 photos and 1 video and duplicate them, naming them to be first when sorted, like DCSF0000."
                )
        if final_images:
            current_sheet_name = verify_name(current_sheet_name)
            results.append((df, current_sheet_name))
def create_sheet(output_path, recursive, df):
        try:
            out_file = Path(output_path) #Output 
            if not results:
                messagebox.showerror("No data", message="No folders with photos were found.")
                if not keepopen_var.get():
                    root.destroy()
                    sys.exit()
                return
            if recursive:
                if output_path.exists():
                    overwrite_check = messagebox.askyesno("Overwrite?", message=output_path.as_posix() + " \nalready exists. Overwrite?")
                    if overwrite_check:
                        with pd.ExcelWriter(output_path) as writer:
                            for df, sheet_name in results:
                                df.to_excel(writer, sheet_name=sheet_name, index=False)
                        messagebox.showinfo("Success!", message="Success, outputted at " + output_path.as_posix()) #Tell user where file outputted
                else:
                    with pd.ExcelWriter(output_path) as writer:
                        for df, sheet_name in results:
                            df.to_excel(writer, sheet_name=sheet_name, index=False)
                    messagebox.showinfo("Success!", message="Success, outputted at " + output_path.as_posix()) #Tell user where file outputted
            else:
                if output_path.exists():
                    overwrite_check = messagebox.askyesno("Overwrite?", message=output_path.as_posix() + " \nalready exists. Overwrite?")
                    if overwrite_check:
                        df.to_excel(out_file, sheet_name="Output", index=False) #Make an Excel file for importing
                        messagebox.showinfo("Success!", message="Success, outputted at " + output_path.as_posix()) #Tell user where file outputted
                else:
                    df.to_excel(out_file, sheet_name="Output", index=False) #Make an Excel file for importing
                    messagebox.showinfo("Success!", message="Success, outputted at " + output_path.as_posix()) #Tell user where file outputted
            if not keepopen_var.get():
                if output_path.exists() and keepopen_var.get() == False:
                    messagebox.showinfo("File not overwritten.", message="File not overwritten. Cancelled successfully.") #Tell user where file outputted
                root.destroy() #End program
                sys.exit()
        except Exception as e:
            messagebox.showerror( #If no output path was set, error and close
                "An error occurred.", message="Is another program is using output.xlsx? Error caught: " + str(e))
            if not keepopen_var.get():
                root.destroy() #End program
                sys.exit()

root = tk.Tk() #Tkinter root
frame = tk.Frame(root) #Tkinter frame window
execute_button = tk.Button(frame, command=lambda:check_recursive(directory_path), text="Execute") #Buttons to click
set_directory_button = tk.Button(frame, command=set_dir, text="Set folder with images")
set_output_button = tk.Button(frame, command=set_output, text="Set output folder")
keepopen_var = tk.BooleanVar(value=True)  # default checked
keepopen_checkbox = tk.Checkbutton(frame, text="Keep open?", variable=keepopen_var)
recursive_var = tk.BooleanVar(value=False)  # default unchecked
recursive_checkbox = tk.Checkbutton(frame, text="Scan subfolders", variable=recursive_var)
name_entry = tk.Entry(frame, width=30, foreground="gray")
name_entry.insert(0, "Filename (default output.xlsx)")
name_entry.bind("<FocusIn>", nameFocusIn)
name_entry.bind("<FocusOut>", nameFocusOut)
frame.pack() #Pack frame and buttons in order
set_directory_button.pack()
set_output_button.pack()
name_entry.pack()
recursive_checkbox.pack()
execute_button.pack()
keepopen_checkbox.pack()
root.geometry("200x120") #Set dimensions of window to open
root.mainloop() #Ensure window only closes by user choice