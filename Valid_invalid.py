
import time
from selenium import webdriver
from _ast import Try

DriverPath = "C:\\Users\\lviha\\Desktop\\chromedriver.exe"
driver = webdriver.Chrome(DriverPath)
emailid = open("C:\\Users\\lviha\\Desktop\\emailinput.txt","r")
emailcontent = emailid.read()
pswd = open("C:\\Users\\lviha\\Desktop\\passwordinput.txt","r")
pswdcontent = pswd.read()
#Opening the Gmail website to check the login functionality
driver.get("http://www.gmail.com")

def valid_login():
    emailid = driver.find_element_by_id("identifierId")
    emailid.send_keys(emailcontent)
    
    driver.find_element_by_class_name("CwaK9").click()
    time.sleep(5)

    passwd = driver.find_element_by_name("password")
    passwd.send_keys(pswdcontent)
    time.sleep(3)

    driver.find_element_by_class_name("CwaK9").click()
    time.sleep(10)

    driver.close()
       
def invalid_login():
    
    emailid = driver.find_element_by_id("identifierId")
    try:
        emailid.send_keys(emailcontent)
        driver.find_element_by_class_name("CwaK9").click()
        time.sleep(5)
    except:
        print("invalid email id. please enter a valid email id below")
    else:
        passwd = driver.find_element_by_name("password")
    try:
        passwd.send_keys("pwsdfty")
        time.sleep(3)
        driver.find_element_by_class_name("CwaK9").click()
        time.sleep(10)
    except:
        print("invalid password. please check and enter valid password below")
        
    finally:
        driver.close()     

if __name__ == "__main__":
    valid_login()
    invalid_login()
       
    