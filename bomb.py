from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import random
import bitoAiConnect
import getEmail
from settings import *


def click(selector):
    element = driver.find_element("css selector", selector)
    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)


def simulateTyping(selector, text):
    click(selector)
    element = driver.find_element("css selector", selector)
    for i in range(len(text)):
        element.send_keys(text[i])
        time.sleep(0.1)


def simulateTypingForDropdown(selector, text):
    element = driver.find_element("css selector", selector)
    click(selector)

    time.sleep(0.5)
    newElement = driver.find_element("css selector", selector)
    for i in range(len(text)):
        newElement.send_keys(text[i])
        time.sleep(0.1)


def selectFromDropdown():
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(1)


def selectLanguage():
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(1)


def selectBirthday():
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(1)


def navigateToUpwork():
    driver.get("https://www.upwork.com")

    while True:
        try:
            acceptCookieButtonSelector = "#onetrust-accept-btn-handler"
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(("css selector", acceptCookieButtonSelector)))
            # acceptCookieButton = driver.find_element(
            #     "css selector", acceptCookieButtonSelector)
            click(acceptCookieButtonSelector)
            break
        except:
            continue


def navigateToSignUpPage():
    signUpButtonSelector = ".up-n-link.air3-btn.air3-btn-primary.mr-0.mb-0.d-none.d-nav-lg-inline-flex.vs-text-default"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", signUpButtonSelector)))
    # signUpButton = driver.find_element(
    #     "css selector", signUpButtonSelector)
    time.sleep(1)
    click(signUpButtonSelector)


def selectRole():
    roleButtonSelector = '[data-qa="work"]'
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", roleButtonSelector)))
    # roleButton = driver.find_element("css selector", roleButtonSelector)
    time.sleep(1)
    click(roleButtonSelector)
    time.sleep(1)
    applyButtonSelector = ".up-btn.up-btn-primary.width-md.up-btn-block"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", applyButtonSelector)))
    # applyButton = driver.find_element(
    #     "css selector", applyButtonSelector)
    time.sleep(0.2)
    click(applyButtonSelector)


def signUpToUpwork():
    global emailInfo
    emailInfo = getEmail.getEmailAddress()
    firstNameInputSelector = "#first-name-input"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", firstNameInputSelector)))
    # firstNameInput = driver.find_element(
    #     "css selector", firstNameInputSelector)
    lastNameInputSelector = "#last-name-input"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", lastNameInputSelector)))
    # lastNameInput = driver.find_element("css selector", lastNameInputSelector)
    emailInputSelector = "#redesigned-input-email"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", emailInputSelector)))
    # emailInput = driver.find_element("css selector", emailInputSelector)
    passwordInputSelector = "#password-input"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", passwordInputSelector)))
    # passwordInput = driver.find_element("css selector", passwordInputSelector)

    checkboxs = driver.find_elements(
        "css selector", ".up-checkbox-replacement-helper")

    submitButtonSelector = "#button-submit-form"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", submitButtonSelector)))
    # submitButton = driver.find_element("css selector", submitButtonSelector)

    personInfo = bitoAiConnect.generateName(personInfoOne["country"])

    firstName = personInfo["firstName"]
    lastName = personInfo["lastName"]
    password = "Night-Angel-610"
    email = emailInfo["login"]+"@"+emailInfo["domain"]

    simulateTyping(firstNameInputSelector, firstName)
    time.sleep(1)
    simulateTyping(lastNameInputSelector, lastName)
    time.sleep(1)
    simulateTyping(emailInputSelector, email)
    time.sleep(1)
    simulateTyping(passwordInputSelector, password)
    time.sleep(1)
    for checkbox in checkboxs:
        checkbox.click()
        time.sleep(1)
    click(submitButtonSelector)
    time.sleep(1)
    print("Signed up to Upwork")


def verifyEmail():
    while True:
        verifyEmailUri = getEmail.getEmailVerifyUri(
            emailInfo["login"], emailInfo["domain"])
        if verifyEmailUri != "":
            driver.get(verifyEmailUri)
            break
        else:
            resendBtnSelector = ".up-btn.up-btn-primary.mr-0.mb-0.btn-block-sm.d-none-mobile-app"
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(("css selector", resendBtnSelector)))
            # resendBtn = driver.find_element(
            #     "css selector", resendBtnSelector)
            click(resendBtnSelector)
            time.sleep(5)
            continue


