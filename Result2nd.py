import pyautogui
import time
def tab():
    pyautogui.keyDown("tab")
    pyautogui.keyUp("tab")
def enter():
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter") 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
hall = input("Hall ticket.no=> ")
#hall = "2108224272"
driver = webdriver.Edge('msedgedriver.exe')
time.sleep(6)
driver.get("http://examresults.ap.nic.in/Inter2GenResult_dts.aspx")
time.sleep(3)
tab()
for character in hall:
    pyautogui.keyDown(character)
    pyautogui.keyUp(character)
    time.sleep(0.3)
enter()
time.sleep(5)
x=4
while x>0:
    tab()
    x=x-1
enter()
time.sleep(5)
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