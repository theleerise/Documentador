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
        self.resize(600, 400)
        R, G, B = ColoresRgb.COLOR11
        #self.setStyleSheet(f"background-color: rgb({R},{G},{B})")
        self.setStyleSheet(f"background-color: {ColoresHEX.COLOR16}")

        self.contenido_caja = ''


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
        self.parent_frame_dho = FramePantalla(ValoresFrameCSS.css('CSS9'))
        self.lay_dho = QVBoxLayout()


        ###########################################
        #ººººººººººººComponentesºººººººººººººººººº#
        ###########################################
        self.etiqueta_op1 = EtiquetaStilo1("Opciones", "CENTER", "Arial", ColoresHEX.COLOR15)
        self.etiqueta_op1.setFixedHeight(70)
        self.lay_dho.addWidget(self.etiqueta_op1)

        self.boton_gen_sql = BotonDcho("Generar SQL's")
        self.boton_gen_sql.setFixedSize(200, 50)
        #self.boton_gen_sql.clicked.connect(UTIL.prueba_boton)
        self.boton_gen_sql.clicked.connect(self.generar_sql)
        self.lay_dho.addWidget(self.boton_gen_sql)

        self.boton_gen_campos = BotonDcho("Generar Campos")
        self.boton_gen_campos.setFixedSize(200, 50)
        #self.boton_gen_campos.clicked.connect(UTIL.prueba_boton)
        self.boton_gen_campos.clicked.connect(self.generar_campos)
        self.lay_dho.addWidget(self.boton_gen_campos)

        self.boton_gen_numero = BotonDcho("Generar Letra-Num")
        self.boton_gen_numero.setFixedSize(200, 50)
        self.boton_gen_numero.clicked.connect(self.numerar_campos)
        self.lay_dho.addWidget(self.boton_gen_numero)

        self.etiqueta_op2 = EtiquetaStilo1("Mensajes", "CENTER", "Arial", ColoresHEX.COLOR15)
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

        #FUNCIONALIDAD
        self.caja = CajaDeTexto()
        self.lay_izq_2.addWidget(self.caja)

        #PUBLICACION
        self.layout_principal.addLayout(self.lay_izq)


    ##############################
    #ººººººº#Funcionalidadººººººº#
    ##############################

    def generar_sql(self):

        self.contenido_caja = self.caja.toPlainText()
        #dividir el contenido en lineas
        lineas = self.contenido_caja.splitlines()
        UTIL.func_generar_sql(lineas)
        self.contenido_caja=''

    def generar_campos(self):
        self.contenido_caja = self.caja.toPlainText()
        # dividir el contenido en lineas
        lineas = self.contenido_caja.splitlines()
        UTIL.func_numerador_de_campos(lineas,'A')
        self.contenido_caja = ''

    def numerar_campos(self):
        self.contenido_caja = self.caja.toPlainText()
        # dividir el contenido en lineas
        lineas = self.contenido_caja
        UTIL.func_letra_campo(lineas)
        self.contenido_caja = ''


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    exit(app.exec())
