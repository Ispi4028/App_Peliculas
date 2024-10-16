from modelo.actor import Actor

class Pelicula:
    def __init__(self, name=None, description=None, category=None, studio=None, rating=None, img=None, actors=None, writers=None, year=None):
        self.__name = name or "Desconocido"
        self.__description = description or "Sin descripción"
        self.__category = category or "Desconocido"
        self.__studio = studio or "Desconocido"
        self.__rating = rating or "0.0"
        self.__img = img or ""
        self.__actors = [Actor(actor) for actor in actors] if actors else []
        self.__writers = writers if writers else []
        self.__year = year or "Desconocido"

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def category(self):
        return self.__category

    @property
    def studio(self):
        return self.__studio

    @property
    def rating(self):
        return self.__rating

    @property
    def img(self):
        return self.__img

    @property
    def actors(self):
        return self.__actors

    @property
    def writers(self):
        return self.__writers

    @property
    def year(self):
        return self.__year
