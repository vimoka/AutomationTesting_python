import time
from selenium import webdriver

username = open("C:\\Users\\lviha\\Desktop\\emailinput.txt","r").read()

password = open("C:\\Users\\lviha\\Desktop\\passwordinput.txt","r").read()

driver = webdriver.Chrome("C:\\Users\\lviha\\Desktop\\chromedriver.exe")
driver.get("http://automationpractice.com/index.php")

driver.find_element_by_class_name("login").click()
try:
    email = driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
    pswd = driver.find_element_by_xpath("//*[@id='passwd']").send_keys(password)
    time.sleep(2)
    login = driver.find_element_by_id("SubmitLogin").click()
except:
    print("invalid email or password")
finally:
    print("login was successful")    

driver.find_element_by_xpath("//*[@id='block_top_menu']/ul/li[1]/a").click()
item1 = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[2]/div/div[2]/div[2]/a[1]/span").click()

try:
    quantity = driver.find_element_by_xpath("//*[@id='quantity_wanted']").get_attribute("value")
    print("the selected quantity of items is " +quantity)
except:
    print("the quantity of item selected is greater than 1,are you sure?")
finally:
    chkout = driver.find_element_by_id("add_to_cart").click()  
      
    proceed_to_chkout = driver.find_element_by_xpath("//span[normalize-space(text())='Proceed to checkout']").click()