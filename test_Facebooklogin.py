import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test Case Started")
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element_by_name("email").send_keys("kaifraza8329@gmail.com")
time.sleep(2)
driver.find_element_by_name("pass").send_keys("78600713570")
time.sleep(4)
driver.find_element_by_name("login").click()

time.sleep(3)
driver.close()
print("Test cases has successfully completed")
