from boxsdk import OAuth2, Client

auth = OAuth2(
    client_id='6mtnzxmqvhjfimcjpd3acn3pdrfjmguk',
    client_secret='1GarmMkUPefszWDehCBGEvWsRZDTH5gF',
    access_token='CSAzAlAOI2Io5unaH7jOBHo4bBvGUg9e',
)
client = Client(auth)

user = client.user().get()
print(f'The current user ID is {user.id}')

#to get the file id, open the file in box, and the number at the end of the url is the file id. 
file_id = '1415834084903'
# file_info = client.file(file_id).get()
# print(f'File "{file_info.name}" has a size of {file_info.size} bytes')

#upload a new file
# new_file = client.folder(0).upload('test.txt')
# print(f'File "{new_file.name}" uploaded to Box with file ID {new_file.id}')

#update an already exsiting file
updated_file = client.file(file_id).update_contents(file_path="test/test.txt", file_name="test.txt")
print(f'File "{updated_file.name}" has been updated')