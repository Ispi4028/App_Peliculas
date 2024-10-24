# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windows.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QWidget)
from recursos.img import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 502)
        icon = QIcon()
        icon.addFile(u":/pestania/icono_cinema.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #4E4E4E, stop:1 #1A1A1A);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #4E4E4E, stop:1 #1A1A1A); \n"
"    border-radius: 10px; \n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"    width: 0;\n"
"    height: 0;\n"
"    margin: 0;\n"
"    padding: 0;\n"
"    border: none;\n"
"}\n"
"")
        self.pestania = QWidget()
        self.pestania.setObjectName(u"pestania")
        self.gridLayout = QGridLayout(self.pestania)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.barra_de_busqueda = QLineEdit(self.pestania)
        self.barra_de_busqueda.setObjectName(u"barra_de_busqueda")
        self.barra_de_busqueda.setMaximumSize(QSize(363, 16777215))
        self.barra_de_busqueda.setStyleSheet(u"QLineEdit {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FFC107, stop:1 #FF9800); \n"
"    color: #000;\n"
"    border: 1px solid #FFC107;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.barra_de_busqueda)

        self.boton_buscar_por_descripcion = QPushButton(self.pestania)
        self.boton_buscar_por_descripcion.setObjectName(u"boton_buscar_por_descripcion")
        self.boton_buscar_por_descripcion.setStyleSheet(u"QPushButton {\n"
"    width: 50px; \n"
"    height: 11px; \n"
"    border-radius: 5px; \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FFC107, stop:1 #FF9800); \n"
"    border: 1px solid #FFC107;\n"
"    font: bold 14px;\n"
"    padding: 10px;\n"
"    box-shadow: 2px 2px 5px #555; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FF9800, stop:1 #FFC107); \n"
"    border-style: inset;\n"
"    border-radius: 5px; \n"
"    outline: none; \n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.boton_buscar_por_descripcion, 0, Qt.AlignLeft)

        self.boton_cambiar_pestania1 = QPushButton(self.pestania)
        self.boton_cambiar_pestania1.setObjectName(u"boton_cambiar_pestania1")
        self.boton_cambiar_pestania1.setEnabled(True)
        self.boton_cambiar_pestania1.setStyleSheet(u"QPushButton {\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset; \n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/pestania/derecha.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_cambiar_pestania1.setIcon(icon1)
        self.boton_cambiar_pestania1.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.boton_cambiar_pestania1, 0, Qt.AlignRight|Qt.AlignTop)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.lista_de_peliculas1 = QListWidget(self.pestania)
        self.lista_de_peliculas1.setObjectName(u"lista_de_peliculas1")
        self.lista_de_peliculas1.setStyleSheet(u"QListWidget {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #4E4E4E, stop:1 #1A1A1A); \n"
"    border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FFD700, stop:1 #FFB700); \n"
"    border-radius: 15px; \n"
"    color: #FFFFFF; \n"
"    font: 12px \"Arial\";\n"
"    padding: 10px; \n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 10px;\n"
"    border: 1px solid #4E4E4E; \n"
"    border-radius: 10px; \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #4E4E4E, stop:1 #1A1A1A); \n"
"    color: #FFFFFF; \n"
"    margin: 1px; \n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FFC107, stop:1 #FF9800);\n"
"    color: #000; \n"
"    border-radius: 10px; \n"
"}\n"
"")

        self.gridLayout.addWidget(self.lista_de_peliculas1, 1, 0, 1, 1)

        self.tabWidget.addTab(self.pestania, "")
        self.pestania2 = QWidget()
        self.pestania2.setObjectName(u"pestania2")
        self.gridLayout_3 = QGridLayout(self.pestania2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.actor = QLineEdit(self.pestania2)
        self.actor.setObjectName(u"actor")
        self.actor.setMaximumSize(QSize(152, 16777215))
        self.actor.setStyleSheet(u"QLineEdit {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FFC107, stop:1 #FF9800); \n"
"    color: #000;\n"
"    border: 1px solid #FFC107;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.actor, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.actor2 = QLineEdit(self.pestania2)
        self.actor2.setObjectName(u"actor2")
        self.actor2.setMaximumSize(QSize(151, 16777215))
        self.actor2.setStyleSheet(u"QLineEdit {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FFC107, stop:1 #FF9800); \n"
"    color: #000;\n"
"    border: 1px solid #FFC107;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.actor2, 0, Qt.AlignLeft)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.boton_buscar_por_actores = QPushButton(self.pestania2)
        self.boton_buscar_por_actores.setObjectName(u"boton_buscar_por_actores")
        self.boton_buscar_por_actores.setMaximumSize(QSize(72, 16777215))
        self.boton_buscar_por_actores.setStyleSheet(u"QPushButton {\n"
"    width: 50px; \n"
"    height: 11px; \n"
"    border-radius: 5px; \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FFC107, stop:1 #FF9800); \n"
"    border: 1px solid #FFC107;\n"
"    font: bold 14px;\n"
"    padding: 10px;\n"
"    box-shadow: 2px 2px 5px #555; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FF9800, stop:1 #FFC107); \n"
"    border-style: inset;\n"
"    border-radius: 5px; \n"
"    outline: none; \n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.boton_buscar_por_actores, 0, Qt.AlignLeft)

        self.boton_cambiar_pestania2 = QPushButton(self.pestania2)
        self.boton_cambiar_pestania2.setObjectName(u"boton_cambiar_pestania2")
        self.boton_cambiar_pestania2.setStyleSheet(u"QPushButton {\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset; \n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/pestania/izquierda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_cambiar_pestania2.setIcon(icon2)
        self.boton_cambiar_pestania2.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.boton_cambiar_pestania2, 0, Qt.AlignRight|Qt.AlignTop)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.lista_de_peliculas_actores = QListWidget(self.pestania2)
        self.lista_de_peliculas_actores.setObjectName(u"lista_de_peliculas_actores")
        self.lista_de_peliculas_actores.setStyleSheet(u"QListWidget {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #4E4E4E, stop:1 #1A1A1A); \n"
"    border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FFD700, stop:1 #FFB700); \n"
"    border-radius: 15px; \n"
"    color: #FFFFFF; \n"
"    font: 12px \"Arial\";\n"
"    padding: 10px; \n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 10px;\n"
"    border: 1px solid #4E4E4E; \n"
"    border-radius: 10px; \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #4E4E4E, stop:1 #1A1A1A); \n"
"    color: #FFFFFF; \n"
"    margin: 1px; \n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FFC107, stop:1 #FF9800);\n"
"    color: #000; \n"
"    border-radius: 10px; \n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.lista_de_peliculas_actores, 1, 0, 1, 1)

        self.tabWidget.addTab(self.pestania2, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 550, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cinema", None))
#if QT_CONFIG(accessibility)
        self.barra_de_busqueda.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.barra_de_busqueda.setText("")
        self.barra_de_busqueda.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por titulo", None))
        self.boton_buscar_por_descripcion.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
#if QT_CONFIG(statustip)
        self.boton_cambiar_pestania1.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.boton_cambiar_pestania1.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.boton_cambiar_pestania1.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pestania), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.actor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Actor1", None))
        self.actor2.setText("")
        self.actor2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Actor2", None))
        self.boton_buscar_por_actores.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.boton_cambiar_pestania2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pestania2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

