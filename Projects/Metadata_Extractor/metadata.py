# Dear programmer:
# When I wrote this code, only God and I knew how it worked.
# Now, only God knows!
# 
# Therefore, if you trying to improve this,
# Please increment this counter as a warning
# For the next person:
# 
# hours_wasted_here = 0

from PIL import Image, UnidentifiedImageError
import os
from pathlib import Path
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

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
def set_dir():
    global directory_path
    directory_path = Path(filedialog.askdirectory(title="Select a Directory"))
#Gets called on set output button press
def set_output():
    global output_path
    output_path = Path(filedialog.askdirectory(title="Select a Output Directory")+"/output.xlsx")
def scan_image(directory_path, files_and_dirs, i, list_of_dates, list_of_images):
    img = Image.open(Path(directory_path) / files_and_dirs[i]) #Open the image in code
    exif_data = img.getexif() #Get the exif metadata
    dt = exif_data.get(306) or exif_data.get(36867) #Only extract date and time
    filename = files_and_dirs[i] #Get filename
    if dt is None:
        raise ValueError(f"No metadata found for {filename}")
    list_of_dates.append(dt) #Add to lists
    list_of_images.append(filename)
#Gets called when irregular pattern is detected
def sort_and_extract_irregular(directory_path):
    with os.scandir(directory_path) as entries:
        file_count = sum(1 for entry in entries if entry.is_file() and entry.name.lower().endswith((photo_types + video_types)))
    if file_count > 0:
        global output_path
        if debug: #No need to set output_path every time
                output_path = Path.home() / "Downloads" / "output.xlsx"
        if directory_path == None or output_path == None:
                messagebox.showerror( #If no output/directory path was set, error to allow for changes
                            "Invalid path(s) specified.", message="Please set an image/video directory path OR output path.")
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
                    if photos_before_video_updated == False and i == 0:
                        sort_and_extract(directory_path)
                    if photos_before_video_updated and regular_pattern_found == False:
                        end = False
                        while pattern_check < photos_before_video:
                            if photos_before_video+i > len(files_and_dirs)-1:
                                regular_pattern_found=True #For scanning last photos/videos
                                end = True
                                break
                            if files_and_dirs[pattern_check+i].lower().endswith((photo_types)):
                                pass
                            pattern_check+=1
                        if not end:
                            if files_and_dirs[i+pattern_check].lower().endswith((video_types)):
                                regular_pattern_found = True
                            else:
                                if not video_first:
                                    img_series.append(str(index)) #Images in a row
                                    scan_image(directory_path, files_and_dirs, i, list_of_dates, list_of_images)
                                else:
                                    img_series.append(str(index-1))
                                    scan_image(directory_path, files_and_dirs, i, list_of_dates, list_of_images)
                        else:
                            for r in range(photos_before_video):
                                if (i+r<len(files_and_dirs)):
                                    scan_image(directory_path, files_and_dirs, i+r, list_of_dates, list_of_images)
                                    img_series.append(str(index+r))
                            messagebox.showerror("Ended in an image", message="Please make sure the last images are cataloged as a set, if they are to be.")

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
        create_sheet(img_series, list_of_images, fixed_date, fixed_time, output_path)
    else:
        messagebox.showerror("Empty directory", message="No files were found. Please select a valid directory")
        return
#Gets called on "Execute" button press 
#Paths supplied by user or debug mode
#Assumes regular pattern
def sort_and_extract(directory_path):
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
            create_sheet(img_series, final_images, final_dates, final_times, output_path)
        

#For regular patterns only
def make_series(list_of_images, photos_before_video_updated, photos_before_video, fixed_date, fixed_time):
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

def create_sheet(img_series, final_images, final_dates, final_times, output_path):
        df = pd.DataFrame( #Create DataFrame
            {
                "Files": final_images,
                "Dates": final_dates,
                "Time": final_times,
                "Image # Series": img_series,
            }
        )

        try:
            out_file = Path(output_path) #Output 
            df.to_excel(out_file, sheet_name="Output", index=False) #Make an Excel file for importing
            messagebox.showinfo(
                "Success!", message="Success, outputted at " + output_path.as_posix() #Tell user where file outputted
            )
            root.destroy() #End program
        except Exception as e:
            messagebox.showerror( #If no output path was set, error and close
                "An error occurred.", message="Is another program is using output.xlsx? Error caught: " + str(e)
            )
            root.destroy()


root = tk.Tk() #Tkinter root
frame = tk.Frame(root) #Tkinter frame window
execute_button = tk.Button(frame, command=lambda:sort_and_extract_irregular(directory_path), text="Execute") #Buttons to click
set_directory_button = tk.Button(frame, command=set_dir, text="Set folder with images")
set_output_button = tk.Button(frame, command=set_output, text="Set output folder")
frame.pack() #Pack frame and buttons in order
set_directory_button.pack()
set_output_button.pack()
execute_button.pack()
root.geometry("200x120") #Set dimensions of window to open
root.mainloop() #Ensure window only closes by user choice