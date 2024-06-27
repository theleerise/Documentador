from crear_ventana import VentanaPrincipal, QApplication
#from crear_ventana2 import VentanaPrincipal, QApplication
from sys import exit

'''Archivo de ejecucion de la ventana'''
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    exit(app.exec())