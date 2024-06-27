from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QPalette, QColor, QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMenu, QHBoxLayout, QVBoxLayout, QWidget, QTextEdit, \
    QSizePolicy, QFrame, QPushButton

from valores_precargados import ColoresRgb, ColoresHEX


class CajaDeColores(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")

class Color(QLabel):
    def __init__(self, color: tuple):
        '''Recordemos que estamos generando un objeto tipo Label a pesar del nombre'''
        #Esta metodologia es mas engorrosa
        #r = color[0]
        #g = color[1]
        #b = color[2]

        #desempaquetamos los valores rgb
        r, g, b, = color
        super().__init__()
        #Permitimos que se pueda cambiar el background de un componente
        self.setAutoFillBackground(True)
        '''Generamos el color'''
        paleta = self.palette()
        paleta.setColor(QPalette.Window, QColor(r, g, b))
        '''Asignamos el color al label'''
        self.setPalette(paleta)

class CajaDeTexto(QTextEdit):
    def __init__(self):
        super().__init__()
        r, g, b = ColoresRgb.COLOR10
        self.setStyleSheet(f"background-color: rgb({r},{g},{b});"
                           f"border-radius: 5%")



        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.setMaximumSize(1000, 800)
        #self.resize(500, 300)

    def borrado(self):
        pass
    def guardar(self):
        pass
    def guardar_como(self):
        pass

class EtiquetaStilo1(QLabel):
    def __init__(self, texto, alinecion, fuente_text, color_etiqueta):
        super().__init__()
        #color de la estiqueta
        r, g, b = color_etiqueta
        self.setStyleSheet(f"background-color: rgb({r},{g},{b});"
                           f"border-radius: 20%")

        #Texto de la Etiqueta
        self.setText(texto)
        #Propiedades del Texto
        self.setFont(QFont(fuente_text, 20))

        def valida_alineacion(tipo):
            if tipo == "CENTER":
                return self.setAlignment(Qt.AlignCenter)
            elif tipo == "IZQ":
                return self.setAlignment(Qt.AlignLeft)
            elif tipo == "JUSTIFICADO":
                return self.setAlignment(Qt.AlignJustify)
            else:
                return self.setAlignment(Qt.AlignRight)
        valida_alineacion(alinecion)

class FramePantalla(QFrame):
    def __init__(self, css_aplicar):
        super().__init__()
        #Estilo del frame
        self.setStyleSheet(css_aplicar)


class BotonDcho(QPushButton):
    def __init__(self, texto_boton):
        super().__init__()
        R1, G1, B1, = ColoresRgb.COLOR1
        R2, G2, B2, = ColoresRgb.COLOR8
        R3, G3, B3, = ColoresRgb.COLOR3
        self.setStyleSheet(f"border-style: solid;"
                           f"border-width: 3px;"
                           f"border-color: {ColoresHEX.COLOR7};"
                           f"background-color: rgb({R2},{G2},{B2});"
                           f"color: {ColoresHEX.COLOR5};"
                           f"border-radius: 8px;")
        self.setText(texto_boton)
        self.setFont(QFont('Arial', 16, QFont.Bold))



