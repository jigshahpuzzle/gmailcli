from googleapiclient import errors
from prettytable import PrettyTable

MAX_RESULTS = 10

'''
Created by prompt to manage the view created by 
the inbox command.
'''
class Inbox(object): 

	'''
	Same as reset
	'''
	def __init__(self): 
		self.reset()

	'''
	Set all variables to their base (initial) condition
	'''
	def reset(self): 
		self.ptokens = [None]
		self.tnum = 0

	'''
	Given a service (and potentially a query), returns the next 10
	threads in the user's account.
	'''
	def ListThreadsMatchingQuery(self, service, user_id='me'):
		index = self.tnum / MAX_RESULTS
		ptoken = self.ptokens[index]
		try:
			if ptoken:
				response = service.users().threads().list(userId=user_id, maxResults=MAX_RESULTS, pageToken=ptoken).execute()
			else:
				response = service.users().threads().list(userId=user_id, maxResults=MAX_RESULTS).execute()
			return response
		except errors.HttpError, error:
			print 'An error occurred: %s' % error

	'''
	Reterive the data found in a thread
	'''
	def GetThread(self, service, user_id, thread_id):
		try:
			thread = service.users().threads().get(userId=user_id, id=thread_id).execute()
			return thread
		except errors.HttpError, error:
			print 'An error occurred: %s' % error


	'''
	Print the top n threads for a user, and return the token necessary to get to 
	the next page.
	'''
	def PrintThreads(self, service, user_id='me'):
		threads = self.ListThreadsMatchingQuery(service, user_id)
		view = PrettyTable(['#', 'Sender', 'Subject'])
		view.align = "l"
		tnum = self.tnum
		for thread in threads['threads']:
			t = self.GetThread(service, user_id, thread['id'])
			labels = t['messages'][0]['labelIds']
			filtered = filter(lambda x : x['name'] == 'Subject' or x['name'] == 'From',t['messages'][0]['payload']['headers'])
			subject = filter(lambda x : x['name'] == 'Subject', filtered)[0]['value']
			sender = filter(lambda x : x['name'] == 'From', filtered)[0]['value']
			if 'UNREAD' in labels:
				sender = color.PURPLE + sender + color.END
				subject = color.PURPLE + subject + color.END
			view.add_row([tnum, sender, subject])
			tnum += 1
		print view
		self.ptokens.append(threads['nextPageToken'])

	'''
	Advances inbox to the next set of results
	'''
	def nextPage(self):
		self.tnum += MAX_RESULTS

	'''
	Retreats inbox to the previous set of results
	'''
	def prevPage(self): 
		self.tnum -= MAX_RESULTS
	

'''
Helper class to assist with assigning colors while printing
'''
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
	
