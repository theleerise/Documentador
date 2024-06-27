from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QTextEdit, QLabel, \
    QPushButton, QLayout, QFrame

'''Librerias Propias'''
from componentes import CajaDeTexto, Color, EtiquetaStilo1, CajaDeColores, FramePantalla, BotonDcho
from valores_precargados import ColoresRgb, ValoresFrameCSS, ColoresHEX
from funcionalidades import Utilidades as UTIL

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        icono = QIcon("icono.png")
        self.setWindowIcon(icono)
        self.setWindowTitle("Documentador")
        self.resize(1200, 900)
        R, G, B = ColoresRgb.COLOR11
        #self.setStyleSheet(f"background-color: rgb({R},{G},{B})")
        self.setStyleSheet(f"background-color: {ColoresHEX.COLOR1}")


        #Componenten general
        self.componente_principal = QWidget()
        self.setCentralWidget(self.componente_principal)

        #Layout Principal
        self.layout_principal = QHBoxLayout()
        self.componente_principal.setLayout(self.layout_principal)

        # DISTRIBUCION de la pantalla
        self.agregar_componentes_dho()
        self.agregar_componentes_izq()



    def agregar_componentes_dho(self):
        #Global
        self.parent_frame_dho = FramePantalla(ValoresFrameCSS.css('CSS7'))
        self.lay_dho = QVBoxLayout()

        #prueba
        self.etiqueta_op1 = EtiquetaStilo1("Opciones", "CENTER", "Arial", ColoresRgb.COLOR8)
        self.etiqueta_op1.setFixedHeight(70)
        self.lay_dho.addWidget(self.etiqueta_op1)

        self.boton_gen_sql = BotonDcho("Generar SQL's")
        self.boton_gen_sql.setFixedSize(200, 50)
        #self.boton_gen_sql.clicked.connect(UTIL.prueba_boton)
        self.lay_dho.addWidget(self.boton_gen_sql)


        self.etiqueta_op2 = EtiquetaStilo1("Mensajes", "CENTER", "Arial", ColoresRgb.COLOR8)
        self.etiqueta_op2.setFixedHeight(70)
        self.lay_dho.addWidget(self.etiqueta_op2)


        #PUBLICACION de componente
        #self.layout_principal.addLayout(self.lay_dho)
        self.parent_frame_dho.setLayout(self.lay_dho)
        self.layout_principal.addWidget(self.parent_frame_dho)



    def agregar_componentes_izq(self):
        self.lay_izq = QVBoxLayout()
        self.lay_izq_1 = QHBoxLayout()
        self.lay_izq_2 = QVBoxLayout()
        self.lay_izq.addLayout(self.lay_izq_1)
        self.lay_izq.addLayout(self.lay_izq_2)
        #prueba


        #FUNCIONALIDAD
        self.lay_izq_2.addWidget(CajaDeTexto())


        #PUBLICACION
        self.layout_principal.addLayout(self.lay_izq)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    exit(app.exec())