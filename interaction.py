from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/Devlopment/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
count = driver.find_elements_by_css_selector("#articlecount a")[0]
print(count.text)
# count.click() to click a link

# get the link by link name

all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()


#Enter text in field

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)




