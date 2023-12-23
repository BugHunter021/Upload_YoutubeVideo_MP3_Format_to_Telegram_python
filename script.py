#!pip install moviepy
#!pip install pytube
#!pip install eyed3

import requests
import os
from pytube import YouTube
from moviepy.editor import *
import eyed3

# ----- Youtube Download

def YutDownload(link):
    youtubeObject = YouTube(link)
    global titlevideo,authorvideo
    titlevideo = youtubeObject.title
    authorvideo = youtubeObject.author

    print("نام اثر: "+youtubeObject.title + "\n"+"نام کانال: "+youtubeObject.author)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(filename='video.mp4')
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
yt=YutDownload(link)

# ----- Convert to MP3
def mp4_to_mp3(mp4, mp3):
  mp4_without_frames = AudioFileClip(mp4)
  mp4_without_frames.write_audiofile(mp3)
  mp4_without_frames.close()

mp4_to_mp3('video.mp4', "audio.mp3")

# ----- Add metaData into audio file
audiofile = eyed3.load("audio.mp3")
audiofile.tag.artist = authorvideo
audiofile.tag.album = "Free For All Comp LP"
audiofile.tag.album_artist = "Various Artists"
audiofile.tag.title = titlevideo
audiofile.tag.save()

# ----- UPLOAD to Channel
print("Uploading to Channel...")
chat_id = 'Enter_ChannelNameforUpload'
token_bot = 'Enter_TOKEN_BOT'
fileup = 'audio.mp3'

file ={"audio": open(f'{fileup}', 'rb')}
params = {
      'chat_id': chat_id,
      'caption': "نام اثر: " + titlevideo + "\n"+"\n"+"نام کانال: " + authorvideo
  }

res = requests.post("https://api.telegram.org/bot" + token_bot + "/sendAudio?", params=params ,files=file)
#print(res.content)
if (res.status_code == 200):
  print("Upload successfully")
