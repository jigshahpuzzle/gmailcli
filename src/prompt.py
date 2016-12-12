from authorize import get_credentials


'''
Script that generates a CLI to work with gmail
'''
def prompt(): 
	print "Welcome to GMail on terminal"
	print "Type 'mm' to view a list of commands"
	while True: 
		userinp = raw_input("-- > ")



'''
Matches passed in user input into a command
'''
def extractCommand(userinp):
	commandList = ['', '', '', '', ''] 


'''

'''
def mm(): 
	pass 

'''
A hashmap that maps strings to function pointers
'''
fMap = {
	'mm' :  mm,
}


