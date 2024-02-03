from boxsdk import OAuth2, Client
from dotenv import load_dotenv
import os
load_dotenv()

BOX_CLIENT_ID = os.getenv('BOX_CLIENT_ID')
BOX_CLIENT_SECRET = os.getenv('BOX_CLIENT_SECRET')
BOX_ACCESS_TOKEN = os.getenv('BOX_ACCESS_TOKEN')

auth = OAuth2(
    client_id=BOX_CLIENT_ID,
    client_secret=BOX_CLIENT_SECRET,
    access_token=BOX_ACCESS_TOKEN,
)
client = Client(auth)

user = client.user().get()
print(f'The current user ID is {user.id}')

#upload a new file
new_file = client.folder(0).upload('test2.txt')
print(f'File "{new_file.name}" uploaded to Box with file ID {new_file.id}')

# #update an already exsiting file

#to get the file id, open the file in box, and the number at the end of the url is the file id. 
# file_id = '1415834084903'
# file_info = client.file(file_id).get()
# print(f'File "{file_info.name}" has a size of {file_info.size} bytes')
# updated_file = client.file(file_id).update_contents(file_path="test.txt", file_name="test.txt")
# print(f'File "{updated_file.name}" has been updated')