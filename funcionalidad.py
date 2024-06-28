import os


class Utilidades():
    @staticmethod
    def prueba_boton():
        print('Presionado boton')

    @staticmethod
    def func_generar_sql(variables_sql: str):
        for linea in variables_sql:
            print('SELECT * FROM VARIABLES')
            print(f"WHERE VARIABLE = '{linea}';")

    def func_numerador_de_campos(campos: str, tipo_de_campo: str, N_CAMPO=0):
        archivo = 'resultado_campos.txt'
        existe = False

        def validar_archivo(nombre_archivo):
            ruta_archivo = os.path.join(os.path.dirname(__file__), nombre_archivo)
            if os.path.exists(ruta_archivo):
                return True
            else:
                return False

        existe = validar_archivo(archivo)

        if existe:
            os.remove(archivo)
            ### incluir codigo para llamar nuevamente a la funcion ###
            Utilidades.func_numerador_de_campos(campos,tipo_de_campo, N_CAMPO)
            print("Se ha eliminado el archivo, vuelvalo a intentar")
        else:

            resultado = open(archivo, mode='a')
            for campo in campos:
                N_CAMPO += 1
                NOMBRE = campo.rstrip()  # La funcion rstrip() es similar a TRIM() de SQL, elimina los espacios
                TIPO = f'(Campo {tipo_de_campo}{N_CAMPO})'
                cadena_texto = f'{NOMBRE} {TIPO}\n'
                resultado.write(cadena_texto)

            resultado.close()
            print('Proceso finalizado :)')

    @staticmethod
    def func_letra_campo( entrada: str ):
        letra_campo, cantidad = eval(entrada)
        numeros = range(1,cantidad+1)
        for numero in numeros:
            print(f'{letra_campo}{numero}')
