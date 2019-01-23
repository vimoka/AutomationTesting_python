
import time
from selenium import webdriver

#Setting up the driver path and instantiating chrome driver 
DriverPath = "C:\\Users\\lviha\\Desktop\\chromedriver.exe"
driver = webdriver.Chrome(DriverPath)

emailid = open("C:\\Users\\lviha\\Desktop\\emailinput.txt","r")
emailcontent = emailid.read()

pswd = open("C:\\Users\\lviha\\Desktop\\passwordinput.txt","r")
pswdcontent = pswd.read()
#Opening the Gmail website to check the login functionality
driver.get("http://www.gmail.com")

#Entering the email id
emailid = driver.find_element_by_id("identifierId")
emailid.send_keys(emailcontent)

#Hitting the next button
driver.find_element_by_class_name("CwaK9").click()
time.sleep(5)

#Entering the password
passwd = driver.find_element_by_name("password")
passwd.send_keys(pswdcontent)
time.sleep(3)

#Submitting the login
driver.find_element_by_class_name("CwaK9").click()
time.sleep(10)

#Closing the driver
driver.close()