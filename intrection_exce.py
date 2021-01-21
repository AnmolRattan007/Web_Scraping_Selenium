from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "/Users/Devlopment/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
signup = driver.find_element_by_class_name("btn")
first_name.send_keys("A")
last_name.send_keys("R")
email.send_keys("AR@ad.ad")
signup.click()


