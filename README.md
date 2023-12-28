### Upload YoutubeVideo (convert to MP3 Format) to Telegram channel by python

Converto video youtube to mp3 and upload to telegram Channle
This script writed by python and uses the 3 way to work :

* Telethon library
* Web request
* Pyrogram library
* 
### Requirements

    Python 3.x

####and install library with this command (Install using pip) :

I writed requirement library at first line of script file like this :

```bash
pip install moviepy
pip install pytube
pip install eyed3
pip install telethon
pip install tgcrypto
pip install pyrogram

```
Code Explanation 

* Initialization:
```python
api_id = '12345' # Your api_id
api_hash = '111111aaaabbbbbcccccccccdddd' # Your api_hash
channel_username = 'ketabbazmp3'
app = Client('my_account', api_id, api_hash)
app.connect()
```

### Usage:

* Setup API Keys: First, obtain your api_id and api_hash from my.telegram.org.
* Configure Script: Open the script and replace api_id and api_hash with your actual API credentials. Set channel_username to the target channel's username for upload MP3 files.
* Run Script: Execute the script. On the first run, you'll need to authenticate with your phone number of telegram profile.

this script contain by 3 block code:

* Get URL of youtube video and download it
* Extract sound of video and convert it to MP3 file.
* Upload MP3 file to telegram channel with methods

### Note

* This script requires a persistent internet connection.
* Ensure sufficient local storage for temporary file downloads.
* Be aware of Telegram's rate limits to avoid being temporarily banned.
* Scripts that work with the Python Library methods can upload files up to 2GB but web request method upload to 50MB.
* You can use colab google for run this scripts. ([https://colab.research.google.com](https://colab.research.google.com)https://colab.research.google.com)
    
