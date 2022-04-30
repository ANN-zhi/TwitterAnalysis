#create an auth() function that will have the “Bearer Token” from the app we just created
import os
os.environ['TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAAJtgVgEAAAAAPtAynyI2oywacLvsArIWn3Aof%2Bg%3DqMxIL4seiIqPfcjG2iYaMYe8DDfiCC7SFm0ykASnSSRfwxtMfG'
# For saving access tokens and for file management when creating and adding to the dataset

def auth():
    return os.getenv('TOKEN')

#Create Headers
#define a function that will take our bearer token, pass it for authorization and return headers we will use to access the API.
def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers