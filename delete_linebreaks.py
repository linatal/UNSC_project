import os
import re
import argparse
import sys
from pathlib import Path

def list_full_paths(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory)]

def delete_linebreaks(input):
    with open(input, 'r+') as f:
        read_f = f.read()
        # delete everything until first column (speaker name, country)
        substitute = re.sub(r"(.*?: )", "", read_f, count=1)
        # delete unnecessary line breaks
        substitute = re.sub("(?<=[^\.])(\n\n)", " ", substitute)
        substitute = re.sub("(?<=[\w\;\:\,])\n", " ", substitute)
        substitute = re.sub("(?<=[\-])\n", "", substitute)
        # write into files
        f.seek(0)
        f.write(substitute)
        f.truncate()

def check():
    print("The skript will delete the speaker names and line breaks and **overrides** the input file(s).")
    answer = input("Continue? Answer [Y/N]: ")
    if answer.lower() in ["y","yes"]:
        print("Continue.")
    elif answer.lower() in ["n","no"]:
        print("Break because of user input.")
        raise Exception("Input: No")
    else:
        raise Exception("Wrong input, break.")
    return 

if __name__ == "__main__":   
    parser = argparse.ArgumentParser(description="input path")
    parser.add_argument('--input', type=str, help='the path to input file')
    args = parser.parse_args()

    check()
    if os.path.isdir(args.input):
        input_dir = os.path.abspath(args.input)
        print('The path specified is a directory, the following files got processed:')
        for f in list_full_paths(input_dir):
            print(f)
            if os.path.basename(f).endswith(".txt") and os.path.basename(f).startswith("UNSC"):
                delete_linebreaks(f)

    elif os.path.isfile(args.input):
        print('The following file got processed:')
        input_f = os.path.abspath(args.input)
        print(input_f)
        delete_linebreaks(input_f)
    else:
        print('The path specified does not exist. Exit.')
        sys.exit()


