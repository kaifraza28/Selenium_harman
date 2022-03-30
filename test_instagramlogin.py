import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

print("Test case started!")
driver.maximize_window()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(1)
driver.find_element_by_name("username").send_keys("kaif.__.raza")
driver.find_element_by_name("password").send_keys("K@ppu2801")
driver.find_element_by_class_name("EPjEi").click()
time.sleep(1)
driver.close()
print("Instagram login done succesufully")
print("Test case has sucessfully completed!")