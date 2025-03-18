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
            "titulo": self.__titulo or 'Desconocido',
            "descripcion": self.__descripcion or 'Sin descripción',
            "categoria": self.__categoria or 'Desconocido',
            "estudio": self.__estudio or 'Desconocido',
            "calificacion": self.__calificacion or '0.0',
            "portada": self.__portada or '',
            "actores": self.__actores or ['Desconocido'],
            "escritores": self.__escritores or ['Desconocido'],
            "anio": self.__anio or 'Desconocido'
        }
