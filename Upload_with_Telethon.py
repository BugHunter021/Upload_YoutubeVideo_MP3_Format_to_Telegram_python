from telethon import TelegramClient
from telethon.sync import TelegramClient


# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = '21348' # Your api_id
api_hash = '64f47180565f69e1eebac574354f902c' # Your api_hash
phone_number = 'session_1' # Your phone number
channel_username = 'kanalsotman'
file_name = '25058.jpg'


client = TelegramClient(phone_number, api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))

async with client:
  await client.send_file(channel_username, file_name, caption="TeeeeeeeeeeeexT")
