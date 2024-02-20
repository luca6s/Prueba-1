import time
from types import TracebackType
import selenium.webdriver as webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

url = 'https://demo-store.seleniumacademy.com/'

class Store_Sele(webdriver.Edge):
    def __init__(self, edge_service = Service(r'C:\Users\prt_lmatamoros\OneDrive - Coordinador Eléctrico Nacional\Documentos\Driver_Edge\msedgedriver.exe'), edge_options = None, keep_alive: bool = True) -> None:
        if edge_options is None:
            edge_options = Options()
            edge_options.add_argument(f'user_agent = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'}')
        self.driver_path = edge_service
        self.keep_alive = keep_alive
        super(Store_Sele, self).__init__()
        self.maximize_window()

    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, traceback: TracebackType | None):
        if self.keep_alive:
            self.quit()
    def get_url(self):
        self.get(url)
    def rellenar_form(self):
        cuenta = self.find_element(By.XPATH, '//span[contains(text(), "Account")]')
        cuenta.click()
        register = self.find_element(By.XPATH, '//a[contains(text(), "Register")]')
        register.click()
        field_register = self.find_element(By.XPATH, '//input[@id="firstname"]')
        field_register.send_keys('lucas')
        time.sleep(5)

