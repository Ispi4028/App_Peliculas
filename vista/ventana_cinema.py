from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem, QCompleter
from App_Peliculas.vista.windows import Ui_MainWindow
from App_Peliculas.vista.descripcion_de_pelicula import DescripcionPelicula
from App_Peliculas.controlador.gestor_peliculas import GestorPeliculas

class Ventanana(QMainWindow):
    boton_buscar_por_descripcion = Signal(str)
    boton_buscar_por_actores = Signal(str, str)

    def __init__(self):
        super(Ventanana, self).__init__()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.__controlador = GestorPeliculas('recursos/peliculas.json')
        self.__actores_unicos = self.__controlador.obtener_actores()
        self.__autocompletar(self.__ui.actor, self.__actores_unicos)
        self.__autocompletar(self.__ui.actor2, self.__actores_unicos)
        self.__autocompletar(self.__ui.barra_de_busqueda, [pelicula.mostrar_detalles()["titulo"] for pelicula in self.__controlador.obtener_catalogo()])
        self.__ui.boton_cambiar_pestania1.clicked.connect(self.cambiar_a_pestania2)
        self.__ui.boton_cambiar_pestania2.clicked.connect(self.cambiar_a_pestania1)
        self.__ui.boton_buscar_por_descripcion.clicked.connect(self.enviar_busqueda_por_titulo)
        self.__ui.boton_buscar_por_actores.clicked.connect(self.enviar_busqueda_por_actores)
        self.__ui.tabWidget.setCurrentIndex(0)

    def __autocompletar(self, widget, items):
        completar = QCompleter(items, self)
        completar.setCaseSensitivity(Qt.CaseInsensitive)
        widget.setCompleter(completar)

    def cambiar_a_pestania1(self):
        self.__ui.tabWidget.setCurrentIndex(0)

    def cambiar_a_pestania2(self):
        self.__ui.tabWidget.setCurrentIndex(1)

    def enviar_busqueda_por_titulo(self):
        titulo = self.__ui.barra_de_busqueda.text().strip()
        if not titulo:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un título para buscar.")
            return
        peliculas = self.__controlador.buscar_por_titulo(titulo)
        if peliculas:
            self.mostrar_resultados_peliculas(self.__ui.lista_de_peliculas1, peliculas)
        else:
            QMessageBox.information(self, "Sin Resultados", "No se encontraron películas con ese título.")

    def enviar_busqueda_por_actores(self):
        actor1 = self.__ui.actor.text().strip()
        actor2 = self.__ui.actor2.text().strip()
        if actor1 == actor2:
            QMessageBox.warning(self, "Error", "Por favor, seleccione dos actores diferentes.")
            return
        if not actor1 or not actor2:
            QMessageBox.warning(self, "Error", "Por favor, seleccione dos actores para buscar.")
            return
        peliculas = self.__controlador.buscar_por_actores(actor1, actor2)
        if peliculas:
            self.mostrar_resultados_peliculas(self.__ui.lista_de_peliculas_actores, peliculas)
        else:
            QMessageBox.information(self, "Sin Resultados", "No se encontraron películas con esos actores.")

    def mostrar_resultados_peliculas(self, list_widget, peliculas):
        list_widget.clear()
        for pelicula in peliculas:
            item = QListWidgetItem(pelicula.mostrar_detalles()["titulo"])
            list_widget.addItem(item)
            item.setData(Qt.UserRole, pelicula)
        list_widget.itemDoubleClicked.connect(self.mostrar_detalles_pelicula)

    def mostrar_detalles_pelicula(self, item):
        pelicula = item.data(Qt.UserRole)
        dialog = DescripcionPelicula(pelicula)
        dialog.exec()