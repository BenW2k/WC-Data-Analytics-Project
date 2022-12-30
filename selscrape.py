from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

url = 'https://www.whoscored.com/Regions/247/Tournaments/36/Seasons/8213/Stages/18657/PlayerStatistics/International-FIFA-World-Cup-2022'
player_list = []
count = 1
delay = 3 # seconds

driver = webdriver.Chrome()
driver.get(url)
driver.set_window_size(1920, 1080)
driver.maximize_window()
element = driver.find_element(By .XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]/span')
element.click()
# next_page = driver.find_element(By .ID, 'next')

def getSummaryStatistics(index):
    players = driver.find_elements(By .XPATH, '//*[@id="stage-top-player-stats-summary"]')
    index = count
    try:
        while len(player_list) != 546:
            for player in players:
                print(f'index: {index}')
                print(f'length: {len(player_list)}')
                player = {
                    'name' : driver.find_element(By .XPATH, f'//*[@id="player-table-statistics-body"]/tr[{index}]/td[1]/a[1]/span').text.strip(),
                    'nationality' : driver.find_element(By .XPATH, f'//*[@id="player-table-statistics-body"]/tr[{index}]/td[1]/a[2]/span').text.strip(),
                    'position' : driver.find_element(By .XPATH, f'//*[@id="player-table-statistics-body"]/tr[{index}]/td[1]/span/span[2]').text.strip(),
                    'assists' : driver.find_element(By .XPATH, f'//*[@id="player-table-statistics-body"]/tr[{index}]/td[6]').text.strip(),
                    'yellow cards' : driver.find_element(By .XPATH, f'//*[@id="player-table-statistics-body"]/tr[{index}]/td[7]').text.strip(),
                    'red cards' : driver.find_element(By .XPATH, f'//*[@id="player-table-statistics-body"]/tr[{index}]/td[7]').text.strip(),
                    'shots per game' : driver.find_element(By .XPATH, f'//*[@id="player-table-statistics-body"]/tr[{index}]/td[9]').text.strip(),
                    'pass%' : driver.find_element(By .XPATH, f'//*[@id="player-table-statistics-body"]/tr[{index}]/td[10]').text.strip(),
                    'aerials won' : driver.find_element(By .XPATH, f'//*[@id="player-table-statistics-body"]/tr[{index}]/td[11]').text.strip(),
                    'MotM awards' : driver.find_element(By .XPATH, f'//*[@id="player-table-statistics-body"]/tr[{index}]/td[12]').text.strip(),
                }
                player_list.append(player)
                if index % 10 == 0:
                    print('Going to next page')
                    
                    try:
                        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'next')))
                        print("Page is ready!")
                        myElem.click()

                    except TimeoutException:
                        print("Loading took too much time!")

                    index = 1

                else:
                    index = index + 1          
    except:
        pass

for x in range(1,100):
    getSummaryStatistics(count)

# print(player_list)