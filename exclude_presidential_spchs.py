import os
import re
import argparse
import sys
import shutil

def create_directories(working_dir):
    lst= []
    preproc_path = working_dir + "selected_spch/" 
    irrel_path = working_dir + "excluded_spch/" 
    lst.extend([preproc_path, irrel_path])
    for p in lst: 
        try:
            os.mkdir(p)
        except OSError:
            print ("Creation of the directory %s failed (potentially already exists)" % p)
        else:
            print ("Successfully created the directory %s " % p)
    return preproc_path, irrel_path




def exclude_irrelevant_text(working_dir, dir_excluded, dir_preproc):
    speaker_f = {}
    # exclude all files with the President - they only serve to greet or thank the participants, structure the debate, etc.

    for f in os.listdir(working_dir):
        if f.endswith(".txt") and f.startswith("UNSC"):
            # copy original files into preprocessed_spch
            shutil.copy(working_dir+str(f), dir_preproc+str(f))
            with open(dir_preproc+str(f), 'r+') as opened_f:
                read_f = opened_f.read()
                # move president's moderation to excluded_spch folder
                if read_f.startswith("The President"):
                    os.rename(dir_preproc+str(f), dir_excluded+str(f))

                pattern_until_colon = "^(.*)(?=:)"
                speaker_name = re.findall(pattern_until_colon, read_f)
                
                try:
                    speaker_f[os.path.basename(f)] = speaker_name[0]
                except: 
                    pass
    return speaker_f



if __name__ == "__main__":   
    parser = argparse.ArgumentParser(description="input and output directory")
    parser.add_argument('--input', metavar='path', type=str, help='the path to the input directory')
    # Execute the parse_args() method
    args = parser.parse_args()

    if not os.path.isdir(args.input):
        print('The path specified does not exist')
        sys.exit()
    
    #print('\n'.join(os.listdir(args.input))) # ls
    working_dir = os.path.join(args.input, '')

    dir_preproc, dir_excluded = create_directories(working_dir)

    #find speaker name and write into dict
    speaker_f = exclude_irrelevant_text(working_dir, dir_excluded, dir_preproc)    
    with open(working_dir+"speaker_dict.txt", "w") as f_dict:
            f_dict.write(str(speaker_f)+'\n')
    

