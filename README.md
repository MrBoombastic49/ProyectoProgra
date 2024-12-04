Proyecto Final: Análisis de Laptops en Mercado Libre

## Descripción del Proyecto

Este proyecto tiene como objetivo el análisis de los precios, las características técnicas y las calificaciones de laptops disponibles en la plataforma de Mercado Libre. A través de un proceso de **Web Scraping**, se recolectan datos como títulos, precios, calificaciones, descuentos, número de reseñas y colores disponibles. Luego, estos datos son limpiados y procesados para ser visualizados en **dashboards interactivos** que permiten explorar las tendencias del mercado, comparar productos y tomar decisiones informadas de compra.

## Objetivo

- **Analizar los rangos de precios de laptops**: Identificar las tendencias de precios según marcas y especificaciones técnicas como almacenamiento y memoria RAM.
- **Evaluar la relación entre precio y calificación**: Visualizar cómo las calificaciones de los usuarios se relacionan con el precio de los productos.
- **Explorar las calificaciones promedio**: Analizar el promedio de calificación otorgada por los usuarios para los principales productos.

## Preguntas a Resolver

1. ¿Cuáles son los rangos de precios más comunes para las laptops según su marca y especificaciones técnicas?
2. ¿Cómo varían los precios de las laptops según su capacidad de almacenamiento y memoria RAM?
3. ¿Qué relación existe entre el precio promedio y las valoraciones de los productos por parte de los usuarios?

## Estructura del Proyecto

Este proyecto está dividido en varios scripts y módulos que realizan tareas específicas:

- **`ConexionSql.py`**: Maneja la conexión a la base de datos MySQL donde se almacenan los datos de los productos.
- **`Limpieza.py`**: Realiza la limpieza y el preprocesamiento de los datos recolectados para convertirlos en un formato adecuado para su análisis.
- **`dash1.py`**: Implementa el primer dashboard interactivo que muestra la distribución de precios y la relación entre precios actuales y anteriores.
- **`dash2.py`**: Visualiza un gráfico interactivo para explorar las calificaciones y descuentos de los productos.
- **`dash3.py`**: Muestra el promedio de calificación de los productos más populares.
- **`dashboard.py`**: El archivo principal donde se configura el layout y la navegación entre los diferentes dashboards.
- **`welcome.py`**: Presenta la introducción al proyecto y las preguntas a resolver.

## Herramientas y Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal utilizado para realizar el web scraping, el procesamiento de datos y la visualización.
- **Dash**: Framework para crear aplicaciones web interactivas en Python.
- **Plotly**: Biblioteca para crear gráficos interactivos.
- **Pandas**: Utilizado para manipular y procesar los datos.
- **SQLAlchemy y MySQL**: Para la conexión y manejo de la base de datos MySQL.
- **BeautifulSoup y Selenium**: Herramientas para el web scraping de los productos en Mercado Libre.

## Instrucciones para Ejecutar

### Instalación de Dependencias

1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```
4. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución del Proyecto

1. Ejecuta el script `dashboard.py` para iniciar la aplicación Dash:
   ```bash
   python dashboard.py
   ```
2. Abre tu navegador y visita `http://127.0.0.1:8050` para interactuar con los dashboards.

## Archivos Principales

### `ConexionSql.py`

Este archivo maneja la conexión a la base de datos MySQL y permite cargar los datos de productos en el DataFrame.

### `Limpieza.py`

Este archivo limpia los datos recolectados, eliminando caracteres especiales, convirtiendo tipos de datos y gestionando valores faltantes.

### `dash1.py`, `dash2.py`, `dash3.py`

Cada uno de estos archivos define un **dashboard interactivo** que permite visualizar distintas métricas sobre los productos (precios, calificaciones, descuentos, etc.).

### `dashboard.py`

El archivo principal que configura la aplicación Dash, la barra de navegación y permite cambiar entre diferentes dashboards.

### `welcome.py`

Este archivo muestra una introducción al proyecto y las preguntas a resolver.

## Resultados Esperados

- **Dashboard 1**: Distribución de precios de laptops y comparación entre precios actuales y anteriores.
- **Dashboard 2**: Relación entre descuentos y calificaciones de productos.
- **Dashboard 3**: Promedio de calificación de los productos más populares.

## Contribuciones

- **Kristhof Arana Palafox** - <k1297909@uabc.edu.mx>
- **Aaron Fernandez Pinto Lopez** - <fernandeza38@uabc.edu.mx>
- **Frida Marisa Lopez Galaviz** - <frida.lopez40@uabc.edu.mx>
- **Jesus Alexis Peralta Alarcon** - <jesus.peralta@uabc.edu.mx>
