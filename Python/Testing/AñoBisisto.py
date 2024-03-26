from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option('detach', True)
chrm_driver = webdriver.Chrome(options=options)
chrm_driver.get("https://www.ge.com/contact/general")

# Create object for Select class


dd1 = Select(chrm_driver.find_element(By.ID, "edit-relationship-to-ge"))
# by index start with 0
dd1.select_by_index(5)


dd2 =  Select(chrm_driver.find_element(By.ID, "edit-subject"))

dd2.select_by_index(2)


dd3 =  Select(chrm_driver.find_element(By.ID, "edit-area-of-interest-careers"))

dd3.select_by_index(2)


# Value = value propertyid=""
#dd1.select_by_value("Investor")

# Text visible in the options
#dd1.select_by_visible_text("Employee")
while True:
    try:
        boton1 = int(input("Ingrese el boton a revisar: "))
        dd1 = Select(chrm_driver.find_element(By.ID, "edit-relationship-to-ge"))
        # by index start with 0
        
        dd1.select_by_index(boton1)
        for i in range(cantidad):
            while True:
                try:
                    año = int(input("Ingrese el año: "))
                    bisiesto = False

                    if (año % 400 == 0) or (año % 100 != 0 and año % 4 == 0):
                        bisiesto = True

                    if bisiesto:
                        print(f"El año {año} es bisiesto.")
                    else:
                        print(f"El año {año} no es bisiesto.")
                    break  # Rompe el bucle interior si se ingresa un número válido

                except ValueError:
                    print("Eso no es un número válido. Intente de nuevo.")

        break  # Rompe el bucle exterior una vez que se han procesado todos los años

    except ValueError:
        print("Eso no es un número. Intente de nuevo.")