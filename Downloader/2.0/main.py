import tkinter as tk; import tkinter.messagebox as messagebox; from pathlib import Path; import subprocess; import os
# main window
root = tk.Tk(
        screenName="Video downloader",
        baseName="Video downloader",
        className="Video downloader",
)

DOWNLOADS_FOLDER = Path.home() / 'Downloads'
chosen_type = ''

def data_mp4():
    global chosen_type
    chosen_type = 'MP4'
    data_type = tk.Label(root, text=f"Current Data Type: {chosen_type}", font=("Arial", 10))
    data_type.grid(row=4, column=1)

def data_mp3():
    global chosen_type
    chosen_type = 'MP3'
    data_type = tk.Label(root, text=f"Current Data Type: {chosen_type}", font=("Arial", 10))
    data_type.grid(row=4, column=1)

def getting_input():
    given_url = link_input.get()
    if len(given_url) != 43 or 'youtube.com' not in given_url:
        messagebox.showerror("Error", "Please enter a valid URL")
        root.mainloop()
    url = [given_url]
    return url[0]

def download_video():

    if chosen_type != 'MP3' and chosen_type != 'MP4':
        messagebox.showerror("Error", "Please select either MP3 or MP4")
    else:
        subprocess.run(["yt-dlp", "-P", DOWNLOADS_FOLDER, getting_input()])
        with os.scandir(DOWNLOADS_FOLDER) as it:
            file_name = [item.name for item in it if item.name.endswith(".webm") or item.name.endswith(".mkv")][0]
        if chosen_type == 'MP3':
            new_name = str(file_name[:file_name.index('[') - 1]) + '.mp3'
        elif chosen_type == 'MP4':
            new_name = str(file_name[:file_name.index('[') - 1]) + '.mp4'
        if os.path.exists(DOWNLOADS_FOLDER / new_name):
            os.remove(DOWNLOADS_FOLDER / file_name)
            messagebox.showinfo("Error", "File already exists")
        else:
            os.rename(DOWNLOADS_FOLDER / file_name, DOWNLOADS_FOLDER / new_name)
            messagebox.showinfo("Success", "Download successful")
            os.startfile(DOWNLOADS_FOLDER)
# window size, fixed size
root.geometry("350x500+1+1")
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
root.minsize(350,500)
root.maxsize(350,500)

# Label and entry pack for the provided link
title_label = tk.Label(root, text="Please enter link below to download", font=("Arial", 14), foreground='black', width=30)
title_label.grid(row=0, column=1)
link_input = tk.Entry(root, width=50)
link_input.grid(row=1, column=1)

fr = tk.Frame(root)
fr.grid(rowspan=2, column=2)
bottom_frame = tk.Frame(root)
bottom_frame.grid(row=2, column=1)

# data type buttons
mp4_button = tk.Button(bottom_frame, text='MP4', command=data_mp4,font=("Arial", 10), relief='raised')
mp4_button.grid(row=2, column=1)
mp3_button = tk.Button(bottom_frame, text='MP3', command=data_mp3,font=("Arial", 10), relief='raised')
mp3_button.grid(row=2, column=2)

# download button
download_button = tk.Button(root, text="Download", command=download_video, font=("Arial", 10), foreground='white', background='blue')
download_button.grid(row=3, column=1)

data_type = tk.Label(root, text=f"Current Data Type:{chosen_type}", font=("Arial", 10))
data_type.grid(row=4, column=1)

root.mainloop()