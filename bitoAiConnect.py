import subprocess
from settings import *
import re
import json
import random
import time


def is_string_contained(main_string, sub_string):
    pattern = sub_string+r"\d+"
    matches = re.finditer(pattern, main_string)
    matched_strings = [match.group() for match in matches]
    if len(matched_strings) > 0:
        return True
    else:
        return False


def resultParser(ai_result):
    try:
        ai_result = ai_result.replace('\n', '')
        match = re.search(r"\[.*?\]", ai_result)

        if (match):
            ai_result = match.group()
            ai_result = json.loads(ai_result)
            random_index = random.randint(0, len(ai_result)-1)
            return ai_result[random_index]
        else:
            return ""
    except:
        return ""


def generateName(country):
    while True:
        command = f'echo "generate {random_amount} men full name in {
            country} with only english character. prompt in array format" | bito'
        try:
            result = subprocess.run(command, shell=True,
                                    capture_output=True, text=True)
        except:
            time.sleep(1)
            continue
        if result.returncode == 0:
            # Print the output
            ai_result = result.stdout
            ai_result = resultParser(ai_result)
            if ai_result != "":
                name_array = ai_result.split(" ")
                first_name = name_array[0]
                last_name = name_array[-1]
                return {"firstName": first_name, "lastName": last_name}
            else:
                time.sleep(1)
                continue
        else:
            time.sleep(1)
            continue


def generateUniversityName(country):
    while True:
        command = f'echo "generate {random_amount} university where educates computer science and gives bachelor degree in {
            country}. prompt in array format. like this. [aaa,bbb]" | bito'
        try:
            result = subprocess.run(command, shell=True,
                                    capture_output=True, text=True)
        except:
            time.sleep(1)
            continue

        if result.returncode == 0:
            # Print the output
            ai_result = result.stdout
            ai_result = resultParser(ai_result)
            if ai_result != "":
                return ai_result
            else:
                time.sleep(1)
                continue
        else:
            time.sleep(1)
            continue


def generateOverview(title):
    while True:
        command = f'echo "generate 10 {
            title} overview. prompt all overviews in one array format" | bito'
        try:
            result = subprocess.run(command, shell=True,
                                    capture_output=True, text=True)
        except:
            time.sleep(1)
            continue

        if result.returncode == 0:
            # Print the output
            ai_result = result.stdout
            ai_result = resultParser(ai_result)
            if len(ai_result) < 100:
                time.sleep(1)
                continue
            if ai_result != "":
                return ai_result
            else:
                time.sleep(1)
                continue
        else:
            time.sleep(1)
            continue


def generateLocationInfo(country):
    while True:
        command = "echo `generate 10 ISO type birthday between 1990 and 1995, address with street, city in "+country + \
            " and random eight digit number in object array format. not ommit. write all. like this.  {['birthday':'1990-00-00','street':'abc', 'city':'abc', 'number':'12312312'],['birthday':'1990-00-00','street':'def','city':'fge','number':'12312312']}` | bito"
        try:
            result = subprocess.run(command, shell=True,
                                    capture_output=True, text=True)
        except:
            time.sleep(1)
            continue

        if result.returncode == 0:
            # Print the output
            ai_result = result.stdout
            ai_result = resultParser(ai_result)
            if "birthday" in ai_result and "street" in ai_result and "city" in ai_result and "number" in ai_result:
                if is_string_contained(ai_result["street"], "Street"):
                    time.sleep(1)
                    continue
                if is_string_contained(ai_result["city"], "City"):
                    time.sleep(1)
                    continue
                return ai_result
            else:
                time.sleep(1)
                continue

        else:
            time.sleep(1)
            continue
