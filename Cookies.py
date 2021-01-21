from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/Users/Devlopment/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

clickable_cookie = driver.find_element_by_id("cookie")

store = driver.find_elements_by_css_selector("#rightPanel #store .grayed")
print(store)
store_prices = driver.find_elements_by_css_selector("#rightPanel #store div b")

prices_arr = []
for s in store_prices:
    text = s.text
    print(text)
    new_s = ""
    for c in s.text:
        if c.isnumeric():
            new_s += c
    print(new_s)
    try:
        int_val = int(new_s)
    except:
        continue
    else:
        prices_arr.append(int_val)

timeout = time.time() + 60 * 5
while True:
    number_cookies = driver.find_element_by_id("money").text
    clickable_cookie.click()
    if time.time() > timeout:
        print(number_cookies)
    for i in range(len(prices_arr)-1, 0, -1):
        if int(number_cookies) > prices_arr[i]:
            div = store[i]
            print(div)
            div.click()
            print(i)
            break



