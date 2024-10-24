from App_Peliculas.modelo.pelicula import Pelicula
import json

class GestorCatalogo:
    def __init__(self, ruta_archivo):
        self.__ruta_archivo = ruta_archivo
        self.__catalogo = self.cargar_catalogo_desde_json()

    def cargar_catalogo_desde_json(self):
        try:
            with open(self.__ruta_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
            catalogo = []
            for entrada in datos:
                try:
                    actores = [actor for actor in entrada.get('actores', [])]
                    escritores = entrada.get('escritores', [])
                    pelicula = Pelicula(
                        titulo=entrada.get('titulo', 'Desconocido'),
                        descripcion=entrada.get('descripcion', 'Sin descripción'),
                        categoria=entrada.get('categoria', 'Desconocido'),
                        estudio=entrada.get('estudio', 'Desconocido'),
                        calificacion=entrada.get('calificacion', '0.0'),
                        portada=entrada.get('portada', ''),
                        actores=actores,
                        escritores=escritores,
                        anio=entrada.get('anio', 'Desconocido')
                    )
                    catalogo.append(pelicula)
                except TypeError as e:
                    print(f"Error en el formato del dato: {entrada}, Error: {e}")
            return catalogo
        except FileNotFoundError as e:
            print(f"Archivo no encontrado: {self.__ruta_archivo}, Error: {e}")
        except json.JSONDecodeError as e:
            print(f"Error al decodificar el JSON: {self.__ruta_archivo}, Error: {e}")
        return []

    def obtener_catalogo(self):
        return self.__catalogo



    def obtener_catalogo(self):
        return self.__catalogo