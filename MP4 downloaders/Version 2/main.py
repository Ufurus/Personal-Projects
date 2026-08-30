# second version of the mp4.
# this time using yt.dlp instead of pytube/pytubefix as currently they are not working.

import os
import subprocess
from yt_dlp import YoutubeDL
URLS = [
    'https://www.youtube.com/watch?v=k1-TrAvp_xs' ]

with YoutubeDL() as ydl:
    ydl.download([URLS[0]])

file_name = os.listdir(os.getcwd())[1]

subprocess.run(["ffmpeg", '-i', file_name, '-c', 'copy', 'output.mp4'])
os.remove(file_name)

# ffmpeg -i input.mkv -c copy output.mp4 - this converts to mp4 from webm.


