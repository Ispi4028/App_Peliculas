import json
from modelo.pelicula import Pelicula

def cargar_catalogo_desde_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return [Pelicula(**entry) for entry in data]

def buscar_peliculas_por_titulo(catalogo, titulo):
    return [pelicula for pelicula in catalogo
            if titulo.lower() in pelicula.name.lower()]

def buscar_peliculas_por_actores(catalogo, actor1, actor2):
    return [pelicula for pelicula in catalogo
            if any(actor.name == actor1
                   for actor in pelicula.actors) and any(actor.name == actor2
                                                         for actor in pelicula.actors)]

def obtener_actores_unicos(catalogo):
    actores = set()
    for pelicula in catalogo:
        for actor in pelicula.actors:
            actores.add(actor.name)
    return list(actores)