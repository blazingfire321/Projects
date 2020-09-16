import time;
from selenium import webdriver;

#time to refresh page (seconds)
Timer = 120

#youtube link
link = 'https://www.youtube.com/watch?v=H7lBW3r9V5U&ab_channel=CrimsonDoge'

#number of views
views = 20

driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
    print(i)
