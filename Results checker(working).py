import time
import pyautogui
def enter():
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter") 
def tab():
    pyautogui.keyDown("tab")
    pyautogui.keyUp("tab") 
def slow_typing(element, text):
    for character in text: 
        element.send_keys(character)
        time.sleep(0.3)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
hall = input("Hall ticket.no=> ")
dob = input("Date of birth(DDMMYYYY)=> ")
driver = webdriver.Edge('msedgedriver.exe')
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
tab() 
time.sleep(2)
for character in dob:
    pyautogui.keyDown(character)
    pyautogui.keyUp(character)
    time.sleep(1)
tab()
enter()
time.sleep(3)
enter()
time.sleep(3)
tab()
enter()
y=10
while y>0:
    tab()
    y=y-1
enter()
time.sleep(10)
name = (f"Marks of_{hall}")

for x in name:
    pyautogui.keyDown(x)
    pyautogui.keyUp(x)
    time.sleep(0.2)
enter()
time.sleep(10)
driver.close()
