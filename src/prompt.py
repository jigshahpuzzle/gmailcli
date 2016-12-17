from authorize import get_credentials


'''
Wrapper to store common CLI functions
'''
class CLI(object):


	def __init__(self): 
		self.loop = True
		self.fmap = {
			'exit' : self.exit,
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
				f()


	'''
	Matches passed in user input with the function pointer to a command
	'''
	def extractCommand(self, userinp):
		commandList = ['exit', 'register', 'inbox', 'sent', 'create'] 
		for cmd in commandList: 
			if cmd in userinp: 
				return self.fmap[cmd]
		return None

	'''
	Exits the CLI
	'''
	def exit(self): 
		 self.loop = False
		

if __name__ == "__main__":
	cli = CLI()
	cli.prompt()
	
