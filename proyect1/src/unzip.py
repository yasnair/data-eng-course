from datetime import date
from zipfile import ZipFile
import utils, os

#dir lake
variables = utils.get_common_var()
date_to_run = variables['date_to_run']
filename = f'{date_to_run}-citibike-tripdata.zip'
filepath = os.path.join(variables['dir_originfiles'] , filename)

try:

    with ZipFile(filepath, 'r') as zipObj:
        # Extract all the contents of zip file in different directory
        zipObj.extractall(variables['dir_processedfiles'])
    print(f'File {filename} created.')
except:
    print(f'ERROR: {filepath} could not processed')
