import json
from modelo.pelicula import Pelicula

def cargar_catalogo_desde_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            datos = json.load(file)
        catalogo = []
        for entrada in datos:
            try:
                pelicula = Pelicula(**entrada)
                catalogo.append(pelicula)
            except TypeError as e:
                print(f"Error en el formato del dato: {entrada}, Error: {e}")
        return catalogo
    except FileNotFoundError as e:
        print(f"Archivo no encontrado: {file_path}, Error: {e}")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar el JSON: {file_path}, Error: {e}")
    return []


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