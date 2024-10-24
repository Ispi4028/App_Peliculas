import sys
from PySide6.QtWidgets import QApplication
from App_Peliculas.vista.ventana_cinema import Ventanana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Ventanana()
    main_window.show()
    sys.exit(app.exec())