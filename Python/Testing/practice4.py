from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option('detach', True)

chrm_driver = webdriver.Chrome(options=options)

chrm_driver.get("https://www.sat.gob.mx/home")

chrm_driver.find_element(By.ID, "mob_search_inputE").send_keys("factura")
time.sleep(2)
results = chrm_driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(results))
for result in results:
    if result.text == "Factura electrónica":
        result.click()
        break
        
#click_factura = lambda results: next((result.click() for result in results if result.text == "Factura electrónica"), None)
#click_factura(results=results)