import time
import pyautogui
def slow_typing(element, text):
    for character in text: 
        element.send_keys(character)
        time.sleep(0.3)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
hall = input("Hall ticket.no=> ")
dob = input("Date of birth(DDMMYYYY)=> ")
#hall = "1234567890"
#dob = "03102004"
driver = webdriver.Edge('msedgedriver.exe')
import time
time.sleep(6)
driver.get("https://results.bie.ap.gov.in/AP_Second_Year_General.do")
time.sleep(3)
print(driver.title)
hallticket_no = driver.find_element_by_id("hallticket_no")
hallticket_no.click()
for character in hall:
    pyautogui.keyDown(character)
    pyautogui.keyUp(character)
    time.sleep(0.3) 
pyautogui.keyDown("tab")
pyautogui.keyUp("tab") 
time.sleep(2)
for character in dob:
    pyautogui.keyDown(character)
    pyautogui.keyUp(character)
    time.sleep(1)
pyautogui.keyDown("tab")
pyautogui.keyUp("tab")
pyautogui.keyDown("enter")
pyautogui.keyUp("enter") 