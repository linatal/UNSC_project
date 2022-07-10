import os
import re
import argparse
import sys
import shutil
from pathlib import Path

def list_full_paths(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory)]

def split_paragraphs(input_f, base_f, path_f):
    with open(input_f) as f:
        read_f = f.read()
        read_splt = read_f.split('\n\n')
        count = 0
        for p in read_splt:
            splt_file = str(path_f) + "/" + str(base_f) + "_" +'{:02d}'.format(count) + ".txt"
            count +=1
            with open(splt_file, "w") as open_splt_f:
                open_splt_f.write(p)

if __name__ == "__main__":   
    parser = argparse.ArgumentParser(description="input path")
    parser.add_argument('--input', type=str, help='the path to input file')
    args = parser.parse_args()
    if os.path.isdir(args.input):
        print('The path specified is a directory, the following files got processed:')
        input_dir = os.path.abspath(args.input)
        for f in list_full_paths(input_dir):
            if os.path.basename(f).endswith(".txt") and os.path.basename(f).startswith("UNSC"):
                print(f)
                input_f = f
                base_f = Path(f).stem
                path_f = Path(f).parent
                split_paragraphs(input_f, base_f, path_f)
    elif os.path.isfile(args.input):
        input_f = os.path.abspath(args.input)
        base_f = Path(args.input).stem
        path_f = Path(input_f).parent
        split_paragraphs(input_f, base_f, path_f)

    else:
        print('The path specified does not exist')
        sys.exit()


