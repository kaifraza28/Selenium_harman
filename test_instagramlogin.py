import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
user_input = input("Please Enter your user_name\n")
user_input2 = input("Please Enter your Password\n")

driver = webdriver.Chrome(ChromeDriverManager().install())

print("Test case started!")
driver.maximize_window()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(1)
driver.find_element_by_name("username").send_keys(user_input)
driver.find_element_by_name("password").send_keys(user_input2)
driver.find_element_by_xpath("//button[@type='submit']").click()
# driver.find_element_by_class_name("_9zn7").click()
time.sleep(10)
driver.close()
print("Instagram login done succesufully")
print("Test case has sucessfully completed!")