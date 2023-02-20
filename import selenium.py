import re
import time

import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from makeDataframe import dataframeFormatter
from selenium import webdriver


flattened = pd.DataFrame(columns=
[
'Game Id'
,'Home Possession'
,'Away Possession'

,'Home Shots on Target'
,'Away Shots on Target'

,'Home Shots'
,'Away Shots'

,'Home Touches'
,'Away Touches'

,'Home Passes'
,'Away Passes'

,'Home Tackles'
,'Away Tackles'

,'Home Clearances'
,'Away Clearances'

,'Home Corners'
,'Away Corners'

,'Home Offsides'
,'Away Offsides'

,'Home Yellow cards'
,'Away Yellow cards'

,'Home Fouls conceded'
,'Away Fouls conceded'
]) 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for x in range(75130,75140):

    while True:
        try:
            # print(driver.page_source)
            driver.implicitly_wait(5)
            wait = WebDriverWait(driver, 20)

            driver.get("https://www.premierleague.com/match/" + str(x))

            # wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[1]/div[5]/button[1]')))
            # driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[5]/button[1]').click()

            driver.implicitly_wait(5)
            element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[5]/button[1]')
            driver.execute_script("arguments[0].click();", element)

            driver.implicitly_wait(5)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainContent"]/div/section[2]/div[2]/div[2]/div[1]/div/div/ul/li[3]')))
            driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/section[2]/div[2]/div[2]/div[1]/div/div/ul/li[3]').click()

            #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mainContent"]/div/section[2]/div[2]/div[2]/div[1]/div/div/ul/li[3]'))).click()
            driver.implicitly_wait(5)
            tables = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/section[2]/div[2]/div[2]/div[2]/section[3]/div[2]/div[2]/table/tbody')
            print(tables.get_attribute('innerHTML'))


            html_table = '<Table>' + tables.get_attribute('innerHTML') + '</Table>'
            # Fix ValueError: No tables found matching pattern '.+'
            html_source = re.sub(r'<.*?>', lambda g: g.group(0).upper(), html_table)


            dfs = pd.read_html(html_source, displayed_only=False)

            #dfs.to_csv('footyData.csv', sep=',', encoding='utf-8')


            # print(dfs)
            # print('\n')
            # print(dfs[0][0][0])

            dfs[0].to_csv('out.csv',index=False)
            #list_row = ["Hyperion", 27000, "60days", 2000]

            time.sleep(4)

            driver.implicitly_wait(25)

            formatted = dataframeFormatter(x)

            flattened.loc[len(flattened)] = formatted



            #print(formatted)
            # #table_id =   WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mainContent']/div/section[2]/div[2]/div[2]/div[1]/div/div/ul/li[3]"))).click()

            # myElem = wait.until(EC.element_to_be_clickable(((By.XPATH,"//ul[@class='tablist']/li[2]")))).click()
        except ValueError:
            print('Retry')
            continue
        break


    print(flattened)


    


driver.quit()

# //*[@id="mainContent"]/div

print(formatted)
flattened.to_csv('final.csv',index=False)
