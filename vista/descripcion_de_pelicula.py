from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QIcon

class DescripcionPelicula(QDialog):
    def __init__(self, pelicula):
        super().__init__()
        self.setWindowTitle("Cinema --> Detalles de la Película")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon("recursos/img/icono_cinema.png"))
        self.setStyleSheet("""
            QDialog {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #4E4E4E, stop:1 #1A1A1A); 
                color: #FFC107; 
                border-radius: 10px;
            }
            QLabel {
                font-size: 14px;
                margin: 5px;
                color: #FFC107;
            }
            QPushButton {
                background-color: #FFC107; 
                color: #000;
                border: none;
                font: bold 14px;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FFB700;
            }
            QPushButton:pressed {
                background-color: #FF9800;
                border-style: inset; 
            }
        """)
        __detalles = pelicula.mostrar_detalles()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Nombre: {__detalles['titulo']}"))
        layout.addWidget(QLabel(f"Descripción: {__detalles['descripcion']}"))
        layout.addWidget(QLabel(f"Categoría: {__detalles['categoria']}"))
        layout.addWidget(QLabel(f"Estudio: {__detalles['estudio']}"))
        layout.addWidget(QLabel(f"Calificación: {__detalles['calificacion']}"))
        layout.addWidget(QLabel(f"Año: {__detalles['anio']}"))
        layout.addWidget(QLabel(f"Actores: {', '.join(__detalles['actores'])}"))
        layout.addWidget(QLabel(f"Escritores: {', '.join(__detalles['escritores'])}"))
        portada_label = QLabel()
        portada_label.setText(f"Portada: <a href='{__detalles['portada']}' style='color: #FFC107;'>Ver Imagen en el Navegador</a>")
        portada_label.setOpenExternalLinks(True)
        layout.addWidget(portada_label)
        btn_atras = QPushButton("Atrás")
        btn_atras.clicked.connect(self.close)
        layout.addWidget(btn_atras)
        self.setLayout(layout)
