from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
options = Options()
options.add_experimental_option('detach', True)

chrm_driver = webdriver.Chrome(options=options)

chrm_driver.get("https://www.sat.gob.mx/home")

chrm_driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')

ver_mas = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/personas/tramites-del-rfc"]')))
ver_mas.click()
