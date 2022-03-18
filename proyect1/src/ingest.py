import wget
import requests
import utils 

variables = utils.get_common_var()
date_to_run = variables['date_to_run']

url = f'https://s3.amazonaws.com/tripdata/{date_to_run}-citibike-tripdata.zip'
try:
    #to get the current working directory
    wget.download(url, out=variables['dir_originfiles'])
except requests.HTTPError as err:
    if err.code == 404:
        print(f'File {date_to_run}-citibike-tripdata.zip does not exits')
    else:
        raise


