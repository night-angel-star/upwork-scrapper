
from settings import *
import os
import shutil


def openChromeBrowser(port):
    profile_path = os.path.join(os.getcwd(), "chrome_profile", str(port))
    shutil.rmtree(profile_path, ignore_errors=True)
    command = 'start /B chrome.exe --incognito -remote-debugging-port=' + \
        str(port)+' --user-data-dir="'+profile_path+'"'
    os.system(command)
