from App_Peliculas.controlador.gestor_catalogo import GestorCatalogo

class GestorPeliculas:
    def __init__(self, ruta_catalogo):
        self.__gestor_catalogo = GestorCatalogo(ruta_catalogo)
        self.__catalogo = self.__gestor_catalogo.obtener_catalogo()
        self.__actores_unicos = self.obtener_actores()

    def buscar_por_titulo(self, titulo):
        return [
            pelicula
            for pelicula in self.__catalogo
            if titulo.lower() in pelicula.mostrar_detalles()["titulo"].lower()
        ]

    def buscar_por_actores(self, actor1, actor2):
        return [
            pelicula
            for pelicula in self.__catalogo
            if any(actor == actor1 for actor in pelicula.mostrar_detalles()["actores"])
            and any(actor == actor2 for actor in pelicula.mostrar_detalles()["actores"])
        ]

    def obtener_actores(self):
        actores = set()
        for pelicula in self.__catalogo:
            for actor in pelicula.mostrar_detalles()["actores"]:
                actores.add(actor)
        return list(actores)

    def obtener_catalogo(self):
        return self.__catalogo
