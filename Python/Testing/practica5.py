from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.wikipedia.org/")

search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Steam Deck")
search_box.submit()

wait = WebDriverWait(driver, 10)
first_result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.mw-search-result-heading a")))
first_result.click()

wait.until(EC.presence_of_element_located((By.ID, "firstHeading")))
content = driver.find_elements(By.CSS_SELECTOR, "div.mw-parser-output > p")
if content:
    print(content[0].text)
else:
    print("No content found.")
