
#! https://www.youtube.com/watch?v=Zauls_kTjYM
#! https://demo-store.seleniumacademy.com/
import time
import selenium.webdriver as webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
#*El user agent indica el buscador al que estaremos accediendo y las versiones
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
#*Este es para indicar donde buscar al driver
edge_driver_path = r'C:\Users\prt_lmatamoros\OneDrive - Coordinador Eléctrico Nacional\Documentos\Driver_Edge\msedgedriver.exe'
edge_service = Service(edge_driver_path)
edge_options = Options()
edge_options.add_argument(f'user-agent={user_agent}')
#*Aquí le decimos al selenium cuales son los navegadores a trabajar y el webdriver que usaremos
browser = webdriver.Edge(service=edge_service, options=edge_options)
#*Entrar al url que se desea y agrandar hoja, mantenerlo ahí para que se pueda ver, ojo que con muy poco tiempo de sleep puede que no cargue, y tampoco es necesario el sleeep
browser.maximize_window()
browser.get('https://demo-store.seleniumacademy.com/')

#*Ahora se buscan los elementos que se desean
# texto_1 = browser.find_element(By.XPATH, '//nav/ol/li/a[contains(text(), "Women")]')
# print(texto_1.text)

#textos_2 = browser.find_elements(By.XPATH, '//nav/ol/li/a')
#for i in textos_2:
#    print(i.text)
#*Los elementos se buscan a traves de sus textos en el XPATH y una vez guardados se hacen click
cuenta = browser.find_element(By.XPATH, '//span[contains(text(), "Account")]')
cuenta.click()
register = browser.find_element(By.XPATH, '//a[contains(text(), "Register")]')
register.click()

field_register = browser.find_element(By.XPATH, '//input[@id="firstname"]')
field_register.send_keys('lucas')
#fiel_register = browser.find_elements(By.XPATH, '//div/form/div/ul/li/div/div/div/input[contains(@class, "input-text required-entry")]')
#
#for i in fiel_register:
#    print(i.text)

time.sleep(5)