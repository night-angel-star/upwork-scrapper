import requests
from settings import *
import time
import re

baseUrl = "https://www.1secmail.com/api/v1/"


def getEmailAddress():
    while True:
        action = "?action=genRandomMailbox&count=10"
        response = requests.get(baseUrl+action)
        if response.status_code == 200:
            data = response.json()
            email = data[0]
            login, domain = email.split("@")
            if domain in avaliableDomainList:
                print({"login": login, "domain": domain})
                return {"login": login, "domain": domain}
            else:
                continue

        else:
            continue


def getEmailVerifyUri(login, domain):
    emailId = ""
    retryTime = 0
    while True:
        emailListAction = f"?action=getMessages&login={login}&domain={domain}"
        emailListResponse = requests.get(baseUrl+emailListAction)
        if emailListResponse.status_code == 200:
            data = emailListResponse.json()
            foundEmail = False
            for d in data:
                if "upwork" in d["from"] and d["subject"] == "Verify your email address":
                    emailId = d["id"]
                    foundEmail = True
                    break
                else:

                    continue
            if foundEmail:
                break
            else:
                time.sleep(2)
                retryTime += 1
                if retryTime < 5:
                    print("email not found")
                    continue
                else:
                    return ""
        else:
            time.sleep(2)
            print("server not respond")
            continue
    verifyUri = getVerifyUri(login, domain, emailId)
    return verifyUri


def getVerifyUri(login, domain, emailId):
    while True:
        action = f"?action=readMessage&login={
            login}&domain={domain}&id={emailId}"
        response = requests.get(baseUrl+action)
        if response.status_code == 200:
            email = response.json()
            emailBody = email["body"]
            match = re.search(
                r'href="(https://www.upwork.com/nx/signup/verify-email/token/[^"]+)"', emailBody)
            if match:
                extracted_string = match.group(1)
                return extracted_string
            else:
                return ""
            break
        else:
            continue


# emailaddress = getEmailAddress()
# print(emailaddress)
# uri = getEmailVerifyUri("vb69ctv", "laafd.com")
# print(uri)
