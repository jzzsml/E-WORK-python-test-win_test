import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urllib import request
import os

def init_driver():
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 1)
    return driver
 
 
def lookup(driver,i):
    driver.get("https://www.ligastavok.ru/bets/popular/rossiiskaiapremer-liga-5271")
    try:
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[%d]/div[2]/div[2]/div[1]/span[2]"%i)))
            #(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/span[1]")))
        button.click()
        urlINeed = driver.current_url
        filetxt = open('savedURL.txt', 'a')
        filetxt.write(urlINeed)
        filetxt.write('\n')
        filetxt.close()

        print("________________________")
        print("__________%d/100________"%(10*i))
    except TimeoutException:
        print("Something wrong whith me...")
    
 
#def get_url(): 
if __name__ == "__main__":
    os.remove('savedURL.txt')
    driver = init_driver()    
    i = 1
    while i<11:
        lookup(driver,i)
        i = i + 1
    time.sleep(1)
    driver.quit()
        
    

    