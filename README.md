# Práctica 2 - Python 2026
 Andres Sales - 018505/2

## Estructura del proyecto
- `notebooks/` → Notebooks con la resolucion de los ejercicios
- `src/` → Archivos `.py` con las funciones
- `venv/` → Entorno virtual (no se sube a GitHub)
- `requirements.txt` → Dependencias del proyecto

## Requisitos
- Python 3.13.12
- Visual Studio Code + extensiones **Python** y **Jupyter**

## Instalación y ejecución

1. Clonar o descargar el repositorio.
   ```bash
   git clone https://github.com/andresmaxi33/Python-Practica-2.git
   cd Python-Practica-2
2. Crear y activar el entorno virtual (solo la primera vez):
   ```bash
   python -m venv venv
   venv\Scripts\activate  <---(windows)
   source venv/bin/activate  <----(mac/linux)
4. Instalar las dependencias
pip install -r requirements.txt

## Configuración de Git

Este repositorio utiliza el archivo `.gitattributes` junto con la herramienta `nbstripout` para **limpiar automáticamente** los outputs y metadatos de los notebooks (`.ipynb`) antes de hacer commit.

Esto hace que los archivos `.ipynb` sean mucho más livianos y evita que aparezcan cambios innecesarios en Git.

**El archivo `.gitattributes` debe permanecer visible** en el repositorio, ya que es parte de la configuración del proyecto.

## Cómo ejecutar los ejercicios (paso a paso)

1. Abri la carpeta `Practica_2` en Visual Studio Code.
2. CTRL + SHIFT + P, hace clic donde dice el interprete de Python y selecciona:
   - `Python 3.13.12 ('venv': venv)` (o `./venv/Scripts/python.exe`)
3. Abri la carpeta `notebooks/`.
4. Abri cualquiera de los archivos `.ipynb` (ej: `ejercicio7.ipynb`).
5. Hacelo clic en **Ejecutar todo**.

 El notebook deberia ejecutarse sin errores.