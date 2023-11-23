import random
import openChromeBrowser
import checkChromeDebugPort
import bomb
from settings import *
import time
import json

with open('staticPersonInfo.json') as file:
    # Load the JSON data
    global staticPersonInfo
    staticPersonInfo = json.load(file)

print(staticPersonInfo)


def __main__():
    for i, personInfo in enumerate(staticPersonInfo):
        print(f"Processing {i+1}/{len(staticPersonInfo)}")
        port = random.randint(9001, 9499)
        while checkChromeDebugPort.checkChromeDebugPort(port):
            port = random.randint(9001, 9499)
        openChromeBrowser.openChromeBrowser(port)
        time.sleep(3)
        result = checkChromeDebugPort.checkChromeDebugPort(port)
        if result:
            print(f"Chrome is opened on the port {port}")
            bomb.main(port, personInfo)
            continue
        else:
            i = i-1
            continue

    time.sleep(999999)


__main__()
