from engine import Xyrox
from google_config import Gemini
from processes import execute
from checker.info import execution_info, risk_info
from checker.risk_checker import check_risk
from dotenv import load_dotenv
import os
import platform
# load the environment variables
load_dotenv()
os_type = platform.system()
engine = Xyrox()
# welcoming speech
# engine.make_speech('Welcome to Gen-X, I\'m your Gemini shell executor')

# Risky commands and chars
unsafe_commands = ['rm', 'cp', 'mv', 'chmod', 'chown', 'ssh', 'telnet', 'rm -rf']
risky_characters = ['r', 'm', 'c', 'p', 'm', 'v', ' ', 'd', 'a', 'e', 'l', 'e', 't', 'n', '-']

def main():
    """ Entry point of the program
    """
    while True:

        # Listine to command
        command = engine.listen_to_speech()
        # any(char in risky_characters for char in gen_x
        #checks if command is available
        if command:
            # Gen-X process command
            gen_x = Gemini(mode='gen', text=f'Generate a strictly {os_type} shell for this command "{command}" with no other word only the command, and make sure it\'s securitywise. let the command start with ":>>".', google_api_key=os.getenv(key='GOOGLE_API_KEY'))
            # print(gen_x)

            if gen_x.startswith(':>>'):
                # remove :.. from gen_x
                gen_x = gen_x[3:]
            print(gen_x) 

            if gen_x in unsafe_commands:
                # if command is potentialy risky a beep sound is made!
                speech = check_risk()

                print(f'Does speech start with lower: {speech}')

                if speech.startswith('yes'):
                    # if the speech start with yes then the command execution is continued
                    result = execute(gen_x)
                    # Gen-X make result speech
                    execution_info(result)

                elif speech.startswith('no'):
                    # if the speech start with no then the command execution is discontinued
                    execution_info('Executon discontinued')
                    # break
                    pass

                else:
                    # when no answer is corelating with yes or no then 
                    risks = Gemini(mode='gen', text=f'Tell me the risk of executing {gen_x} in one or two sentence only.', google_api_key=os.getenv(key='GOOGLE_API_KEY'))
                    risk_info(risks)
                    # break from loop to listening again for command    
                    pass
            else:

                result = execute(gen_x)
                # Gen-X make result speech
                execution_info(result)

        else:
            print('Command not available')
            pass
if __name__ == "__main__":
    main()