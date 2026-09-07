""""
This was the first version of MP3 downloader, but it somehow works now as a MP4. So, this is the
first iteration of MP4 downloaders
"""

import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
import shutil
import ffmpeg
import subprocess

path = r'C:/Users/Потребител/Desktop/MP3 downloads' # main folder for MP3 files
temp_path = r'C:/Users/Потребител/Desktop/tmp' # temporary dir where m4a files are downloaded and ready
# to be converted

def convert_video_to_audio(video_path, audio_path):
    command = 'ffmpeg -i {} -vn -ar 44100 -ac -b: a 192k {}'.format(video_path, audio_path)
    subprocess.call(command, shell=True)

while True:

    url = input("Enter URL: ")
    if 'youtube.com/watch' in url and len(url) == 43:
        break
    print("Please enter a valid youtube link")

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download(temp_path)

for file in os.listdir(temp_path):
    title = file[:-4].split()
    if yt.title.split()[1] == title[1]:
        video_path = os.path.join(temp_path, file)
        audio_path = os.path.join(path, file)
        convert_video_to_audio(video_path, audio_path)
        # shutil.move(os.path.join(temp_path, file), path)