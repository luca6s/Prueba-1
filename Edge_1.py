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
browser.get('http://demo-store.seleniumacademy.com/')
time.sleep(10)
#*Ahora tienes que seguir viendo el video y tratar de apretar botones