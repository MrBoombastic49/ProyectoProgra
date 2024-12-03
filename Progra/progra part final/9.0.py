import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

# Función para realizar el web scraping
def obtener_datos_mercadolibre(paginas):
    # Configuración del navegador
    s = Service(ChromeDriverManager().install())
    opciones = Options()
    opciones.add_argument("--window-size=1024,1200")
    navegador = webdriver.Chrome(service=s, options=opciones)

    # Ir a la página de listado de laptops
    url = "https://listado.mercadolibre.com.mx/laptops"
    navegador.get(url)
    time.sleep(5)

    # Inicialización de datos
    datos = {"titulo": [], "precio": [], "precio_anterior": [], "descuento": [], "calificacion": [], "num_reviews": [], "colores_disponibles": []}

    for pagina in range(paginas):
        time.sleep(3)

        # Hacer scroll hacia abajo para cargar más contenido
        navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        # Espera explícita para asegurarse de que los productos se han cargado
        try:
            WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ui-search-result__wrapper"))
            )
        except:
            print(f"Error al cargar la página {pagina + 1}.")
            break

        # Obtener el HTML de la página actual
        soup = BeautifulSoup(navegador.page_source, 'html.parser')

        # Buscar los elementos de producto
        productos = soup.find_all("div", class_="poly-card poly-card--list")
        print(f"Productos encontrados en la página {pagina + 1}: {len(productos)}")

        for producto in productos:
            # Extraer título y precio de cada producto
            titulo = "N/A"
            precio = "N/A"
            precio_anterior = "N/A"
            descuento = "N/A"
            calificacion = "N/A"
            num_reviews = "N/A"
            colores_disponibles = "N/A"

            # Extraer título
            titulo_container = producto.find("h2", class_="poly-box poly-component__title")
            if titulo_container:
                titulo = titulo_container.find("a").text

            # Extraer precio anterior (el precio tachado)
            precio_anterior_container = producto.find("span", class_="andes-money-amount__fraction")
            if precio_anterior_container:
                precio_anterior = precio_anterior_container.text.strip()

            # Extraer precio actual (el precio visible)
            precio_container = producto.find("span", class_="andes-money-amount andes-money-amount--cents-superscript")
            if precio_container:
                precio = precio_container.text.strip()

            # Extraer descuento
            descuento_container = producto.find("span", class_="andes-money-amount__discount")
            if descuento_container:
                descuento = descuento_container.text.strip().replace(" OFF", "")  # Eliminamos el "OFF" del texto

            # Extraer calificación
            calificacion_container = producto.find("span", class_="poly-reviews__rating")
            if calificacion_container:
                calificacion = calificacion_container.text.strip()

            # Extraer número de reseñas
            num_reviews_container = producto.find("span", class_="poly-reviews__total")
            if num_reviews_container:
                num_reviews = num_reviews_container.text.strip()
            else:
                num_reviews = "N/A"  # Si no se encuentra el número de reseñas, asignar "N/A"

            # Extraer colores disponibles
            colores_disponibles_container = producto.find("span", class_="poly-component__variations-text")
            if colores_disponibles_container:
                colores_disponibles = colores_disponibles_container.text.strip().split()[-2]

            # Añadir los datos al diccionario
            datos["titulo"].append(titulo)
            datos["precio"].append(precio)
            datos["precio_anterior"].append(precio_anterior)
            datos["descuento"].append(descuento)
            datos["calificacion"].append(calificacion)
            datos["num_reviews"].append(num_reviews)
            datos["colores_disponibles"].append(colores_disponibles)

        # Intentar hacer clic en el botón de 'Siguiente' para avanzar de página
        try:
            # Asegurarse de que el botón siguiente esté visible y se pueda hacer clic
            WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@title='Siguiente']"))
            )
            boton_siguiente = navegador.find_element(By.XPATH, "//a[@title='Siguiente']")
            siguiente_url = boton_siguiente.get_attribute("href")  # Obtener la URL del siguiente enlace
            navegador.get(siguiente_url)  # Navegar a la siguiente página
            time.sleep(3)
        except:
            print("No se encontró el botón de 'Siguiente'. Fin del scraping.")
            break

    # Cerrar navegador
    navegador.quit()

    # Verificar y guardar datos
    if datos["titulo"] and datos["precio"]:
        df = pd.DataFrame(datos)

        # Guardar el archivo CSV sucio (sin limpiar aún)
        df.to_csv("C:/Users/aaron/PycharmProjects/ProyectoFinal/Datasets/productos_mercadolibre_sucio.csv", index=False)
        print("Datos guardados en productos_mercadolibre_sucio.csv")
    else:
        print("No se encontraron datos para guardar.")

# Ejecutar el scraping y almacenar los datos en un CSV sucio
obtener_datos_mercadolibre(6)
