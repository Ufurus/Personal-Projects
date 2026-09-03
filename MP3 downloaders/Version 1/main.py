# First iteration of MP3 downloader. Using moviePy lib to edit
# m4a files to mp3.

# It downloads them to personally created directory called /tmp
# after download, it converts the file and move it to another directory
# called mp3 downloads on desktop. Also, it should be setup with a GUI in future versions.

# As it is first iteration, next iteration will fix the issue with directories
# to be more universal, rather being so personal.

import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from moviepy import AudioFileClip

temporary_directory = r'C:\Users\Потребител\Desktop\tmp' # where it will download and convert files temporary
target_directory = r'C:/Users/Потребител/Desktop/MP3 downloads' # target directory where MP3 files will go

def transform_from_m4a_to_mp3(curr_directory):
    """"Function to convert m4a file to mp3"""
    for filename in os.listdir(curr_directory):
        if filename == yt.title + '.m4a':
            file_location = os.path.join(curr_directory, filename)
            mp4_file = (filename.split('.m4a')[0]) + '.mp3'
            final_file_location = os.path.join(target_directory, mp4_file)
            audio_file_m4a = AudioFileClip(file_location)
            audio_file_m4a.write_audiofile(final_file_location)
            os.remove(file_location)
            break

while True:

    url = input('Enter URL: ')
    if url.startswith("http") or url.startswith("https"):
        if "youtube.com" in url:
            break
    print('Please enter a valid URL')

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_audio_only()
ys.download(temporary_directory)
transform_from_m4a_to_mp3(temporary_directory)