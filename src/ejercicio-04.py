"""
Data Engineering Test
Solvex - 2024
Resuelto por Santiago Taracena Puga
Ejercicio 4 - Web Scraping con Requests
"""

# Librerías necesarias para el ejercicio
import requests
from bs4 import BeautifulSoup

# URL de la página de CoinMarketCap
url = "https://coinmarketcap.com/currencies/bitcoin/"

# Solicitud GET para obtener el contenido de la página
response = requests.get(url)

# Verificación de la solicitud exitosa (código de respuesta 200)
if (response.status_code == 200):

    # Instancia de BeautifulSoup para hacer scrapping
    soup = BeautifulSoup(response.text, "html.parser")

    # Span con clases "sc-f70bb44c-0 jxpCgO base-text", que contiene el precio buscado
    price_tag = soup.find("span", class_="sc-f70bb44c-0 jxpCgO base-text")

    # Código a ejecutar si se encontró el precio
    if (price_tag):

        # Extracción del precio del elemento y almacenamiento en una variable
        price = price_tag.text
        print(f"\nEl precio actual de Bitcoin es: {price}\n")

    # Código a ejecutar si no se encontró el precio
    else:
        print("\nNo se pudo encontrar el precio de Bitcoin en la página.\n")

# Código a ejecutar si la solicitud no fue exitosa
else:
    print(f"\nError al hacer la solicitud. Código de respuesta: {response.status_code}\n")
