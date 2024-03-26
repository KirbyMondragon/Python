import requests

url = 'https://www.unam.mx/'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    with open('unam.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("HTML de la página UNAM.mx extraído correctamente.")
else:
    print("Error al obtener la página. Código de estado:", response.status_code)
