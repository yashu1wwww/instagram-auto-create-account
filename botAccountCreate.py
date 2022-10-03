from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import accountInfoGenerator as account

browser = webdriver.Chrome()
browser.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(5)
#name = account.username()
#time.sleep(3)
browser.find_element_by_name('emailOrPhone').send_keys("ugi07248@nezid.com") #replace with your mail/10 minutes mail/temp mail/phone no
time.sleep(2) 
# Fill the fullname value
fullname_field = browser.find_element_by_name('fullName')
fullname_field.send_keys(account.generatingName())
username_field = browser.find_element_by_name('username')
username_field.send_keys(account.username())
time.sleep(10)
#you must enter password and click next button because of part process you cant remember the password so you have 10 second time for it so you remember it and remaining things go automated
#Birthday verification
browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]"))).click()

browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()

browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()
time.sleep(50)
driver.close()










