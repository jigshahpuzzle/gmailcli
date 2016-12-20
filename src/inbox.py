from googleapiclient import errors
from dashtable import data2md

'''
Given a service (and potentially a query), returns the top 10
threads in the user's account.
'''
def ListThreadsMatchingQuery(service, user_id, ptoken, query=''):

  try:
    if ptoken:
        response = service.users().threads().list(userId=user_id, q=query, maxResults=10, pageToken=ptoken).execute()
    else:
        response = service.users().threads().list(userId=user_id, q=query, maxResults=10).execute()
    threads = []
    if 'threads' in response:
      threads.extend(response['threads'])
    return threads
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
def PrintThreads(service, user_id, ptoken):
	threads = ListThreadsMatchingQuery(service, user_id, ptoken)
	view = [['Sender', 'Subject']]
	for thread in threads:
		t = GetThread(service, user_id, thread['id'])
		subject = filter(lambda x : x['name'] == 'Subject',t['messages'][0]['payload']['headers'])[0]['value']
		sender = filter(lambda x : x['name'] == 'From' ,t['messages'][0]['payload']['headers'])[0]['value']
		view.append([sender, subject])
	print data2md(view) 	
