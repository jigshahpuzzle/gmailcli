from __future__ import print_function
import httplib2
import os

from googleapiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import httplib2

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = ['https://mail.google.com/', 
			'https://www.googleapis.com/auth/gmail.modify']
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'


'''
Data structure to store gmail authorization credentials with 
helper methods to handle Oauth2 Flow
'''
class GmailAuth(object):

	'''
	email : user email	
	register : boolean indicating if it is a register
	'''
	def __init__(self, email=None, register=False):
		self.reset(email, register)			

	'''
	Resets credentials when changing email account or sets 
	a new email account
	'''	
	def reset(self, email=None, register=False):
		self.email = email
		if not register and email:
			self.credentials = self.load_credentials(email)
		elif email: 
			self.credentials = self.get_credentials(email)
		if email:
			http = self.credentials.authorize(httplib2.Http())
			self.service = discovery.build('gmail', 'v1', http=http)
		else:
			self.service = None 

	'''
	Called by the 'use' command to store a user's credentials in a global.
	'''
	def load_credentials(self, email_id):
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
	def get_credentials(self, email_id):
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

