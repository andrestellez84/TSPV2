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
   pip install flask flask-cors ortools
   ```
3. Inicia el servidor:
   ```bash
   python app.py
   ```

La API expone la ruta `/api/solve`, la cual recibe un JSON con un arreglo `coordinates` y devuelve la secuencia óptima calculada.

## Ejecución del frontend

1. En otra terminal, inicia un servidor estático dentro de la carpeta `frontend`:
   ```bash
   cd frontend
   # usando Python 3
   python -m http.server 8000
   ```
2. Abre `http://localhost:8000` en tu navegador.

## Probar la aplicación

1. Con el backend en funcionamiento, abre la página del frontend.
2. Haz clic en el canvas para agregar ciudades. Verás la lista de coordenadas debajo del lienzo.
3. Pulsa **Mejor Ruta** para enviar las coordenadas al backend.
4. Se dibujará la ruta óptima en el canvas siguiendo el orden devuelto por la API.

## Ejecutar pruebas

Para verificar el funcionamiento del solver se incluye una suite de pruebas basada en `unittest` dentro del directorio `backend/tests`.
Con un entorno virtual activo, ejecuta:

```bash
python -m unittest discover -s backend/tests
```

Esto correrá pruebas sencillas sobre el endpoint `/api/solve`.
