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
browser.find_element_by_name('emailOrPhone').send_keys("gxdbfamctreq@spacehotline.com") #replace with your mail/temp mail or 10minutes mail
time.sleep(2) 
# Fill the fullname value
fullname_field = browser.find_element_by_name('fullName')
fullname_field.send_keys(account.generatingName())
username_field = browser.find_element_by_name('username')
username_field.send_keys(account.username())
time.sleep(11)

#for password leaved 11 seconds so you must enter your required password in 11 second

input = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/button').click()
time.sleep(2)

#Birthday verification
browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]"))).click()

browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()

browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[29]"))).click()
time.sleep(1)

input = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[6]/button').click()
time.sleep(50)
driver.close()
#in last it ask otp enter the otp tehn account created......
#use proxy to hide instagram and more than 2 accounts use proxy otherwise insta will ban accounts....




















