"""
- INGEST DATA:
    - Create directory to save donwloaded files 
    - Donwload the file based on the date in argv[1] list or actual date if no value is set.
"""
import wget
import os, sys
sys.path.insert(1, f'{os.getcwd()}/proyect1/utils')
from parameters import FOLDER_ORIGIN_FILES, URL_BASE, FIX_FILE_PATH
from utils_all import (
    get_dir,
    get_date_to_run
)

def main():
    path            = get_dir(FOLDER_ORIGIN_FILES)
    date_to_run     = get_date_to_run()
    url             = URL_BASE + date_to_run + FIX_FILE_PATH + '.zip'
    filename        = path + os.path.basename(url)

    try:
        if os.path.exists(filename):
            print(f'File {filename} already exist....')
        else:
            wget.download(url, out=path)  
    except:
        print(f'ERROR 404: {url} could not be open.')


if __name__ == '__main__':
    main()