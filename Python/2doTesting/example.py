#Actions chains - acciones en cadena

# **** Imports ************
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#******************

# ***+ Chrome options - to keep it open *********+
options = Options()
options.add_experimental_option('detach', True)

browser = webdriver.Chrome(options=options)



# ***** Site URL to be tested *************
browser.get("http://upsrj.edu.mx/")
browser.maximize_window()
time.sleep(3)
# ***************************
# **** Wait Object ***
wait = WebDriverWait(browser, 4) # <-SE USA HASTA QUE LO MANDO LLAMAR
browser.implicitly_wait(5) # <- CADA ACCION VA A TARDAR MAX 5

# ************

#*** Action Object ******
action = ActionChains(browser)
#**************



""" element = browser.find_element(By.ID, "ID")

action.double_click(element)
action.context_click(element) # <- CLICK DERECHO
action.move_to_element(element)# <- Hover
action.drag_and_drop(element)
action.pause(element) 

cada action debe tener al final .perform() aunque sean multiples acciones"""

academics = browser.find_element(By.XPATH, "//ul[@id='menu-sta-rosa-1']/li[1]")
action.move_to_element(academics).perform()
programs = browser.find_element(By.LINK_TEXT, "Investigación")
action.move_to_element(programs).perform()
dat = browser.find_element(By.LINK_TEXT, "Lineas de Investigación")
action.move_to_element(dat).perform()
SW = browser.find_element(By.LINK_TEXT, "Software")
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Software")))
action.move_to_element(SW).click().perform()
#action.scroll_by_amount(500, 1300).perform()