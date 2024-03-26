from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome options
options = Options()
options.add_experimental_option('detach', True)

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=options)

# Open the Gandhi website
driver.get("https://www.gandhi.com.mx/#")

# XPath for the 'Accesorios' link
accessories_xpath = '/html/body/div[2]/div/header/div[2]/section/nav/ul/li[6]/a'

# XPath for the 'Separadores' link
separadores_xpath = '/html/body/div[2]/div/header/div[2]/section/nav/ul/li[6]/div/div[1]/ul[2]/li[1]/ul/li/a/span'

# XPath for the 'Disponible' element
disponible_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div/div[4]/div[1]'

# XPath for the first new element to be clicked
first_new_element_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/ol/li/a/label/span[1]'

# XPath for the second new element to be clicked
second_new_element_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div/div[5]/div[2]/div/ol/li/a/label/span[1]'

# XPath for the additional element to be clicked
additional_element_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div[3]/div[3]/div[1]'

# XPath for the newly added element to be clicked
newly_added_element_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div/div[5]/div[2]/div/ol/li/a/label/span[1]'

# Wait and click on the 'Accesorios' link
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, accessories_xpath))).click()

# Wait and click on the 'Separadores' link
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, separadores_xpath))).click()

# Wait and click on the 'Disponible' element
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, disponible_xpath))).click()

# Wait and click on the first new element
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, first_new_element_xpath))).click()

# Wait and click on the second new element
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, second_new_element_xpath))).click()

# Wait and click on the additional element
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, additional_element_xpath))).click()

# Wait and click on the newly added element
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, newly_added_element_xpath))).click()

# Add any further automation steps here if needed

# Close the browser (optional, remove if you want the browser to stay open)
# driver.quit()

driver.save_screenshot()