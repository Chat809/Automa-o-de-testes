from selenium import webdriver
import time
navegador = webdriver.Chrome()
navegador.get("https://munizpn.com.br/")

time.sleep(1)  
navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
navegador.execute_script("window.scrollBy(1000, 0);")
time.sleep(1)
navegador.execute_script("window.scrollBy(-1000, 0);")
time.sleep(1)
navegador.execute_script("window.scrollBy(0, -document.body.scrollHeight);")
time.sleep(3)

navegador.quit()

#Testando dimensionamento do site scrolando para baixo, direita, esquerda e cima, retornando para posição inicial.
#Funções time.sleep para intervalos de tempo, window.scroll para percorrer eixos em pixels.