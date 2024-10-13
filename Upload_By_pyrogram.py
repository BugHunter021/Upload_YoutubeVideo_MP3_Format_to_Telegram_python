#!pip install moviepy
#!pip install pytube
#!pip install eyed3
#!pip install telethon
#!pip install tgcrypto
#!pip install pyrogram

import requests
import os
from pytube import YouTube
from moviepy.editor import *
import eyed3
#from telethon import TelegramClient
#from telethon.sync import TelegramClient

from pyrogram import Client
from pyrogram.types import *


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

file_name = "".join(i for i in titlevideo if i not in "\/:*?<>|") + '.mp3'
mp4_to_mp3('video.mp4', file_name)
# ----- Add metaData into audio file
audiofile = eyed3.load(file_name)
audiofile.tag.artist = authorvideo
audiofile.tag.album = "Free For All Comp LP"
audiofile.tag.album_artist = "Various Artists"
audiofile.tag.title = titlevideo
audiofile.tag.save()

# ----- UPLOAD to Channel
print("Uploading to Channel...")

api_id = '12345' # Your api_id
api_hash = '1111111aaaabbbbbccccccdddddd' # Your api_hash
session_name = 'session_1' 
channel_username = 'ketabbazmp3'
#file_name = titlevideo+'.mp3'
caption = "🎤Title: " + titlevideo + "\n"+"\n"+"🎥Youtube Channle: " + authorvideo + "\n"+"\n"+"@"+channel_username

app = Client('my_account', api_id, api_hash)
app.connect()
async with app:
  async def progress(current, total):
    currentnum = current * 100 / total
    sys.stdout.write("\r%d%% uploading ... " % currentnum)
    sys.stdout.flush()
    #print(f"{current * 100 / total:.1f}%")
  await app.send_audio(channel_username, file_name, caption = caption,progress=progress)
  print("\n Upload successfully")

if os.path.exists(file_name):
  os.remove(file_name)
  os.remove('video.mp4')
  print("Temp file deleted")

