from selenium import webdriver

chrome_driver_path = "/Users/Devlopment/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_titles = driver.find_elements_by_css_selector(".event-widget .menu a")

ls_event_times = [time.text for time in event_times]
ls_event_titles = [title.text for title in event_titles]
events = {index: {'time': ls_event_times[index], 'name': ls_event_titles[index]} for index in range(len(event_titles))}
print(events)
driver.quit()
