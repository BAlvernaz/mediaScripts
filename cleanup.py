#!/usr/bin/python3

import os
import shutil
import time

folder_names = ['tv-sonarr', 'radarr', 'tv-4k', 'movies-4K']
start_location = '/mnt/unionfs/'
oneday = (time.time())- 1 * 86400
def get_files():
  for folder in folder_names:
    current_folder = start_location + folder + '/'
    for root, folders, files, in os.walk(current_folder):
        for folder in folders:
          folder_path = os.path.join(root, folder)
          if oneday >= os.stat(folder_path).st_ctime and os.path.exists(folder_path) and not shutil.rmtree(folder_path):
            print("Deleted {}".format(folder_path))




              


get_files()