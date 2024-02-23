import os
import glob
import sys
import shutil

def get_pdf(source_path):
    files = []
    unique_files = set(glob.glob(os.path.join(source_path, '*.pdf')))
    for pfile in unique_files:
        files.append(pfile)
    return files

def copy_(files, destination_path):
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    for pfile in files:
        file_name = os.path.basename(pfile)
        destination_file_path = os.path.join(destination_path, file_name)
        if not os.path.exists(destination_file_path):
            shutil.copy(pfile, destination_path)

source_path = sys.argv[1]

try:
    if not os.path.exists(source_path):
        raise FileNotFoundError("the given path is not there")
    destination_path=sys.argv[2]


    files = get_pdf(source_path)
    copy_(files, destination_path)


    for pfile in files:
        print(pfile)

except FileNotFoundError as error_m:
    print(error_m)





