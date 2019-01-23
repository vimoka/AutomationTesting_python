
import time
from selenium import webdriver
from selenium.webdriver.remote import webelement
from _ast import If

#setting username and password
username = open("C:\\Users\\lviha\\Desktop\\emailinput.txt","r")
usr = username.read()

password = open("C:\\Users\\lviha\\Desktop\\passwordinput.txt","r")
pswd = password.read()

firstname = "Vimoka"
lastname = "Nalluri"
#setting driver path
DriverPath = "C:\\Users\\lviha\\Desktop\\chromedriver.exe"
driver = webdriver.Chrome(DriverPath)

#email signup
driver.get("http://automationpractice.com/index.php")
driver.find_element_by_class_name("login").click()
email = driver.find_element_by_id("email_create")
email.send_keys(usr)
time.sleep(5)
nextbutton = driver.find_element_by_id("SubmitCreate").click()
time.sleep(3)

#filling up the signup form
button = driver.find_element_by_id("uniform-id_gender2").click()
#setting first name and last name and password
first_name = driver.find_element_by_id("customer_firstname")
first_name.send_keys(firstname)

last_name = driver.find_element_by_id("customer_lastname")
last_name.send_keys(lastname)

paswd = driver.find_element_by_name("passwd")
paswd.send_keys(pswd)
 
#selecting date of birth
DayOfBirth = driver.find_element_by_id("days")
DayOfBirth.select_by_value('26')

MonthOfBirth = driver.find_element_by_id("months")
MonthOfBirth.select_by_value('10')

YearOfBirth = OfBirth = driver.find_element_by_id("years")
YearOfBirth.select_by_value('1993')

#signing up for personal information 
address = driver.find_element_by_name("address1")
address.send_keys("1223 112th ave s")

city = driver.find_element_by_name("city")
city.send_keys("bellevue")

state = driver.find_element_by_id("id_state")
state.select_by_visible_text("Washington")

phone = driver.find_element_by_id("phone_mobile")
phone.send_keys("9908236565")

AliasAddress = driver.find_element_by_id("alias")
AliasAddress.send_keys("bellevue,washington")

#Registering 
Register = driver.find_element_by_id("submitAccount").click()
time.sleep(5)

#Returning to homepage
home = driver.find_element_by_class_name("btn btn-default button button-small").click()
time.sleep(3)

#signout
signout = driver.find_element_by_class_name("logout").click()
time.sleep(5)

#signin
driver.find_element_by_class_name("login").click()
driver.find_element_by_id("email").send_keys(usr)
driver.find_element_by_id("passwd").send_keys(pswd)
login = driver.find_element_by_id("SubmitLogin").click()
