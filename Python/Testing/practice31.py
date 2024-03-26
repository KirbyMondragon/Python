from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

def case_1():
    options = Options()
    options.add_experimental_option('detach', True)
    chrm_driver = webdriver.Chrome(options=options)
    chrm_driver.get("https://www.ge.com/contact/general")
    options.add_experimental_option('detach', True)

    # Create object for Select class


    dd1 = Select(chrm_driver.find_element(By.ID, "edit-relationship-to-ge"))
    # by index start with 0
    dd1.select_by_index(boton1)

    for i in range(9):
        dd2 =  Select(chrm_driver.find_element(By.ID, "edit-subject"))
        dd2.select_by_index(i)
        
        dd3 =  Select(chrm_driver.find_element(By.ID, "edit-area-of-interest-careers"))
        dd3.select_by_index(1)



def case_2():
    options = Options()
    options.add_experimental_option('detach', True)
    chrm_driver = webdriver.Chrome(options=options)
    chrm_driver.get("https://www.ge.com/contact/general")

    # Create object for Select class


    dd1 = Select(chrm_driver.find_element(By.ID, "edit-relationship-to-ge"))
    # by index start with 0
    dd1.select_by_index(boton1)

    
    chrm_driver.find_element(By.ID, "edit-email-address").send_keys("kevinmondragon@gmail.com")
    chrm_driver.find_element(By.ID, "edit-comments-or-questions").send_keys("This is cool, I like it")

def case_3():
    options = Options()
    options.add_experimental_option('detach', True)
    chrm_driver = webdriver.Chrome(options=options)
    chrm_driver.get("https://www.ge.com/contact/general")

    # Create object for Select class


    dd1 = Select(chrm_driver.find_element(By.ID, "edit-relationship-to-ge"))
    # by index start with 0
    dd1.select_by_index(7)

    for i in range(3):
        dd2 =  Select(chrm_driver.find_element(By.ID, "edit-subject"))

        dd2.select_by_index(i)

    dd3 =  Select(chrm_driver.find_element(By.ID, "edit-area-of-interest-careers"))

    dd3.select_by_index(1)

    
    chrm_driver.find_element(By.ID, "edit-email-address2").send_keys("kevinmondragon@gmail.com")
    chrm_driver.find_element(By.ID, "edit-comments-or-questions").send_keys("This is cool, I like it")


def default_case():
    return "Opción no válida"

def switch(case_number):
    switcher = {
        1: case_1,
        2: case_2,
        3: case_3
    }
    # El método get del diccionario devuelve el valor para el caso dado,
    # o default_case si el caso no está en el diccionario.
    return switcher.get(case_number, default_case)()


boton1 = int(input("Ingrese el boton a revisar: "))
# Prueba de la función switch
print(switch(boton1))  # Debería imprimir: Seleccionaste la opción 1

