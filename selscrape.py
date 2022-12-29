from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.whoscored.com/Regions/247/Tournaments/36/Seasons/8213/Stages/18657/PlayerStatistics/International-FIFA-World-Cup-2022'

driver = webdriver.Chrome()
driver.get(url)
element = driver.find_element(By .XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]/span')
element.click()

def getSummaryStatistics(driver):
  
  driver.find_element(By .XPATH, '//*[@id="player-table-statistics-body"]/tr[1]/td[1]/a[1]/span').text.strip())
# table = driver.find_element(By.CLASS_NAME, 'grid with-centered-columns hover')
# name = driver.find_element(By.XPATH, '//*[@id="player-table-statistics-body"]/tr[1]/td[1]/a[1]/span/text()')
# # # //*[@id="player-table-statistics-body"]/tr[1]/td[1]/a[1]/span/text()
# # # //*[@id="player-table-statistics-body"]/tr[2]/td[1]/a[1]/span/text()


# def get_data(url):
#   driver.get(url)
#   driver.quit()

# get_data()