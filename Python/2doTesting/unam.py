import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)

# ***** Site URL to be tested *************
browser.get("https://www.unam.mx/")
browser.maximize_window()
time.sleep(3)

# *** Action Object ******
action = ActionChains(browser)

# *** Acciones en cadena *******************

# 1. Movemos el cursor a "Comunidad"
comunidad_element = browser.find_element(By.XPATH, "//li[@class='sf-depth-1 menuparent active sf-with-ul']")
action.move_to_element(comunidad_element).perform()

# 2. Esperamos a que el submenu "Estudiantes" sea visible
estudiantes = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='sf-depth-1 menuparent active sf-with-ul']")))

# 3. Movemos el cursor a "Estudiantes"
action.move_to_element(estudiantes).perform()

# 4. Hacemos clic en "Servicios Universitarios"
servicios_universitarios = browser.find_element(By.XPATH, "//a[@href='/servicios-universitarios']")
action.move_to_element(servicios_universitarios).click().perform()

# 5. Extraemos el título de la página
titulo_pagina = browser.title

# 6. Imprimimos el título de la página
print(titulo_pagina)

# Se deja el navegador abierto para inspección manual
