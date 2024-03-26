import math
def areacirculo(radio):
    pi = math.pi
    resultado = (pi*(radio**2))
    return resultado



radio =int(input("Tell me your radio: "))
print(radio)
print(areacirculo(radio))

