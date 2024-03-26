from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options




options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)


driver.get("https://upsrj.edu.mx/sistemaintegral/web/alumnos.php")
print("######### URL #########")
print(driver.current_url)
print("------------------------------- \n")

driver.find_element(By.ID, "signin_username").send_keys("016000057")
driver.find_element(By.ID, "signin_password").send_keys("12345678")




# What if the website does not have ID, class, name
# We can use Xpath

driver.find_element(By.XPATH, "//input[@type='submit']").click()
msj = driver.find_element(By.CLASS_NAME, "error_list").text
print("#######MESSAGE###########")
print(msj)
print("-----------------------")