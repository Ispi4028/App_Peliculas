from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap, QIcon

class VentanaEmergentePelicula(QDialog):
    def __init__(self, pelicula):
        super().__init__()
        self.setWindowTitle("Cinema-->Detalles de la Película")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon("recursos/img/icono_cinema.png"))

        self.setStyleSheet("""
            QDialog {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #4E4E4E, stop:1 #1A1A1A); /* Fondo degradado igual al de la ventana principal */
                color: #FFC107; /* Texto dorado */
                border-radius: 10px;
            }
            QLabel {
                font-size: 14px;
                margin: 5px;
                color: #FFC107; /* Texto dorado */
            }
            QPushButton {
                background-color: #FFC107; /* Fondo dorado */
                color: #000;
                border: none;
                font: bold 14px;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FFB700; /* Color más oscuro al pasar el ratón */
            }
            QPushButton:pressed {
                background-color: #FF9800; /* Color más oscuro al presionar */
                border-style: inset; 
            }
        """)

        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"Nombre: {pelicula.name}"))
        layout.addWidget(QLabel(f"Descripción: {pelicula.description}"))
        layout.addWidget(QLabel(f"Categoría: {pelicula.category}"))
        layout.addWidget(QLabel(f"Estudio: {pelicula.studio}"))
        layout.addWidget(QLabel(f"Rating: {pelicula.rating}"))
        layout.addWidget(QLabel(f"Año: {pelicula.year}"))
        layout.addWidget(QLabel(f"Actores: {', '.join(actor.name for actor in pelicula.actors)}"))
        layout.addWidget(QLabel(f"Escritores: {', '.join(pelicula.writers)}"))

        portada_label = QLabel()
        portada_label.setText(f"Portada: <a href='{pelicula.img}' style='color: #FFC107;'>Ver Imagen en el Navegador</a>")
        portada_label.setOpenExternalLinks(True)
        layout.addWidget(portada_label)

        btn_close = QPushButton("Atrás")
        btn_close.clicked.connect(self.close)
        layout.addWidget(btn_close)

        self.setLayout(layout)
