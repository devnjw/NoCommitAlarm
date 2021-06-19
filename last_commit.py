import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request

from datetime import date

today = date.today()
print(today)

driver = webdriver.Chrome(os.getcwd() + "/chromedriver")
driver.get("https://github.com/devnjw")

items = driver.find_elements_by_css_selector(".ContributionCalendar-day")
for item in items:
    time.sleep(0.01)
    date = item.get_attribute("data-date")
    print(str(today) + " vs ", date)
    if str(today) is date:
        print("SAME")
