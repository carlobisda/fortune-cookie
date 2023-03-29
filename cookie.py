
import random
import sys
import os

def select_random(filename):
    if os.path.exists(filename): #CHECKS IF INPUT FILE EXISTS
        with open(filename, 'r') as f:
            titles = f.readlines()
            return random.choice(titles).strip()

    else:
        return "File Not Found."

if __name__ == '__main__':
    if len(sys.argv) > 1: #PASSES COMMAND LINE ARGUMENTS TO THE SCRIPT
        filename = sys.argv[1] #FILENAME VARIABLE
    else:
        filename = 'cookie' #DEFAULT FILE

    print(select_random(filename))