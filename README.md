# TSPV2

Proyecto que contiene la segunda versión del TSP.

## Objetivo general

Desarrollar una solución modular con componentes de **backend** y **frontend** que permita explorar el problema del viajante.

## Instalación de dependencias

1. Clona este repositorio.
2. Desde la raíz, instala las dependencias de cada módulo:
   ```bash
   cd backend
   # instala dependencias del backend (por ejemplo, con npm o pip)
   cd ../frontend
   # instala dependencias del frontend (por ejemplo, con npm)
   ```

## Ejecución del servidor backend

1. Crea un entorno virtual en la carpeta `backend` y activa el entorno:
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install flask ortools
   ```
3. Inicia el servidor:
   ```bash
   python app.py
   ```

La API expone la ruta `/api/solve`, la cual recibe un JSON con un arreglo `coordinates` y devuelve la secuencia óptima calculada.
