
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

#composing an email
driver.find_element_by_css_selector((".aic .z0 div")).click()

#selecting the recepient 
recepient = driver.find_element_by_css_selector((".oj div textarea"))
recepient.send_keys("vnalluri@uncc.edu")

#subject of the email being sent
subject = driver.find_element_by_css_selector((".aoD.az6 input"))
subject.send_keys("Sending email using Python Automation")

#Entering the content of the email
Econtent = driver.find_element_by_css_selector((".Ar.Au div"))
Econtent.send_keys("Hi, just checking the email automating functionality")

#clicking the send button
sendButton = driver.find_element_by_css_selector((".T-I J-J5-Ji.aoO.T-I-atl.L3.T-I-Zf-aw2")).click()

#Closing the driver
driver.close()