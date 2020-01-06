from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from getpass import getpass

print('Pick email:')
print('1: email 1' + '\n') # add your own email here
print('2: email 2' + '\n') # add your own email here
print('3: email 3' + '\n') # add your own email here

alternative = input()
if alternative == '1':
    usernameStr = 'example@hotmail.com' # add your own email here
elif alternative == '2':
    usernameStr = 'example@hotmail.com' # add your own email here
elif alternative == '3':
    usernameStr = 'example@hotmail.com' # add your own email here

passwordStr = getpass('Password: ')

browser = webdriver.Chrome()

browser.get('https://outlook.live.com/owa/?nlp=1')

username = browser.find_element_by_id('i0116')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_id('idSIButton9')
nextButton.click()

password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'i0118')))
password.send_keys(passwordStr)

sleep(1)
signButton = browser.find_element_by_id('idSIButton9')
signButton.click()
