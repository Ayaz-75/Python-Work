from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


py_link = "https://www.python.org/"
chrome_driver_path = "C:\Development\chromedriver.exe"



s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get(py_link)


event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
names_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# print(menu_list)
times = []
names = []


for item in event_times:
    times.append(item.text)

for name in names_list:
    names.append(name.text)

events = {}
for n in range(len(event_times)):
    events[n] = {

        "time": event_times[n].text,
        "names": names_list[n].text,

    }


# print(events)

new_dict = {n: names_list[n].text for n in range(len(event_times))}

# print(new_dict)






driver.quit()