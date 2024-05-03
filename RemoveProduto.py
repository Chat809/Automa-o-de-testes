from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

url = "https://munizpn.com.br/produtos/extrato-de-propolis-verde-vida-natural-30ml/"
driver.get(url)

element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".js-item-product"))
)

element.click()

buy_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".js-addtocart"))
)

buy_button.click()

time.sleep(4)

cart_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".js-toggle-cart"))
)

cart_button.click()

time.sleep(3)

remove_button_selector = 'button[data-component="line-item.remove"]'
remove_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, remove_button_selector)))
remove_button.click()

time.sleep(3)

driver.quit()

#Testando funcionalidade de remover produto depois de adicionado com clicks e timesleep.
#Seleção de elementos por seletores CSS.