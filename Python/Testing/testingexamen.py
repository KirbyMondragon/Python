from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

driver.get("https://www.sat.gob.mx/personas")

#Espacio donde desplegamos el menu, simulando raton
rfc = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "1462228502462")))

hover = ActionChains(driver).move_to_element(rfc)
hover.perform()

#Tiempo de espera
time.sleep(5)

obtener_RFC = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/personas/tramites-del-rfc"]')))
obtener_RFC.click()

if driver.current_url == "https://www.sat.gob.mx/personas/tramites-del-rfc":
    print("Verification that the Url has the words: tramites-del-rfc")
if driver.current_url == "https://www.sat.gob.mx/personas/tramites-del-rfc":
    print("You don't find the url")
    
time.sleep(5)

obtener_rfc = driver.find_element(By.CSS_SELECTOR, 'a[href="/tramites/28753/obten-tu-rfc-con-la-clave-unica-de-registro-de-poblacion-curp"]')
driver.execute_script("arguments[0].click();", obtener_rfc)

driver.save_screenshot("ScreenShotSAT.jpg")