from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def available(url:str) -> bool | str:
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(0.5)
    try:
        site=driver.find_element(by=By.CLASS_NAME, value="styled__AlertStyled-sc-p35rtj-0")
        return False
    except NoSuchElementException:
        driver.implicitly_wait(0.5)
        site = driver.find_element(by=By.CLASS_NAME, value="styled__UnitPriceStyled-sc-kfm84t-2")
        return site.text



if __name__ == "__main__":
    print('This is just a module, cant be executed without the main program') 
    
    
    
    
    
    
    
    
    
    
