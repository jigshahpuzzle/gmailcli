from authorize import GmailAuth
from inbox import Inbox

'''
Executable script run in main method
'''
def executable():
	cli = CLI()
	cli.prompt()


'''
Wrapper to store common CLI functions
'''
class CLI(object):

	def __init__(self): 
		self.loop = True
		f = open("credentials/registration.txt")
		data = f.read()
		f.close()
		email = data.split("\n")[0]
		self.user = UserData(email)
		self.fmap = {
			'exit' : self.exit,
			'register' : self.register,
			'help' : self.help,
			'use' : self.use,    
			'inbox' : self.inbox,          
		}
	
	'''
	Script that generates a CLI to work with gmail
	'''
	def prompt(self): 
		print "Welcome to GMail on terminal"
		print "Type 'help' to view a list of commands"
		while self.loop: 
			userinp = raw_input("-- > ")
			f = self.extractCommand(userinp)
			if f:
				f(userinp)


	'''
	Matches passed in user input with the function pointer to a command
	'''
	def extractCommand(self, userinp):
		commandList = ['exit', 'register', 'inbox', 'sent', 'create', 'help', 'use'] 
		for cmd in commandList: 
			if cmd in userinp: 
				return self.fmap[cmd]
		return None

	'''
	Exits the CLI
	'''
	def exit(self, userinp): 
		 self.loop = False
		
	'''
	Authorizes and saves a new gmail account for the user
	'''
	def register(self, userinp): 
		email = userinp.split('register ')[1]
		self.user.reset(email, True)

	'''
	Loads a user's credentials into the global state
	'''
	def use(self, userinp):
		email = userinp.split('use ')[1]
		self.user.reset(email)	
		print "Using account %s" % email

	def inbox(self, userinp):
		params = userinp.split('inbox ')
		if len(params) > 1: 
			if params[1] == 'n':
				self.user.inbox.nextPage()	
			if params[1] == 'p': 
				self.user.inbox.prevPage()
		self.user.inbox.PrintThreads(self.user.gauth.service) 

	'''
	Prints out a help menu for the user
	'''
	def help(self, userinp): 
		print "List of Commands:"
		print "1. exit (quit the CLI)"
		print "2. register <gmail address> (register a new gmail account with the system)"
		print "3. use <gmail address> (load authentication for a registered email address)"
		print "4. inbox (load a view with N email threads starting from last indexed point)"
		print "5. inbox n (advance indexed point by N threads, and then show view)"
		print "6. inbox p (retreat indexed point by N threads, and then show view)"



'''
Stores the current email account's data and has helper 
functions to modify this data. 
'''
class UserData(object):

	'''
	Initialize basic user data to base condition
	'''
	def __init__(self, email): 
		self.email = email
		self.gauth = GmailAuth(email)
		self.inbox = Inbox()	

	'''
	Initialize a user with passed in email, overwriting previous user
	'''
	def reset(self, email, register=False):
		self.email = email	
		self.gauth.reset(email, register)
		self.inbox.reset()

if __name__ == "__main__":
	executable()
