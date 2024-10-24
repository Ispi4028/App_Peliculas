class Pelicula:
    def __init__(self, titulo, descripcion, categoria, estudio, calificacion, portada, actores, escritores, anio):
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__categoria = categoria
        self.__estudio = estudio
        self.__calificacion = calificacion
        self.__portada = portada
        self.__actores = actores
        self.__escritores = escritores
        self.__anio = anio

    def mostrar_detalles(self):
        return {
            "titulo": self.__titulo,
            "descripcion": self.__descripcion,
            "categoria": self.__categoria,
            "estudio": self.__estudio,
            "calificacion": self.__calificacion,
            "portada": self.__portada,
            "actores": self.__actores,
            "escritores": self.__escritores,
            "anio": self.__anio
        }