def clickGetStarted():
    getStartedBtnSelector = "[data-qa='get-started-btn']"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", getStartedBtnSelector)))
    # getStartedBtn = driver.find_element(
    #     "css selector", getStartedBtnSelector)
    click(getStartedBtnSelector)


def skipStep():
    while True:
        try:
            skipBtnSelector = "[data-ev-label='wizard_skip']"
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(("css selector", skipBtnSelector)))
            # skipBtn = driver.find_element(
            #     "css selector", skipBtnSelector)
            click(skipBtnSelector)
            break
        except:
            time.sleep(1)
            continue


def nextStep():
    while True:
        try:
            nextBtnSelector = "[data-ev-label='wizard_next']"
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(("css selector", nextBtnSelector)))
            # nextBtn = driver.find_element(
            #     "css selector", nextBtnSelector)
            click(nextBtnSelector)
            break
        except:
            time.sleep(1)
            continue


def startInputResume():
    while True:
        try:
            fillOutManuallyBtnSelector = "[data-qa='resume-fill-manually-btn']"
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(("css selector", fillOutManuallyBtnSelector)))
            # fillOutManuallyBtn = driver.find_element(
            #     "css selector", fillOutManuallyBtnSelector)
            click(fillOutManuallyBtnSelector)
            break
        except:
            time.sleep(1)
            continue


def inputTitle():
    inputBtnSelector = ".air3-input.form-control"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", inputBtnSelector)))
    # inputBtn = driver.find_element("css selector", inputBtnSelector)
    simulateTyping(inputBtnSelector, personInfoOne["title"])
    time.sleep(1)
    nextStep()


def inputEducation():
    while True:
        try:
            addEducationBtnSelector = "[data-qa='education-add-btn']"
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(("css selector", addEducationBtnSelector)))
            # addEducationBtn = driver.find_element(
            #     "css selector", addEducationBtnSelector)
            click(addEducationBtnSelector)
            break
        except:
            time.sleep(2)
            continue

    time.sleep(1)
    schoolSelector = "[aria-labelledby='school-label']"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", schoolSelector)))
    # schoolInput = driver.find_element(
    #     "css selector", schoolSelector)
    universityName = bitoAiConnect.generateUniversityName(
        personInfoOne["country"])
    simulateTypingForDropdown(schoolSelector, universityName)
    time.sleep(0.5)
    selectFromDropdown()

    degreeSelector = "[aria-labelledby='degree-label']"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", degreeSelector)))
    # degreeInput = driver.find_element(
    #     "css selector", degreeSelector)
    simulateTypingForDropdown(
        degreeSelector, personInfoOne["degree"])
    time.sleep(0.5)
    selectFromDropdown()

    fieldOfStudySelector = "[aria-labelledby='area-of-study-label']"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", fieldOfStudySelector)))
    # fieldOfStudyInput = driver.find_element(
    #     "css selector", fieldOfStudySelector)
    simulateTypingForDropdown(
        fieldOfStudySelector, personInfoOne["fieldOfStudy"])

    time.sleep(1)
    saveEducationBtnSelector = "[data-qa='btn-save']"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", saveEducationBtnSelector)))
    # saveEducationBtn = driver.find_element(
    #     "css selector", saveEducationBtnSelector)
    click(saveEducationBtnSelector)
    time.sleep(1)
    nextStep()


def inputLanguage():
    languageInputSelector = ".air3-dropdown-toggle"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", languageInputSelector)))
    # languageInput = driver.find_element(
    #     "css selector", languageInputSelector)
    click(languageInputSelector)
    time.sleep(0.5)
    selectLanguage()
    time.sleep(1)
    nextStep()


def inputSkills():
    skillInputSelector = "[aria-labelledby='skills-input']"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", skillInputSelector)))
    # skillInput = driver.find_element(
    #     "css selector", skillInputSelector)
    for skill in personInfoOne["skill"]:
        simulateTypingForDropdown(skillInputSelector, skill)
        time.sleep(0.5)
        selectFromDropdown()
        time.sleep(0.5)
    nextStep()


def inputOverview():
    overviewInputSelector = "[aria-labelledby='overview-label']"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", overviewInputSelector)))
    # overviewInput = driver.find_element(
    #     "css selector", overviewInputSelector)
    overview = bitoAiConnect.generateOverview(personInfoOne["title"])
    simulateTyping(overviewInputSelector, overview)
    time.sleep(1)
    nextStep()


