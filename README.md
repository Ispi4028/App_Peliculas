# Instrucciones para el Compilado del Archivo .ui

Para asegurarte de que todos los recursos se carguen correctamente en la aplicación, debes seguir estos pasos:

## Paso 1: Incluir recursos_rc en el compilado del .ui

En el compilado que se genere del archivo `.ui` (llamese 'windows', para evitar incompatibilidad), añade la siguiente línea al archivo:

```python
from recursos.img import recursos_rc
```



## Paso 2: Compilar el .qrc dentro de /recursos/img

Generar un compilado de recursos.qrc (llamese recursos_rc para evitar complicaciones).