from authorize import get_credentials, load_credentials


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
		self.fmap = {
			'exit' : self.exit,
			'register' : self.register,
			'help' : self.help,
			'use' : self.use,              
		}

	
	'''
	Script that generates a CLI to work with gmail
	'''
	def prompt(self): 
		print "Welcome to GMail on terminal"
		print "Type 'mm' to view a list of commands"
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
		userinp = userinp.split('register ')[1]
		self.credentials = get_credentials(userinp)

	
	def use(self, userinp):
		userinp = userinp.split('use ')[1]
		self.credentials = load_credentials(userinp)
		print "Using account %s" % userinp

	'''
	Prints out a help menu for the user
	'''
	def help(self, userinp): 
		print "List of Commands:"
		print "1. exit (quit the CLI)"
		print "2. register <gmail address> (register a new gmail account with the system)"
		print "3. use <gmail address> (load information for a registered email address)"

if __name__ == "__main__":
	executable()
