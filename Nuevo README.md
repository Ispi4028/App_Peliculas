# Instrucciones para el Compilado del Archivo .ui

Para asegurarse de que todos los recursos se carguen correctamente en la aplicación, debes seguir estos pasos:

## Paso 1: Incluir recursos_rc en el compilado del .ui

En el compilado que se genere del archivo `.ui` (llamese 'windows', para evitar incompatibilidad), añade la siguiente línea al archivo:

```python
from App_Peliculas.recursos.img import recursos_rc
```

## Paso 2: Compilar el .qrc dentro de /recursos/img

Generar un compilado de recursos.qrc (llamese recursos_rc para tener continuidad). debe de compilarse dentro del directorio 'img' para que sea exitosa la compilación

## Comandos para compilar el .ui y .qrc

```bash
pyside6-uic windows.ui -o windows.py 
pyside6-rcc -o recursos.qrc recursos.py 
```