def inputCategory():
    categoryButtonSelector = f"[aria-label='{personInfoOne["category"]}']"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", categoryButtonSelector)))
    # categoryButton = driver.find_element(
    #     "css selector", categoryButtonSelector
    # )
    click(categoryButtonSelector)
    time.sleep(1)
    nextStep()


def inputRate():
    rateInputSelector = "[data-ev-label='currency_input']"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", rateInputSelector)))
    # rateInput = driver.find_element(
    #     "css selector", rateInputSelector)
    simulateTyping(rateInputSelector, personInfoOne["rate"])
    time.sleep(1)
    nextStep()


def inputLocation():
    random_number = random.randint(1, 20)
    imgBtnSelector = "[data-qa='open-loader']"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", imgBtnSelector)))
    # imgBtn = driver.find_element("css selector", imgBtnSelector)
    click(imgBtnSelector)
    time.sleep(3)
    uploadButtonSelector = "[data-ev-label='image_crop_input']"
    uploadButton = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", uploadButtonSelector)))
    imagePath = os.path.join(os.getcwd(), "img", f"{random_number}.jpg")
    uploadButton.send_keys(imagePath)
    time.sleep(2)
    imageSaveBtnSelector = "[data-qa='btn-save']"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", imageSaveBtnSelector)))
    # imageSaveBtn = driver.find_element("css selector", imageSaveBtnSelector)
    click(imageSaveBtnSelector)
    time.sleep(2)
    locationInfo = bitoAiConnect.generateLocationInfo(personInfoOne["country"])
    birthday = locationInfo['birthday']
    street = locationInfo['street']
    city = locationInfo['city']
    phoneNumber = locationInfo['number']
    birthdayInputSelector = "[aria-labelledby='date-of-birth-label']"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", birthdayInputSelector)))
    # birthdayInput = driver.find_element(
    #     "css selector", birthdayInputSelector)
    simulateTyping(birthdayInputSelector, birthday)
    selectBirthday()
    streetInputSelector = "[aria-labelledby='street-label']"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", streetInputSelector)))
    # streetInput = driver.find_element(
    #     "css selector", streetInputSelector)
    simulateTyping(streetInputSelector, street)

    cityInputSelector = "[aria-labelledby='city-label']"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", cityInputSelector)))
    # cityInput = driver.find_element("css selector", cityInputSelector)
    simulateTypingForDropdown(cityInputSelector, city)
    time.sleep(1)
    selectFromDropdown()
    phoneNumberInputSelector = '[data-ev-label="phone_number_input"]'
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", phoneNumberInputSelector)))
    # phoneNumberInput = driver.find_element(
    #     "css selector", phoneNumberInputSelector)
    simulateTyping(phoneNumberInputSelector, phoneNumber)
    time.sleep(1)
    nextStep()


def submitProfile():
    submitBtnSelector = '[data-qa="submit-profile-top-btn"]'
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(("css selector", submitBtnSelector)))
    # submitBtn = driver.find_element(
    #     "css selector", submitBtnSelector)
    click(submitBtnSelector)


def main(port, personInfo):
    global option
    global driver
    global personInfoOne
    while True:
        try:
            personInfoOne = personInfo
            option = webdriver.ChromeOptions()
            # Replace with the actual remote debugging address
            option.add_experimental_option(
                "debuggerAddress", f"localhost:{port}")
            option.add_argument("--incognito")

            driver = webdriver.Chrome(options=option)
            navigateToUpwork()
            time.sleep(2)
            navigateToSignUpPage()
            time.sleep(2)
            selectRole()
            time.sleep(2)
            signUpToUpwork()
            time.sleep(10)
            verifyEmail()
            time.sleep(2)
            clickGetStarted()
            time.sleep(2)
            skipStep()  # skip experience
            time.sleep(2)
            skipStep()  # skip goal
            time.sleep(2)
            skipStep()  # skip work-experience
            time.sleep(2)
            startInputResume()
            time.sleep(2)
            inputTitle()
            time.sleep(2)
            skipStep()  # skip employment
            time.sleep(2)
            inputEducation()
            time.sleep(2)
            inputLanguage()
            time.sleep(2)
            inputSkills()
            time.sleep(2)
            inputOverview()
            time.sleep(2)
            inputCategory()
            time.sleep(2)
            inputRate()
            time.sleep(2)
            inputLocation()
            time.sleep(2)
            submitProfile()
            break
        except Exception as e:
            print(e)
            time.sleep(1)
            continue
