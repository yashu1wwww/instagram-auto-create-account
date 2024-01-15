from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import random

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/sem/campaign/emailsignup/?campaign_id=13530338610&extra_1=s%7Cc%7C547419127163%7Ce%7Cinstagram%20account%20create%7C&placement=&creative=547419127163&keyword=instagram%20account%20create&partner_id=googlesem&extra_2=campaignid%3D13530338610%26adgroupid%3D126262413294%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-1321618851571%26loc_physical_ms%3D1007768%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=CjwKCAiAqY6tBhAtEiwAHeRopeIwzferJ9NOpJyFgYWi4aakB8yssdbWVU-Yhtb2LodWlJqD3d1WhRoCsjkQAvD_BwE")

time.sleep(3)

driver.find_element_by_name("emailOrPhone").send_keys("123email@gmail.com") #email or ph.no replace
driver.find_element_by_name("fullName").send_keys("instaaa") #name 
driver.find_element_by_name("username").send_keys("insta@_123")  #username 
driver.find_element_by_name("password").send_keys("Insta123@#$%") #password 
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[8]/div/button').click()
time.sleep(5)
#Birthday verification
dropdown_element = driver.find_element(By.CLASS_NAME, "_aau-")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("March") #change to required
time.sleep(2)
dropdown_element = driver.find_element(By.CLASS_NAME, "_aau-")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("March") #change to required
time.sleep(2)
dropdown_element = driver.find_element(By.CLASS_NAME, "_aau-")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("1998") #change to required
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div/div[6]/button').click()
#Ask otp enter and click on next button thats it..(dont forgot to save the username and password)
time.sleep(30)  

