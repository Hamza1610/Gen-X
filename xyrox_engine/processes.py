import subprocess

def execute(args):

    """Execute shell command

        args(list or string): 
    """
    if isinstance(args, str):
        
        try:
            output = subprocess.run(args, shell=True, check=True)
            print(output)
            return 'Command executed successfully'
        except:
            return 'Error occured while executing command!'

    elif isinstance(args, list):

        for item in args:
            try:
                output = subprocess.run(item, shell=True, check=True)
                print(output)
                return 'Command executed successfully'
            except:
                return 'Error occured while executing command!'
    else:
       raise TypeError(args)