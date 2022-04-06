"""
- INGEST DATA:
    - Create directory to unzip files.
    - Save files in folder with files pending of proccesing.
"""

import os,sys
sys.path.insert(1, f'{os.getcwd()}/proyect1/utils')
from zipfile    import ZipFile
from parameters import FOLDER_ORIGIN_FILES, FOLDER_RAW_FILES, FIX_FILE_PATH
from utils_all    import (
                            get_dir,
                            get_date_to_run,
                            file_exist
                        )

def main():
    path_origin    = get_dir(FOLDER_ORIGIN_FILES)
    path_final     = get_dir(FOLDER_RAW_FILES)
    date_to_run    = get_date_to_run()
    filename       = path_origin + date_to_run + FIX_FILE_PATH + '.zip' #File .zip

    if os.path.exists(filename):
        if not file_exist(path_final, date_to_run):
           with ZipFile(filename,'r') as zipObj:
            # Extract all the contents of zip file in different directory
            zipObj.extractall(path_final) 
        else:
            print(f'Date {date_to_run} was already processed. Not actions taken.')
    else:
        print(f'File {filename} does not exists...')

if __name__ == '__main__':
    main()
