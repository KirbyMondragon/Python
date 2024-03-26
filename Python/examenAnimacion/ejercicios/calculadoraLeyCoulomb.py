nombres_Integrantes =["Kevin Arturo", "Fresco Kirby"]
VACIO = 9 * 10**9
print("Calculadora de Ley de Coulomb")

carga_Electrica1 = float(input("¿Cual es el valor de tu carga 1?"))
carga_Electrica2 =float(input("¿Cual es el valor de tu carga 2?"))

radio =float(input("¿Cual es el valor de tu radio?"))

fuerza=float((VACIO)*(carga_Electrica1 * carga_Electrica2)/(radio** 2))

print("El valor de su fuerza es: ", fuerza, "N")