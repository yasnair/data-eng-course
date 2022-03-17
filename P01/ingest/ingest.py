from ctypes import util
import wget
from decouple import config

from urllib.parse import urlparse
import requests
import utils 


#Set directory to donwload files.
dir_originfiles    = utils.get_dir('lake/origin_files/')
 #get date to pull
date_to_run = utils.get_date_to_run()

url = f'https://s3.amazonaws.com/tripdata/{date_to_run}-citibike-tripdata.zip'
try:
    #to get the current working directory
    wget.download(url, out=dir_originfiles)
except requests.HTTPError as err:
    if err.code == 404:
        print(f'File {date_to_run}-citibike-tripdata.zip does not exits')
    else:
        raise


