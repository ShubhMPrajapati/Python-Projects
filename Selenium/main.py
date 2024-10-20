from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Selenium WebDriver (e.g., using Chrome)
driver = webdriver.Chrome()

driver.get('https://www.python.org/')



time_element = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul a')
event = {}
for n in range(len(time_element)):
    event[n] = {
        "time": time_element[n].text,
        "event": events[n].text
    }


print(event)





driver.quit()
