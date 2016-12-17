# gmailcli

## Configuration
1. Run 'git clone https://github.com/jigshahpuzzle/gmailcli ~/gmailcli/'
2. Create a client_secret.json file with Google to access their APIs, and store in credentials/ directory.
	- To complete this, follow step 1 here: https://developers.google.com/gmail/api/quickstart/python
    - Make sure that the client_secret file generated is of type 'installed' and not 'web'.
3. Make bash script executable by doing "chmod u+x exec.sh" within the gmailcli/ directory  
4. Install dependencies. Within the gmailcli/ directory, run:
	- 'virtualenv gcli' (run 'pip install virtualenv' first if it is not yet installed)
    - 'source gcli/bin/activate'
    - 'pip install -r requirements.txt'
    - 'deactivate' (optional)

## Executing
. ~/gmailcli/exec.sh

Type 'help' for a list of commands
