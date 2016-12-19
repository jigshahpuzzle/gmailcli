from __future__ import print_function
import httplib2
import os

from googleapiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
			'https://mail.google.com/', 
			'https://www.googleapis.com/auth/gmail.modify', 
			'https://www.googleapis.com/auth/gmail.metadata']
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'


'''
Called by the 'use' command to store a user's credentials in a global.
'''
def load_credentials(email_id):
    home_dir = os.getcwd()
    credential_dir = os.path.join(home_dir, 'credentials/')
    f = open(os.path.join(credential_dir, 'registration.txt'))
    data = f.read()
    f.close()
    if email_id in data:	
        credential_path = os.path.join(credential_dir, email_id + '.json')
        store = Storage(credential_path)
        credentials = store.get()
        return credentials	
    else: 
        print ("Failure to load credentials. Try registering the emaild_id first.")


'''
Called by the "register" command to register a new user.
'''
def get_credentials(email_id):
    home_dir = os.getcwd()
    credential_dir = os.path.join(home_dir, 'credentials/')
    credential_path = os.path.join(credential_dir, email_id + '.json')
    flow = client.flow_from_clientsecrets(os.path.join(credential_dir, CLIENT_SECRET_FILE), SCOPES)
    flow.user_agent = APPLICATION_NAME
    store = Storage(credential_path)
    if flags:
        credentials = tools.run_flow(flow, store, flags)
    else: # Needed only for compatibility with Python 2.6
          credentials = tools.run(flow, store)
    print('Storing credentials to ' + credential_path)
    f = open("credentials/registration.txt", "a")
    f.write(email_id + "\n")
    f.close()
	  
    return credentials

