from engine import Xyrox
from google_config import Gemini
from dotenv import load_dotenv
import os
# load the environment variables
load_dotenv()

engine = Xyrox()

# welcoming speech
# engine.make_speech('Welcome to Gen-X, I\'m your Gemini shell executor')

# Listine to command
command = engine.listen_to_speech()

# Risky commands and chars
unsafe_commands = ['rm', 'cp', 'mv', 'chmod', 'chown', 'ssh', 'telnet', 'rm -rf']
risky_characters = ['r', 'm', 'c', 'p', 'm', 'v', ' ', 'd', 'a', 'e', 'l', 'e', 't', 'n', '-']
#checks if command is available
if len(command) >= 1:
    # Gen-X process command
    gen_x = Gemini(mode='gen', text=f'Generate a shell command for this command "{command}" with no other word only the command, and make sure it\'s securitywise. let the command start with ":>>".', google_api_key=os.getenv(key='GOOGLE_API_KEY'))
    # print(gen_x)

    if gen_x.startswith(':>>'):
        gen_x =gen_x[3:]
    print(gen_x) 

    if gen_x in unsafe_commands or any(char in risky_characters for char in gen_x):
        # if command is potentialy risky a beep sound is made!
        print('Command could be potentially risky. Exercise caution and double-check!')

        engine.make_speech()

else:
    print('command length is less that one')
    pass