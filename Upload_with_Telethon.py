#!pip install moviepy
#!pip install pytube
#!pip install eyed3
#!pip install telethon

import requests
import os
from pytube import YouTube
from moviepy.editor import *
import eyed3
from telethon import TelegramClient
from telethon.sync import TelegramClient

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
file_name = "".join(i for i in titlevideo if i not in "\/:*?<>|") + '.mp3'

# ----- Convert to MP3

def mp4_to_mp3(mp4, mp3):
  mp4_without_frames = AudioFileClip(mp4)
  mp4_without_frames.write_audiofile(mp3)
  mp4_without_frames.close()

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

api_id = '21348' # Your api_id
api_hash = '' # Your api_hash
phone_number = 'session_1' # Your phone number
channel_username = 'ketabbazmp3'
#file_name = titlevideo+'.mp3'
caption = "نام اثر: " + titlevideo + "\n"+"\n"+"نام کانال یوتیوب: " + authorvideo + "\n"+"\n"+"@ketabbazmp3"

client = TelegramClient(phone_number, api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))

async with client:
  await client.send_file(channel_username, file_name, caption = caption, video_note=True)
  print("Upload successfully")

if os.path.exists(file_name):
  os.remove(file_name)
  os.remove('video.mp4')
  print("Temp file deleted")
