import os; import subprocess;import tkinter as tk; import tkinter.messagebox; from pathlib import Path

DOWNLOADS_FOLDER = Path.home() / 'Downloads'

# main window
root = tk.Tk(screenName='MP4 downloader',
             baseName='MP4 downloader',
             className='mp4 downloader',
             useTk=1,
             )

#configuring size of the window and where it opens on the monitor, preferable the center of the screen
root.geometry("700x500")
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

# simple label for name of the application
title_label = tk.Label(root, text='enter link below to download it', font=('consolas', 15))
title_label.pack()

# input space for the URL
link_input = tk.Entry(root, width=70)
link_input.pack()

def getting_input():
    given_url = link_input.get()
    a = given_url
    def wrong_url():
        tk.messagebox.showinfo("Error", "Please enter a valid URL")
        root.mainloop()
    try:
        if len(given_url) != 43 or 'youtube.com' not in given_url:
            wrong_url()
    finally:
        url = [given_url]

    return url[0]

def download_button():

    subprocess.run(["yt-dlp", "-P", DOWNLOADS_FOLDER, getting_input()])
    file_name = [i for i in os.listdir(DOWNLOADS_FOLDER) if i.endswith(".webm") or i.endswith(".mkv")][0]
    new_name = str(file_name[:file_name.index('[') - 1]) + '.mp4'
    if os.path.exists(DOWNLOADS_FOLDER / new_name):
        os.remove(DOWNLOADS_FOLDER / file_name)
        tkinter.messagebox.showinfo("Error", "File already exists")
    else:
        full_file_path = DOWNLOADS_FOLDER / file_name
        os.rename(full_file_path, DOWNLOADS_FOLDER / new_name)
        tkinter.messagebox.showinfo("Success", "Download successful")

# download button
button = tk.Button(root, text='download', command=download_button)
button.pack()

# this ensures the window starts
root.mainloop()