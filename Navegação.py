from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()
navegador.get("https://munizpn.com.br/")

elementos_a = navegador.find_elements(By.CSS_SELECTOR, ".js-nav-desktop-list a")

for elemento_a in elementos_a:
    url_link = elemento_a.get_attribute("href")
    navegador.execute_script("window.open('{}', '_blank');".format(url_link))
    time.sleep(2)

navegador.quit()

#Estrutura de repetição para cada elemento a dentro da classe da ul do site, abrindo nova guia e prosseguindo para o próximo elemento até que todos tenham sido percorridos.