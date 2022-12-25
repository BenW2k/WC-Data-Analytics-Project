from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.whoscored.com/Regions/247/Tournaments/36/Seasons/8213/Stages/18657/PlayerStatistics/International-FIFA-World-Cup-2022'

driver = webdriver.Chrome()

driver.get(url)

table = driver.find_element(By.CLASS_NAME, 'grid with-centered-columns hover')

for x in range(1,5):
    