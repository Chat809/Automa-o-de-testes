from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

navegador = webdriver.Chrome()
navegador.get("https://munizpn.com.br/")

wait = WebDriverWait(navegador, 10)

try:
    campo_busca = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    campo_busca.send_keys("maçã")
    
    time.sleep(2)

    botao_busca = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.search-input-submit")))
    botao_busca.click()

    time.sleep(3)
finally: 
    navegador.quit()

#Utilizei os imports para garantir a localização do elemento, primeiramente preenchendo o campo de input e depois acionando o botão para submeter.