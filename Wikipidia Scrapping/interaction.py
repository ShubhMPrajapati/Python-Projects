from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)

driver.get('https://orteil.dashnet.org/experiments/cookie/')

coockie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
i = 0
while i < 2500:
    coockie.click()
    i+=1

mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]')
mine.click()

driver.find_element(By.XPATH,'//*[@id="exportSave"]').click()

driver.quit()

