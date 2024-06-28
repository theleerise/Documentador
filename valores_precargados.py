class ColoresRgb:
    COLOR1 = (250, 245, 173)
    COLOR2 = (208, 236, 231)
    COLOR3 = (167, 175, 159)
    COLOR4 = (255, 0, 0)  # ROJO
    COLOR5 = (255, 250, 0)  # AMARILLO
    COLOR6 = (0, 0, 250)  # AZUL
    COLOR7 = (79, 92, 106)  # --> Interfaz
    COLOR8 = (62, 73, 84)  # --> Interfaz
    COLOR9 = (231, 235, 238)
    COLOR10 = (208, 213, 220)  # --> Para componentes
    COLOR11 = (97, 106, 107)  # --> Interfaz


class ColoresHEX:
    COLOR1 = '#566573'  # --> FONDO
    COLOR2 = '#273746'
    COLOR3 = '#4A5552'
    COLOR4 = '#324842'
    COLOR5 = '#FFFFFF'  # --> BLANCO
    COLOR6 = '#000000'
    COLOR7 = '#50646E'

    # paleta de colores de adobe1
    COLOR8 = '#7956CA'
    COLOR9 = '#725FA0'
    COLOR10= '#7640F5'
    COLOR11= '#1A0238'  # FONDO
    COLOR12= '#625975'
    COLOR13= '#42414B'
    COLOR14= '#2D2936'
    COLOR15= '#3D4361'
    COLOR16= '#3F2152'


class ValoresFrameCSS:

    @staticmethod
    def css(tipo_estilo):
        estilo = tipo_estilo.upper()

        if estilo == 'PRUEBA':
            CSS = (f"background-color: rgb(200,200,200);"
                   f"border-radius: 10%")
            return CSS
        if estilo == 'CSS7':
            R, G, B = ColoresRgb.COLOR7
            CSS = (f"background-color: rgb({R},{G},{B});"
                   f"border-radius: 10%")
            return CSS
        if estilo == 'CSS8':
            R, G, B = ColoresRgb.COLOR8
            CSS = (f"background-color: rgb({R},{G},{B});"
                   f"border-radius: 10%")
            return CSS
        if estilo == 'CSS9':
            CSS = (f"background-color: {ColoresHEX.COLOR11};"
                   f"border-radius: 10%")
            return CSS
        else:
            print("··#Estilo de CCS no existe. Asignamos el color Rojo como aviso#··")
            R, G, B = ColoresRgb.COLOR4
            CSS = (f"background-color: rgb({R},{G},{B});"
                   f"border-radius: 10%")
            return CSS
