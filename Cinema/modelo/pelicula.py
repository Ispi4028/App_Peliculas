from modelo.actor import Actor

class Pelicula:
    def __init__(self, name, description, category, studio, rating, img, actors, writers, year):
        self.__name = name
        self.__description = description
        self.__category = category
        self.__studio = studio
        self.__rating = rating
        self.__img = img
        self.__actors = [Actor(actor) for actor in actors]
        self.__writers = writers
        self.__year = year

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