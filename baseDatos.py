import sqlite3
import os
from time import strftime
     
class BaseDatos(object):
    def __init__(self):
        self.listaErrores = []
        self.iniciarDirectorios()

        self.__error = None
        self.directorios = []
        
        self.registroBaseDatos = strftime('%H:%M:%S %p')
        self.conexionBaseDatos = sqlite3.connect(
            './config/db_sqlite3/database/base_datos_gesv.db'
        )
        self.cursorBaseDatos = self.conexionBaseDatos.cursor()
        self.iniciarServicios()


    def iniciarServicios(self):
        self.escribirScriptCreacionTablas()
        self.iniciarAdmin()
        self.escribirScriptRespaldo()

    def iniciarAdmin(self):
        self.cursorBaseDatos.execute(
            '''INSERT INTO usuario VALUES(
                CURRENT_TIMESTAMP, 'admin',
                'admin', 'admin'
            )'''
        )
        self.conexionBaseDatos.commit()
    def iniciarDirectorios(self):
        if './db_sqlite3' in os.listdir():
            self.iniciarListaDirectorios()
        else:
            try:
                os.mkdir(
                    './config/db_sqlite3'
                )
            except:
                self.__error = '[ * ]  Error en la creacion de directorio'
                self.listaErrores.append(
                    self.__error
                )
            finally:
                try:
                    os.mkdir(
                        './config/db_sqlite3/scripts'
                    )
                except:
                    self.__error = '[ * ]  Error en la creacion de directorio'
                    self.listaErrores.append(
                        self.__error
                    )
                finally:
                    try:
                        os.mkdir(
                            './config/db_sqlite3/database'
                        )
                    except:
                        self.__error = '[ * ]  Error en la creacion de directorio'
                        self.listaErrores.append(
                            self.__error
                        )
                    finally:
                        try:
                            os.mkdir(
                                './config/db_sqlite3/config'
                            )
                        except:
                            self.__error = '[ * ]  Error en la creacion de directorio'
                            self.listaErrores.append(
                                self.__error
                            )
    def iniciarListaDirectorios(self):
        for x in os.listdir():
            self.directorios.append(x)
    def escribirScriptRespaldo(self):
        #print(f'    [ * ]  Iniciando la exportacion de datos...')
        with open(
            './config/db_sqlite3/scripts/SCRIPT_RESPALDO.sql',
            'w') as script:
            self.cursorBaseDatos.execute(
                'SELECT * FROM cliente_gesv'
            )
            self.fetchallBaseDatos = self.cursorBaseDatos.fetchall()
            for dato in self.fetchallBaseDatos:
                dato = str(dato)
                #print(f'    [ + ]  Datos exportados')
                script.write('INSERT INTO cliente_gesv VALUES%s;\n'%dato)
            script.close()
    def escribirScriptCreacionTablas(self):
        TABLA_CLIENTE = '''
        CREATE TABLE IF NOT EXISTS cliente_gesv(
            fecha_registro VARCHAR2(25) NOT NULL,
            rut VARCHAR2(12) PRIMARY KEY NOT NULL,
            nombres VARCHAR2(30) NOT NULL,
            apellidos VARCHAR2(30) NOT NULL,
            nacionalidad VARCHAR2(25) NOT NULL,
            sexo VARCHAR2(9) NOT NULL,
            fecha_nacimiento VARCHAR2(20) NOT NULL,
            region VARCHAR2(30) NOT NULL,
            comuna VARCHAR2(25) NOT NULL,
            direccion VARCHAR2(25) NOT NULL,
            nro_domicilio NUMERIC(6) NOT NULL,
            fono NUMERIC(11) NOT NULL,
            e_mail VARCHAR2(25) NOT NULL
            );'''
        TABLA_USUARIO = '''
        CREATE TABLE IF NOT EXISTS usuario(
            fecha_registro VARCHAR2(25) NOT NULL,
            nombre_usuario VARCHAR2(20) NOT NULL,
            contrasena VARCHAR2(20) NOT NULL,
            e_mail VARCHAR2(25) NOT NULL);'''

        TABLA_REGISTRO_USUARIO = '''
        CREATE TABLE IF NOT EXISTS REGISTRO_USUARIO(
            fecha_registro VARCHAR2(30) NOT NULL,
            clasificacion VARCHAR2(15) NOT NULL,
            rut VARCHAR2(15) NOT NULL
            );'''

        TABLA_APP_GESV = '''
        CREATE TABLE IF NOT EXISTS GESV(
            fecha_registro VARCHAR2(30),
            errores VARCHAR2(150));'''
        with open(
            './config/db_sqlite3/scripts/SCRIPT_CREACION_TABLA_REGISTRO_USUARIO.sql',
            'w'
            ) as script:

            for lineaScript in TABLA_REGISTRO_USUARIO:
                lineaScript = str(lineaScript)
                script.write(
                    '%s'%lineaScript
                    )
        script.close()

        with open(
            './config/db_sqlite3/scripts/SCRIPT_CREACION_TABLA_USUARIO.sql',
            'w'
            ) as script:

            for lineaScript in TABLA_USUARIO:
                lineaScript = str(lineaScript)
                script.write(
                    '%s'%lineaScript
                    )
        script.close()

        with open(
            './config/db_sqlite3/scripts/SCRIPT_CREACION_TABLA_CLIENTE.sql',
            'w'
            ) as script:
            for lineaScript in TABLA_CLIENTE:
                lineaScript = str(lineaScript)
                script.write(
                    '%s'%lineaScript
                    )
        script.close()

        with open(
            './config/db_sqlite3/scripts/SCRIPT_TABLA_GESV.sql',
            'w'
            ) as script:
            for lineaScript in TABLA_APP_GESV:
                lineaScript = str(lineaScript)
                script.write(
                    '%s'%lineaScript
                    )
        script.close()
        self.lecturaScriptsSQL()
    def lecturaScriptsSQL(self):
        scriptSQL = open(
            './config/db_sqlite3/scripts/SCRIPT_CREACION_TABLA_REGISTRO_USUARIO.sql',
            'r'
            )
        self.cursorBaseDatos.executescript(scriptSQL.read())
        self.conexionBaseDatos.commit()

        scriptSQL = open(
            './config/db_sqlite3/scripts/SCRIPT_CREACION_TABLA_USUARIO.sql',
            'r'
            )
        self.cursorBaseDatos.executescript(scriptSQL.read())
        self.conexionBaseDatos.commit()

        scriptSQL = open(
            './config/db_sqlite3/scripts/SCRIPT_CREACION_TABLA_CLIENTE.sql',
            'r'
            )
        self.cursorBaseDatos.executescript(scriptSQL.read())
        self.conexionBaseDatos.commit()

        scriptSQL = open(
            './config/db_sqlite3/scripts/SCRIPT_TABLA_GESV.sql',
            'r'
            )
        self.cursorBaseDatos.executescript(scriptSQL.read())
        self.conexionBaseDatos.commit()   