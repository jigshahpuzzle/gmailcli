from googleapiclient import errors
from prettytable import PrettyTable

'''
Given a service (and potentially a query), returns the next 10
threads in the user's account.
'''
def ListThreadsMatchingQuery(service, user_id, ptoken, query=''):

  try:
    if ptoken:
        response = service.users().threads().list(userId=user_id, q=query, maxResults=10, pageToken=ptoken).execute()
    else:
        response = service.users().threads().list(userId=user_id, q=query, maxResults=10).execute()
    return response
  except errors.HttpError, error:
    print 'An error occurred: %s' % error

'''
Reterive the data found in a thread
'''
def GetThread(service, user_id, thread_id):

  try:
    thread = service.users().threads().get(userId=user_id, id=thread_id).execute()
    return thread
  except errors.HttpError, error:
    print 'An error occurred: %s' % error


'''
Print the top 10 threads for a user, and return the token necessary to get to 
the next page.
'''
def PrintThreads(service, user_id, ptoken, tnum):
	threads = ListThreadsMatchingQuery(service, user_id, ptoken)
	view = PrettyTable(['#', 'Sender', 'Subject'])
	view.align = "l"
	for thread in threads['threads']:
		t = GetThread(service, user_id, thread['id'])
		labels = t['messages'][0]['labelIds']
		subject = filter(lambda x : x['name'] == 'Subject',t['messages'][0]['payload']['headers'])[0]['value']
		sender = filter(lambda x : x['name'] == 'From' ,t['messages'][0]['payload']['headers'])[0]['value'].split('<')[0]
		if 'UNREAD' in labels:
			sender = color.PURPLE + sender + color.END
			subject = color.PURPLE + subject + color.END
		view.add_row([tnum, sender, subject])
		tnum += 1
	print view
	return threads['nextPageToken']
	

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
	
