from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option('detach', True)
chrm_driver = webdriver.Chrome(options=options)
chrm_driver.get("https://upsrj.edu.mx")

# Create object for Select class


dd1 = Select(chrm_driver.find_element(By.CLASS_NAME, "sf-with-ul-pre sf-with-ul"))
# by index start with 0
dd1.select_by_index(2)



# Value = value propertyid=""
#dd1.select_by_value("Investor")

# Text visible in the options
#dd1.select_by_visible_text("Employee")

#Investor, jobseeker, goverment employee
#1,2,6