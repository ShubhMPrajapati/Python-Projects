import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")  # Open browser in incognito mode

driver = uc.Chrome(version_main=129, options=chrome_options)

driver.get("https://bumble.com/")
driver.find_element(By.XPATH, '//*[@id="main"]/section[1]/div/div[2]/div/div[2]/div/div[3]/a').click()
time.sleep(8)

driver.find_element(By.XPATH, '//button[contains(@class,"color-provider-facebook")]').click()

input("Click Enter After Loging in with details...")
i = 0
while i <20:
    driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[2]/div/div[1]/span').click()
    i+=1
    time.sleep(1)
driver.quit()

