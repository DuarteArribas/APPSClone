#!/usr/bin/env python3

from gdgps_apps.apps import APPS
from gdgps_apps import defines
import os, sys
import time
from pprint import pprint

#
# Retrieve arguments
#
if (sys.argv[1] == "-i"):
    input = sys.argv[2]
    head, tail = os.path.split(input)
    filename = tail
else:
    logger.error('----- ERROR ('+str(input)+') ----- ERRNO 1')
    print('false1')
    exit()

if(sys.argv[3] == "-d" and os.path.isdir(sys.argv[4]) == True):
    output = sys.argv[4]
else:
    logger.error('----- ERROR ('+input+') ----- ERRNO 2')
    print('false2')
    exit()

#
# Read Configuration file
#
apps = APPS(settings_file="/var/www/html/MiraSeries/upload/apps_settings", download_directory=output, log_level=None) #Onde esta o file de settings
print('Uploading %s...' %input)
uploaded_file = apps.upload_gipsyx(input)['id']
pause = 30
i = 0
time.sleep(pause)

while i < 20:
    # Get latest status of uploaded file
    apps.list_data()
    info = apps.detail(uploaded_file)

    if info['state'] == defines.Data.AVAILABLE:

        path = apps.download_result(info['id'], dr=output)
        apps.delete_data(info['id'])

        #if path.find(' '):
        #    os.rename(path, path.split(' ')[0] + path.split(' ')[1][3:])

        #    path = path.split(' ')[0] + path.split(' ')[1][3:]

        print(path)
        exit()

    elif info['state'] == defines.Data.ERROR:

        apps.delete_data(info['id'])
        print('false e')
        exit()

    elif info['state'] == defines.Data.VERIFIED:

        apps.approve(info['id'])
    time.sleep(pause)  # pause for 30 seconds so we don't overwhelm |APPS|
    i = i + 1

print('false3')
exit()
