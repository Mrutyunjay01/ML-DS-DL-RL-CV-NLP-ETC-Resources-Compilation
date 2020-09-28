# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:34:26 2020

@author: MRUTYUNJAY BISWAL
"""
import os
import tarfile
import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join('datasets', 'housing')
DOWNLOAD_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=DOWNLOAD_URL, housing_path=HOUSING_PATH):
    
    if not os.path.isdir(housing_path):
        # use mkdirs to create nested directories
        os.makedirs(housing_path)
        
    tgz_path = os.path.join(housing_path, 'housing.tgz')
    print('Retriving Data from the URL...')
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    print('EXtracting the tar file...')
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()
    pass

fetch_housing_data()

