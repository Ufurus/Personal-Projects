import tkinter as tk; from buttons import mp4_downloader, mp3_downloader


def downloader_app():
    root = tk.Tk(
        screenName="Video downloader",
        baseName="Video downloader",
        className="Video downloader",
        useTk=bool(1.0)
    )
    root.geometry("800x700")
    root.title('Downloader')
    root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
    return root

def text_display():
    information_display = tk.Label(app, text = "Please enter link below to download", font = ("Helvetica", 12))
    information_display.pack()
    return

def link_input():
    entered_input = tk.Entry(app, width = 70)
    entered_input.pack()
    return entered_input

def chosen_file_type():
    mp4_button = tk.Button(app, text='MP4', command=mp4_downloader(), font=("Arial", 12))
    mp4_button.pack()
    mp3_button = tk.Button(app, text='MP3', command=mp3_downloader(), font=("Arial", 12))
    mp3_button.pack()
    return mp4_button, mp3_button

def download_button():
    download = tk.Button(app, text='Download', font=("Arial", 12), background="Blue", foreground="white")
    download.pack()
    return download

app = downloader_app()
