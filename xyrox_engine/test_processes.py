import subprocess

def execute(args):

    """Execute shell command

        args(list or string): 
    """
    if isinstance(args, str):
        
        output = subprocess.run(args, shell=True, check=True)
        print(output)

    elif isinstance(args, list):

        for item in args:
            output = subprocess.run(item, shell=True, check=True)
            print(output)
    else:
       raise TypeError(args)
if __name__ == '__main__':
    execute(['move Example_folder ../'])