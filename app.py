import tkinter as tk
import socket
import os
import pandas as pd
import time
from baseDatos import BaseDatos
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from time import strftime
from cliente import Cliente

class Inicio(tk.Frame):
    def __init__(self, w):
        super().__init__(w)
        width_of_window = 427
        height_of_window = 250
        screen_width = w.winfo_screenwidth()
        screen_height = w.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
        w.overrideredirect(1)
        self.styleInicio = ttk.Style()
        self.styleInicio.theme_use('clam')
        self.styleInicio.configure(
            'red.Horizontal.TProgressbar', foreground = 'red', background = '#786271'
        )
        self.barraProgreso = ttk.Progressbar(
            w, style = 'white.Horizontal.TProgressbar',
            orient = tk.HORIZONTAL, length = 500, mode = 'determinate',)
        self.barraProgreso.place(x = -10, y = 235)


        tk.Frame(w, width = 427, height = 241, background = '#786271').place(x=0,y=0)
        self.botonInicio = tk.Button(
            w, width = 20, height = 1, text = 'Iniciar',
            font = ('Ubuntu light', 12),
            command = self.barra, border = 0,
            foreground = '#FFFFFF', background = '#D5A27C'
        )
        self.botonInicio.place(x = 120, y = 200)

        self.label1= tk.Label(
            w, text = 'GESV', foreground = '#FFFFFF',
            background = '#786271', font = ('Calibri (Body)',18,'bold')
        )
        self.label1.place(x = 50, y = 80)

        self.label2 = tk.Label(
            w, text = 'Aplicación', foreground = '#FFFFFF',
            background ='#786271', font = ('Calibri (Body)',18))
        self.label2.place(x = 125, y = 82)

        self.label3 = tk.Label(
            w, text='version 1.0',foreground = '#FFFFFF',
            background ='#786271', font = ('Calibri (Body)',13))
        self.label3.place(x=50,y=110)
        w.mainloop()
    def iniciarPrograma(self):
        root = tk.Tk()
        programa = Ventana(root)
        programa.mainloop()
    def barra(self):
        self.labelCarga = tk.Label(
            w, text='Cargando...', foreground = '#FFFFFF', background = '#D5A27C',
            font = ('Ubuntu light', 12)
        )
        self.labelCarga.pack(fill = 'x')
        
        
        r = 0
        for i in range(100):
            self.barraProgreso['value'] = r
            #print('Cargando estado [ '+str(self.barraProgreso['value'])+'% ]')
            w.update_idletasks()
            time.sleep(0.01)
            r = r+1
        w.destroy()
        self.iniciarPrograma()
        
class Configuracion(object):
    def __init__(self):
        self.modoOscuro = False
        self.modoClaro = True

        self.hostOperador = socket.gethostname()
        self.ipOperador = socket.gethostbyname(self.hostOperador)
        self.nombreOperador = str('[ '+self.hostOperador+'@'+self.ipOperador+' ]')

        self.rutaIconoModo = r'./config/icon/modo.jpg'
        self.rutaIconoConfig = r'./config/icon/conf.jpg'
        self.rutaIconoUsuario = r'./config/icon/usuario.jpg'
        self.rutaIconoEditorTexto = r'./config/icon/editor.jpg'
    def crearArchivoConfig(self):
        with open('./config/config.txt', 'w') as archivoConfig:
            archivoConfig.write('0')
        archivoConfig.close()

class Operador:
    def __init__(self):
        self.listaOperacion = [
            'Registrar cliente',
            'Gestionar cliente',
            'Administrador'
            ]

class Ventana(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.modoClaro = modoClaro
        self.modoOscuro = modoOscuro
        self.Configuracion = Configuracion()
        self.Configuracion.crearArchivoConfig()

        root.title(self.Configuracion.nombreOperador)
        root.geometry('700x500')

        self.framePanel = tk.Frame(
            self, background = '#786271'
        )
        self.framePanel.pack(
            fill = 'both', expand = True, padx = 15, side = tk.TOP
        )
        self.labelReloj = tk.Label(
            self, font = ('Ubuntu light', 14, 'bold'),
            background = '#786271', foreground = '#FFFFFF'
        )
        self.labelReloj.pack(
            fill = 'both', expand = True, padx = 15, pady = 15
        )
        self.reloj()

        self.configure(background = '#DDDDDD')
        self.pack(
            fill = 'both',expand = True
        )

        '''self.iconoConfiguracion = tk.PhotoImage(
            file = self.Configuracion.rutaIconoConfig
        )
        self.botonConfiguracion = tk.Button(
            self.framePanel, relief = 'flat'
        )
        self.botonConfiguracion.config(
            image = self.iconoConfiguracion, activebackground = '#000000',
            background = '#000000'
        )
        self.botonConfiguracion.pack(
            expand = True, pady = 15, side = tk.LEFT
        )'''

        self.iconoModo = tk.PhotoImage(
            file = self.Configuracion.rutaIconoModo
        )
        self.botonModo = tk.Button(
            self.framePanel,
            relief = 'flat',
            command = self.cambiarModo
        )
        self.botonModo.config(
            image = self.iconoModo, activebackground = '#000000',
            background = '#000000'
        )
        self.botonModo.pack(
            expand = True, pady = 15,
            side = tk.RIGHT
        )

        '''self.iconoUsuario = tk.PhotoImage(
            file = self.Configuracion.rutaIconoUsuario
        )
        self.botonUsuario = tk.Button(
            self.framePanel, relief = 'flat'
        )
        self.botonUsuario.config(
            image = self.iconoUsuario, activebackground = '#000000',
            background = '#000000'
        )
        self.botonUsuario.pack(
            expand = True, pady = 15,
            side = tk.RIGHT
        )'''

        self.frameVentana = tk.Frame(self)
        self.frameVentana.configure(background = '#FFFFFF')
        self.frameVentana.pack(
            fill = 'both', expand = True, padx = 15
        )
        self.frameOperacion = Operacion(self.frameVentana)
        self.frameOperacion.configure(background = '#FFFFFF')
        self.frameOperacion.pack(
            fill = 'both', expand= True,
            padx = 10, pady = 10
        )
        self.frameFooter = tk.Frame(
            self, background = '#786271'
        )
        self.frameFooter.pack(
            fill = 'both', expand = True, padx = 15, pady = 15, side = tk.BOTTOM
        )
        self.labelEstado = tk.Label(
            self.frameFooter, font = ('Ubuntu light', 14, 'bold'),
            background = '#786271', foreground = '#FFFFFF'
        )
        self.labelEstado.pack(
            expand = True
        )
        self.configure(
            background = '#DDDDDD'
        )
        self.pack(
            fill = 'both', expand = True
        )
    def reloj(self):
        hora = strftime('%H:%M:%S %p')
        self.labelReloj.config(text = hora)
        self.labelReloj.after(200, self.reloj)
    def cambiarModo(self):
        if self.modoClaro:
            self.modoOscuro = True
            self.modoClaro = False

            self.Configuracion.modoOscuro = True
            self.Configuracion.modoClaro = False
            with open('./config/config.txt', 'w') as archivoConfig:
                archivoConfig.write('1')
            archivoConfig.close()

            self.configure(background = '#111111')
            self.frameVentana.configure(background = '#222222')

        elif self.modoOscuro:
            self.modoClaro = True
            self.modoOscuro = False

            self.Configuracion.modoClaro = True
            self.Configuracion.modoOscuro = False

            with open('./config/config.txt', 'w') as archivoConfig:
                archivoConfig.write('0')
            archivoConfig.close()

            self.configure(background = '#DDDDDD')
            self.frameVentana.configure(background = '#FFFFFF')


        try:
            self.frameOperacion.cambiarModo()
        except Exception as e:
            e = str(e)
            BaseDatos.cursorBaseDatos.execute(
                '''
                INSERT INTO GESV(fecha_registro, errores)
                VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
            )
            BaseDatos.conexionBaseDatos.commit()

class Operacion(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Operador = Operador()
        self.Cliente = Cliente()
        self.Configuracion = Configuracion()
        self.modoClaro = modoClaro
        self.modoOscuro = modoOscuro


        # Construccion del modulo de operacion
        self.labelFrameOperacion = tk.LabelFrame(
            self, text = 'Seleccione una operación', font = ('Ubuntu light', 14),
            relief = 'solid', bd = 1, background = '#FFFFFF'
        )
        self.labelFrameOperacion.pack(
            fill = 'x', expand = True
        )
        self.frameListBox = tk.Frame(
            self.labelFrameOperacion, background = '#FFFFFF'
        )
        self.frameListBox.pack(
            fill = 'x', expand = True, padx = 15
        )
        
        self.listBoxOperacion = tk.Listbox(
            self.frameListBox, relief = 'solid', bd = 1,
            justify = 'center', selectbackground = '#786271',
            background = '#DDDDDD'
        )

        self.listBoxOperacion.pack(
            fill = 'both', expand = True, side = tk.RIGHT,
            padx = 50, pady = 15
        )

        # Funciones de teclado
        self.listBoxOperacion.bind(
            '<Double-Button-1>',
            lambda event:self.operacionUsuario(event)
        )
        self.listBoxOperacion.bind(
            '<Return>',
            lambda event:self.operacionUsuario(event)
        )
        self.insertarOperaciones()
    def insertarOperaciones(self):
        for operacion in self.Operador.listaOperacion:
            self.listBoxOperacion.insert(tk.END, operacion)

    def cambiarModo(self):
        try:
            if self.modoOscuro:
                self.modoClaro = True
                self.modoOscuro = False
                self.configure(background = '#FFFFFF')
                self.frameListBox.configure(background = '#FFFFFF')
                self.labelFrameOperacion.configure(
                    background = '#FFFFFF', foreground = '#000000'
                )                
                self.listBoxOperacion.configure(
                    background = '#DDDDDD', foreground = '#000000', relief = 'solid'
                )
            elif self.modoClaro:
                self.modoClaro = False
                self.modoOscuro = True
                self.configure(background = '#222222')
                self.frameListBox.configure(background = '#222222')
                self.labelFrameOperacion.configure(
                    background = '#222222', foreground = '#FFFFFF', relief = 'groove'
                )
                self.listBoxOperacion.configure(
                    background = '#333333', foreground = '#FFFFFF'
                )
            #print('modo claro  : ',self.modoClaro)
            #print('modo oscuro : ',self.modoOscuro)

            try:
                self.cambiarModoRegistro()
            except Exception as e:
                e = str(e)
                BaseDatos.cursorBaseDatos.execute(
                    '''
                    INSERT INTO GESV(fecha_registro, errores)
                    VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
                )
                BaseDatos.conexionBaseDatos.commit()
            finally:
                try:
                    self.cambiarModoGestion()
                except Exception as e:
                    e = str(e)
                    BaseDatos.cursorBaseDatos.execute(
                        '''
                        INSERT INTO GESV(fecha_registro, errores)
                        VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
                    )
                    BaseDatos.conexionBaseDatos.commit()
                finally:
                    try:
                        self.cambiarModoModificacion()
                    except Exception as e:
                        e = str(e)
                        BaseDatos.cursorBaseDatos.execute(
                            '''
                            INSERT INTO GESV(fecha_registro, errores)
                            VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
                        )
                        BaseDatos.conexionBaseDatos.commit()
        except Exception as e:
            e = str(e)
            BaseDatos.cursorBaseDatos.execute(
                '''
                INSERT INTO GESV(fecha_registro, errores)
                VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
            )
            BaseDatos.conexionBaseDatos.commit()
    def cambiarModoRegistro(self):
        if self.modoClaro:
            self.modoOscuro = False
            # ----------------------- MODULO DE REGISTRO ----------------------- #
            self.frameModuloRegistro.configure(background = '#FFFFFF')
            self.labelFrameFormulario.configure(
                background = '#FFFFFF', foreground = '#000000',
                relief = 'solid'
            )
            self.labelEstado.configure(
                background = '#FFFFFF', foreground = '#000000'
            )
            self.labelFrameDatosPersonales.configure(
                background = '#FFFFFF', foreground = '#000000',
                relief = 'solid'
            )
            self.labelFrameDatosUbicacion.configure(
                background = '#FFFFFF', foreground = '#000000',
                relief = 'solid'
            )

            self.labelRut.configure(
                background = '#FFFFFF', foreground = '#000000',
            )
            self.labelNombres.configure(
                background = '#FFFFFF', foreground = '#000000',
            )
            self.labelApellidos.configure(
                background = '#FFFFFF', foreground = '#000000',
            )
            self.labelNacionalidad.configure(
                background = '#FFFFFF', foreground = '#000000',
            )
            self.labelSexo.configure(
                background = '#FFFFFF', foreground = '#000000',
            )
            self.labelRegion.configure(
                background = '#FFFFFF', foreground = '#000000',
            )
            self.labelFechaNacimiento.configure(
                background = '#FFFFFF', foreground = '#000000',
            )
            self.labelComuna.configure(
                background = '#FFFFFF', foreground = '#000000',
            )
            self.labelDireccion.configure(
                background = '#FFFFFF', foreground = '#000000',
            )
            self.labelNumeroDomicilio.configure(
                background = '#FFFFFF', foreground = '#000000',
            )
            self.labelFono.configure(
                background = '#FFFFFF', foreground = '#000000',
            )
            self.labelEmail.configure(
                background = '#FFFFFF', foreground = '#000000',
            )

            self.frameFechaNacimiento.configure(background = '#FFFFFF')
        elif self.modoOscuro:
            self.modoClaro = False
            # ----------------------- MODULO DE REGISTRO ----------------------- #
            self.frameModuloRegistro.configure(background = '#222222')
            self.labelFrameFormulario.configure(
                background = '#222222', foreground = '#FFFFFF',
                relief = 'groove'
            )
            self.labelEstado.configure(
                background = '#222222', foreground = '#FFFFFF'
            )
            self.labelFrameDatosPersonales.configure(
                background = '#222222', foreground = '#FFFFFF',
                relief = 'groove'
            )
            self.labelFrameDatosUbicacion.configure(
                background = '#222222', foreground = '#FFFFFF',
                relief = 'groove'
            )

            self.labelRut.configure(
                background = '#222222', foreground = '#FFFFFF',
            )
            self.labelNombres.configure(
                background = '#222222', foreground = '#FFFFFF',
            )
            self.labelApellidos.configure(
                background = '#222222', foreground = '#FFFFFF',
            )
            self.labelNacionalidad.configure(
                background = '#222222', foreground = '#FFFFFF',
            )
            self.labelSexo.configure(
                background = '#222222', foreground = '#FFFFFF',
            )
            self.labelRegion.configure(
                background = '#222222', foreground = '#FFFFFF',
            )
            self.labelFechaNacimiento.configure(
                background = '#222222', foreground = '#FFFFFF',
            )
            self.labelComuna.configure(
                background = '#222222', foreground = '#FFFFFF',
            )
            self.labelDireccion.configure(
                background = '#222222', foreground = '#FFFFFF',
            )
            self.labelNumeroDomicilio.configure(
                background = '#222222', foreground = '#FFFFFF',
            )
            self.labelFono.configure(
                background = '#222222', foreground = '#FFFFFF',
            )
            self.labelEmail.configure(
                background = '#222222', foreground = '#FFFFFF',
            )

            self.frameFechaNacimiento.configure(background = '#222222')
    def cambiarModoGestion(self):
        if self.modoClaro:
            self.modoOscuro = False
            self.frameBusqueda.configure(background = '#FFFFFF')
            self.labelFrameBusqueda.configure(
                background = '#FFFFFF', foreground = '#000000',
                relief = 'solid'
            )
            self.frameTreeView.configure(background = '#FFFFFF')
            self.style = ttk.Style(self.moduloGestion)
            self.style.theme_use(
                'clam'
            )
            self.style.configure(
                'Treeview',
                background = '#FFFFFF', 
                fieldbackground = '#FFFFFF',
                foreground = '#000000'
            )


            self.style.configure(
                'mystyle.Treeview', highlightthickness = 0, border = 0,
                font = ('Ubuntu light', 9)
            )
            self.style.configure(
                'mystyle.Treeview.Heading', font=('Calibri (Body)', 11)
            )
            self.treeView.configure(style = 'mystyle.Treeview')


            self.clickDerecho.configure(
                background = '#FFFFFF',
                foreground = '#000000'
            )
            self.subMenuOrden.configure(
                background = '#FFFFFF',
                foreground = '#000000'
            )
            self.subMenuFiltro.configure(
                background = '#FFFFFF',
                foreground = '#000000'
            )
        elif self.modoOscuro:
            self.modoClaro = False

            self.frameBusqueda.configure(background = '#222222')
            self.labelFrameBusqueda.configure(
                background = '#222222', foreground = '#FFFFFF',
                relief = 'groove'
            )
            self.frameTreeView.configure(background = '#222222')
            self.style = ttk.Style(self.moduloGestion)
            self.style.theme_use(
                'clam'
            )
            self.style.configure(
                'Treeview',
                background = '#222222', 
                fieldbackground = '#222222',
                foreground = '#FFFFFF'
            )
            self.style.configure(
                'mystyle.Treeview', highlightthickness = 0, border = 0,
                font = ('Ubuntu light', 9)
            )
            self.style.configure(
                'mystyle.Treeview.Heading', font=('Calibri (Body)', 11)
            )
            self.clickDerecho.configure(
                background = '#333333',
                foreground = '#FFFFFF'
            )
            self.subMenuOrden.configure(
                background = '#333333',
                foreground = '#FFFFFF'
            )
            self.subMenuFiltro.configure(
                background = '#333333',
                foreground = '#FFFFFF'
            )
    def cambiarModoModificacion(self):
        if self.modoClaro:
            self.modoOscuro = False
            self.frameModuloModificacion.configure(background = '#FFFFFF')
            self.labelFrameModificacion.configure(
                background = '#FFFFFF', foreground = '#000000', relief = 'solid'
            )
            self.frameDatos.configure(background = '#FFFFFF')
        elif self.modoOscuro:
            self.modoClaro = False

            self.frameModuloModificacion.configure(background = '#222222')
            self.labelFrameModificacion.configure(
                background = '#222222', foreground = '#FFFFFF', relief = 'groove'
            )
            self.frameDatos.configure(background = '#222222')

    def operacionUsuario(self, event):
        # Modulo de registro
        if self.listBoxOperacion.get(
            self.listBoxOperacion.curselection()) == self.Operador.listaOperacion[0]:
            try:
                self.moduloRegistro = tk.Tk()
                self.moduloRegistro.configure(background = '#786271')
                self.moduloRegistro.geometry('1000x670')
                self.moduloRegistro.title('Modulo de Registro')

                self.frameModuloRegistro = tk.Frame(
                    self.moduloRegistro, background = '#FFFFFF')
                self.frameModuloRegistro.pack(
                    fill = 'both', expand = True, padx = 15, pady = 15
                )
                self.labelFrameFormulario = tk.LabelFrame(
                    self.frameModuloRegistro, text = 'Modulo de Registro',
                    font = ('Ubuntu light', 14), relief = 'solid', bd = 1,
                    foreground = '#786271', background = '#FFFFFF'
                )
                self.labelFrameFormulario.pack(
                    fill = 'both', expand = True, padx = 15, pady = 15
                )
                self.labelFrameDatosPersonales = tk.LabelFrame(
                    self.labelFrameFormulario, text = 'Datos personales del Cliente',
                    font = ('Ubuntu light', 14), relief = 'solid', bd = 1,
                    foreground = '#786271', background = '#FFFFFF'
                )
                self.labelFrameDatosPersonales.pack(
                    fill = 'x', expand = True, padx = 15, pady = 15, side = tk.LEFT
                )

                self.labelFrameDatosUbicacion = tk.LabelFrame(
                    self.labelFrameFormulario, text = 'Datos de ubicación del Cliente',
                    font = ('Ubuntu light', 14), relief = 'solid', bd = 1,
                    foreground = '#786271', background = '#FFFFFF'
                )
                self.labelFrameDatosUbicacion.pack(
                    fill = 'x', expand = True, padx = 15, pady = 15, side = tk.RIGHT
                )


                self.labelRut = tk.Label(
                    self.labelFrameDatosPersonales, text = '\n\nRut [XX.XXX.XXX-X]',
                    font = ('Ubuntu light', 12), background = '#FFFFFF'
                )
                self.labelRut.pack(expand = True)
                self.entryRut = tk.Entry(
                    self.labelFrameDatosPersonales, justify = 'center',
                    relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                    fg = '#000000', width = 30
                )
                self.entryRut.pack(expand = True, padx = 20, pady = 8)
                self.labelNombres = tk.Label(
                    self.labelFrameDatosPersonales, text = 'Nombres',
                    font = ('Ubuntu light', 12), background = '#FFFFFF'
                )
                self.labelNombres.pack(expand = True)
                self.entryNombres = tk.Entry(
                    self.labelFrameDatosPersonales, justify = 'center',
                    relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                    fg = '#000000', width = 30
                )
                self.entryNombres.pack(expand = True, padx = 20, pady = 8)
                self.labelApellidos = tk.Label(
                    self.labelFrameDatosPersonales, text = 'Apellidos',
                    font = ('Ubuntu light', 12), background = '#FFFFFF'
                )
                self.labelApellidos.pack(expand = True)
                self.entryApellidos = tk.Entry(
                    self.labelFrameDatosPersonales,justify = 'center',
                    relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                    fg = '#000000', width = 30
                )
                self.entryApellidos.pack(expand = True, padx = 20, pady = 8)
                self.labelNacionalidad = tk.Label(
                    self.labelFrameDatosPersonales, text = 'Nacionalidad',
                    font = ('Ubuntu light', 12), background = '#FFFFFF'
                )
                self.labelNacionalidad.pack(expand = True)
                self.entryNacionalidad = tk.Entry(
                    self.labelFrameDatosPersonales, justify = 'center',
                    relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                    fg = '#000000', width = 30
                )
                self.entryNacionalidad.pack(expand = True, padx = 20, pady = 8)
                self.labelSexo = tk.Label(
                    self.labelFrameDatosPersonales, text = 'Sexo',
                    font = ('Ubuntu light', 12), background = '#FFFFFF'
                )
                self.labelSexo.pack(expand = True)
                
                self.comboBoxSexo = ttk.Combobox(
                    self.labelFrameDatosPersonales, justify = 'center',
                    value = self.Cliente.listaSexo, font = ('Ubuntu light', 13),
                    width = 28, state = 'readonly'
                )
                self.comboBoxSexo.pack(expand = True, padx = 20, pady = 8)

                self.labelFechaNacimiento = tk.Label(
                    self.labelFrameDatosPersonales, text = 'Fecha de Nacimiento [DD/MM/AAAA]',
                    font = ('Ubuntu light', 12), background = '#FFFFFF'
                )
                self.labelFechaNacimiento.pack(expand = True)            
                self.frameFechaNacimiento = tk.Frame(
                    self.labelFrameDatosPersonales, background = '#FFFFFF'
                )
                self.frameFechaNacimiento.pack(expand = True, pady = 8)
                self.comboBoxDia = ttk.Combobox(
                    self.frameFechaNacimiento, justify = 'center',
                    value = self.Cliente.listaDias, font = ('Ubuntu light', 13),
                    width = 5, state = 'readonly'
                )
                self.comboBoxDia.pack(
                    fill = 'x', expand = True,
                    side = tk.LEFT, padx = 2
                )
                self.comboBoxMes = ttk.Combobox(
                    self.frameFechaNacimiento, justify = 'center',
                    value = self.Cliente.listaMes, font = ('Ubuntu light', 13),
                    width = 12, state = 'readonly'
                )
                self.comboBoxMes.pack(
                    fill = 'x', expand = True,
                    side = tk.LEFT, padx = 2
                )
                self.comboBoxAño = ttk.Combobox(
                    self.frameFechaNacimiento, justify = 'center',
                    value = self.Cliente.listaAños, font = ('Ubuntu light', 13),
                    width = 5, state = 'readonly'
                )
                self.comboBoxAño.pack(
                    fill = 'x', expand = True,
                    side = tk.RIGHT, padx = 2
                )
                self.labelRegion = tk.Label(
                    self.labelFrameDatosUbicacion,text = '\n\nRegión',
                    font = ('Ubuntu light', 12),background = '#FFFFFF'
                )
                self.labelRegion.pack(expand = True)

                self.comboBoxRegion = ttk.Combobox(
                    self.labelFrameDatosUbicacion, justify = 'center',
                    value = self.Cliente.listaRegion, font = ('Ubuntu light', 13),
                    width = 28, state = 'readonly'
                )
                self.comboBoxRegion.pack(expand = True, padx = 10, pady = 8)

                self.labelComuna = tk.Label(
                    self.labelFrameDatosUbicacion, text = 'Comuna',
                    font = ('Ubuntu light', 12), background = '#FFFFFF'
                )
                self.labelComuna.pack(expand = True)
                self.entryComuna = tk.Entry(
                    self.labelFrameDatosUbicacion, justify = 'center',
                    relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                    fg = '#000000', width = 30
                )
                self.entryComuna.pack(expand = True, padx = 20, pady = 8)
                self.labelDireccion = tk.Label(
                    self.labelFrameDatosUbicacion, text = 'Dirección',
                    font = ('Ubuntu light', 12), background = '#FFFFFF'
                )
                self.labelDireccion.pack(expand = True)
                self.entryDireccion = tk.Entry(
                    self.labelFrameDatosUbicacion, justify = 'center',
                    relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                    fg = '#000000',width = 30
                )
                self.entryDireccion.pack(expand = True, padx = 20, pady = 8)
                self.labelNumeroDomicilio = tk.Label(
                    self.labelFrameDatosUbicacion, text = 'Número de Domicilio',
                    font = ('Ubuntu light', 12), background = '#FFFFFF'
                )
                self.labelNumeroDomicilio.pack(expand = True)
                self.entryNumeroDomicilio = tk.Entry(
                    self.labelFrameDatosUbicacion, justify = 'center',
                    relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                    fg = '#000000', width = 30
                )
                self.entryNumeroDomicilio.pack(expand = True, padx = 20, pady = 8)

                self.labelFono = tk.Label(
                    self.labelFrameDatosUbicacion, text = 'Fono',
                    font = ('Ubuntu light', 12), background = '#FFFFFF'
                )
                self.labelFono.pack(expand = True)
                self.entryFono = tk.Entry(
                    self.labelFrameDatosUbicacion, justify = 'center',
                    relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                    fg = '#000000', width = 30
                )
                self.entryFono.pack(expand = True, padx = 20, pady = 8)
                self.labelEmail = tk.Label(
                    self.labelFrameDatosUbicacion, text = 'E-mail',
                    font = ('Ubuntu light', 12), background = '#FFFFFF'
                )
                self.labelEmail.pack(expand = True)
                self.entryEmail = tk.Entry(
                    self.labelFrameDatosUbicacion, justify = 'center',
                    relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                    fg = '#000000', width = 30
                )
                self.entryEmail.pack(expand = True, padx = 20, pady = 8)

                self.labelEstado = tk.Label(
                    self.frameModuloRegistro, font = ('Ubuntu light', 14, 'bold'),
                    background = '#FFFFFF', foreground = '#FF4861'
                )
                self.labelEstado.pack(
                    expand = True, side = tk.TOP
                )
                self.frameConfirmacion = tk.Frame(
                    self.frameModuloRegistro, relief = 'flat', width = 40,
                    background = '#D5A27C'
                )

                self.frameConfirmacion.pack(
                    fill = 'both', expand = True, pady = 15, padx = 15
                )
                self.labelEnter = tk.Label(
                    self.frameConfirmacion, text = 'Presione [ ENTER ] para registrar',
                    font = ('Ubuntu light', 14),
                    foreground = '#FFFFFF', background = '#D5A27C'
                )
                self.labelEnter.pack(
                    expand = True, pady = 15, padx = 15
                )
                self.moduloRegistro.bind(
                    '<Return>',
                    self.__registrarCliente
                )

                self.moduloRegistro.bind(
                    '<Escape>',
                    self.cerrarModuloRegistro
                )
                self.cambiarModoRegistro()
                self.moduloRegistro.mainloop()
            except Exception as e:
                e = str(e)
                BaseDatos.cursorBaseDatos.execute(
                    '''
                    INSERT INTO GESV(fecha_registro, errores)
                    VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
                )
                BaseDatos.conexionBaseDatos.commit()
        # Modulo de gestion
        elif self.listBoxOperacion.get(
            self.listBoxOperacion.curselection()) == self.Operador.listaOperacion[1]:
            self.moduloGestion = tk.Tk()
            self.moduloGestion.configure(background = '#786271')
            self.moduloGestion.geometry('1000x600')
            self.moduloGestion.title('Modulo de Gestion')
            
            self.moduloGestion.bind(
                '<Escape>',
                self.cerrarModuloGestion
            )
            
            self.frameBusqueda = tk.Frame(
                self.moduloGestion,
                background = '#FFFFFF'
            )
            self.frameBusqueda.pack(
                fill = 'both', expand = True,
                padx = 10, pady = 15
            )
            self.labelFrameBusqueda = tk.LabelFrame(
                self.frameBusqueda, text = 'Gestion de Cliente',
                font = ('Ubuntu light', 14), relief = 'solid',
                bd = 1, foreground = '#786271', background = '#FFFFFF'
            )
            self.labelFrameBusqueda.pack(
                fill = 'both', expand = True,
                padx = 15, pady = 15
            )

            self.frameTreeViewBusqueda = tk.Frame(
                self.labelFrameBusqueda, background = '#786271',
                relief = 'solid', bd = 1
            )
            self.frameTreeViewBusqueda.pack(
                fill = 'x', expand = False,
                padx = 10, pady = 10
            )

            self.labelBusqueda = tk.Label(
                self.frameTreeViewBusqueda, text = 'Buscador de Clientes',
                font = ('Ubuntu light', 14), background = '#786271',
                foreground = '#FFFFFF'
            )
            self.labelBusqueda.pack(
                fill = 'x', expand = True, side = tk.LEFT
            )
            self.entryBusqueda = tk.Entry(
                self.frameTreeViewBusqueda, justify = 'center',
                relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                fg = '#000000', width = 20
            )
            self.entryBusqueda.pack(
                fill = 'x', expand = True, padx = 15, side = tk.LEFT
            )
            self.entryBusqueda.bind(
                '<Return>',
                self.__buscarCliente
            )

            self.botonBusqueda = tk.Button(
                self.frameTreeViewBusqueda, text = 'Buscar cliente',
                relief = 'flat', width = 20, font = ('Ubuntu light', 10),
                fg = '#FFFFFF', justify = 'center', background = '#D5A27C'
                #command = self.__buscar_cliente
            )
            self.botonBusqueda.pack(
                fill = 'x', expand = True, padx = 15,
                pady = 10, side = tk.RIGHT
            )
            self.frameTreeView = tk.Frame(
                self.labelFrameBusqueda
            )
            self.frameTreeView.pack(
                fill = 'both', expand = True,
                padx = 10, pady = 15
            )
        
            #self.lectura_configuracion_treeView()
            self.treeView = ttk.Treeview(
                self.frameTreeView, height = 58,
                column = ('#1','#2','#3'
                        '#4','#5','#6',
                        '#7','#8','#9',
                        '#10','#11','#12',
                        '#13', '#14'),
                show = 'headings'
            )
            
            self.treeView.pack(
                fill = 'both', expand = True, side = tk.LEFT
            )
            self.treeView.heading(
                '#1', text = 'Fecha de Registro', anchor = tk.CENTER
            )
            self.treeView.heading(
                '#2', text = 'Rut', anchor = tk.CENTER
            )
            self.treeView.heading(
                '#3', text = 'Nombres', anchor = tk.CENTER
            )
            self.treeView.heading(
                '#4', text = 'Apellidos', anchor = tk.CENTER
            )
            self.treeView.heading(
                '#5', text = 'Nacionalidad', anchor = tk.CENTER
            )
            self.treeView.heading(
                '#6', text = 'Sexo', anchor = tk.CENTER
            )
            self.treeView.heading(
                '#7', text = 'Fec. de Nacimiento', anchor = tk.CENTER
            )
            self.treeView.heading(
                '#8', text = 'Región', anchor = tk.CENTER
            )
            self.treeView.heading(
                '#9', text = 'Comuna', anchor = tk.CENTER
            )
            self.treeView.heading(
                '#10', text = 'Dirección', anchor = tk.CENTER
            )
            self.treeView.heading(
                '#11', text = 'Nro. de Domicilio', anchor = tk.CENTER
            )
            self.treeView.heading(
                '#12', text = 'Fono', anchor = tk.CENTER
            )
            self.treeView.heading(
                '#13', text = 'E-mail', anchor = tk.CENTER
            )
            self.treeView.column('#1', width = 138, anchor = 'w')
            self.treeView.column('#2', width = 120, anchor = 'center')
            self.treeView.column('#3', width = 160, anchor = 'center')
            self.treeView.column('#4', width = 160, anchor = 'center')
            self.treeView.column('#5', width = 120, anchor = 'center')
            self.treeView.column('#6', width = 90, anchor = 'center')
            self.treeView.column('#7', width = 150, anchor = 'center')
            self.treeView.column('#8', width = 180, anchor = 'center')
            self.treeView.column('#9', width = 130, anchor = 'center')
            self.treeView.column('#10', width = 170, anchor = 'center')
            self.treeView.column('#11', width = 110, anchor = 'center')
            self.treeView.column('#12', width = 120, anchor = 'center')
            self.treeView.column('#13', width = 200, anchor = 'center')
            #self.treeView.bind('<ButtonRelease-1>', self.cliente_seleccionado)
            #self.treeView.bind('<Return>', self.__modificar_cliente)
            self.__obtenerCliente(event)
            self.scrollBarTreeView_y = ttk.Scrollbar(
                self.treeView, orient = 'vertical',
                command = self.treeView.yview
            )
            self.scrollBarTreeView_y.pack(fill = 'y', side = tk.RIGHT)
            self.scrollBarTreeView_x = ttk.Scrollbar(
                self.treeView, orient = 'horizontal',
                command = self.treeView.xview
            )
            self.scrollBarTreeView_x.pack(fill = 'x', side = tk.BOTTOM)
            self.treeView.configure(
                yscrollcommand = self.scrollBarTreeView_y.set,
                xscrollcommand = self.scrollBarTreeView_x.set,
                style = 'Treeview'
            )
            self.clickDerecho = tk.Menu(
                self.moduloGestion,
                tearoff = 0
            )

            self.clickDerecho.add_command(
                label = 'Eliminar cliente',
                command = lambda:self.__eliminarCliente(event)
            )
            self.clickDerecho.add_command(
                label = 'Verificar cliente'
            )
            self.clickDerecho.add_separator()

            self.subMenuOrden = tk.Menu(self.clickDerecho)
            self.subMenuOrden.add_command(
                label = 'Fecha de registro A-Z',
                command = self.ordenarFechaRegistroAsc
            )
            self.subMenuOrden.add_command(
                label = 'Fecha de Registro Z-A',
                command = self.ordenarFechaRegistroDesc
            )
            self.subMenuOrden.add_command(
                label = 'Rut A-Z',
                command = self.ordenarRutAsc
            )
            self.subMenuOrden.add_command(
                label = 'Rut Z-A',
                command = self.ordenarRutDesc
            )
            self.subMenuOrden.add_command(
                label = 'Nombres A-Z',
                command = self.ordenarNombresAsc
            )
            self.subMenuOrden.add_command(
                label = 'Nombres Z-A',
                command = self.ordenarNombresDesc
            )
            self.subMenuOrden.add_command(
                label = 'Apellidos A-Z',
                command = self.ordenarApellidosAsc
            )
            self.subMenuOrden.add_command(
                label = 'Apellidos Z-A',
                command = self.ordenarApellidosDesc
            )

            self.subMenuFiltro = tk.Menu(self.clickDerecho)
            self.subMenuFiltro.add_command(
                label = 'Fecha de registro',
                command = self.__obtenerFechaRegistro
            )
            self.subMenuFiltro.add_command(
                label = 'Rut',
                command = self.__obtenerRut
            )
            self.subMenuFiltro.add_command(
                label = 'Nombres',
                command = self.__obtenerNombres
            )
            self.subMenuFiltro.add_command(
                label = 'Apellidos',
                command = self.__obtenerApellidos
            )
            self.subMenuFiltro.add_command(
                label = 'Nacionalidad',
                command = self.__obtenerNacionalidad
            )
            self.subMenuFiltro.add_command(
                label = 'Sexo',
                command = self.__obtenerSexo
            )
            self.subMenuFiltro.add_command(
                label = 'Region',
                command = self.__obtenerRegion
            )
            self.subMenuFiltro.add_command(
                label = 'Comuna',
                command = self.__obtenerComuna
            )
            self.subMenuFiltro.add_command(
                label = 'Direccion',
                command = self.__obtenerDireccion
            )
            self.subMenuFiltro.add_command(
                label = 'Nro. de domicilio',
                command = self.__obtenerNroDomicilio
            )
            self.subMenuFiltro.add_command(
                label = 'Fono',
                command = self.__obtenerFono
            )
            self.subMenuFiltro.add_command(
                label = 'E-mail',
                command = self.__obtenerEmail
            )




            self.clickDerecho.add_cascade(
                label = 'Ordenar por',
                menu = self.subMenuOrden
            )

            self.clickDerecho.add_cascade(
                label = 'Filtrar por',
                menu = self.subMenuFiltro
            )
                
            self.clickDerecho.add_command(
                label = 'Actualizar registros',
                command = lambda:self.__obtenerCliente(event)
            )
            self.treeView.bind('<Button-3>', self.operacionClick)
            self.treeView.bind('<Double-1>', self.__modificarCliente)
            #self.treeView.bind('<Return>', self.__modificar_cliente)
            #self.treeView.bind('<Delete>', self.__eliminarCliente)

            self.moduloGestion.bind('<F5>', self.__obtenerCliente)

            #self.lectura_configuracion_operacion()
            self.cambiarModoGestion()
            self.moduloGestion.mainloop()
        elif self.listBoxOperacion.get(
            self.listBoxOperacion.curselection()) == self.Operador.listaOperacion[2]:
            self.moduloVerificacion = tk.Tk()
            self.moduloVerificacion.configure(background = '#786271')
            self.moduloVerificacion.geometry('500x350')
            self.moduloVerificacion.title(self.Configuracion.nombreOperador)
            
            self.moduloVerificacion.bind(
                '<Escape>',
                self.cerrarModuloVerificacion
            )
            self.frameModuloVerificacion = tk.Frame(
                self.moduloVerificacion,
                background = '#FFFFFF'
            )
            self.frameModuloVerificacion.pack(
                fill = 'both', expand = True,
                padx = 10, pady = 15
            )
            self.labelFrameVerificacion = tk.LabelFrame(
                self.frameModuloVerificacion, text = 'Administrador',
                font = ('Ubuntu light', 14), relief = 'solid', bd = 1,
                foreground = '#786271', background = '#FFFFFF'
            )
            self.labelFrameVerificacion.pack(
                fill = 'both', expand = True, padx = 15, pady = 15
            )
            self.labelUsuarioAdmin = tk.Label(
                self.labelFrameVerificacion, text = '\n\nUsuario',
                font = ('Ubuntu light', 12), background = '#FFFFFF'
            )
            self.labelUsuarioAdmin.pack(expand = True)
            self.entryUsuarioAdmin = tk.Entry(
                self.labelFrameVerificacion, justify = 'center',
                relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                fg = '#000000', width = 30
            )
            self.entryUsuarioAdmin.pack(expand = True, padx = 20, pady = 8)

            self.labelContraseñaAdmin = tk.Label(
                self.labelFrameVerificacion, text = '\nContraseña ',
                font = ('Ubuntu light', 12), background = '#FFFFFF'
            )
            self.labelContraseñaAdmin.pack(expand = True)
            self.entryContraseñaAdmin = tk.Entry(
                self.labelFrameVerificacion, justify = 'center',
                relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                fg = '#000000', width = 30, show = '*'
            )
            self.entryContraseñaAdmin.pack(expand = True, padx = 20, pady = 8)
            self.frameConfirmacionAdmin = tk.Frame(
                self.moduloVerificacion, relief = 'flat', width = 40,
                background = '#D5A27C'
            )

            self.frameConfirmacionAdmin.pack(
                fill = 'both', expand = True, pady = 15, padx = 15
            )
            self.labelEnterAdmin = tk.Label(
                self.frameConfirmacionAdmin, text = 'Presione [ ENTER ] para ingresar',
                font = ('Ubuntu light', 14),
                foreground = '#FFFFFF', background = '#D5A27C'
            )
            self.labelEnterAdmin.pack(
                expand = True, pady = 15, padx = 15
            )
            self.moduloVerificacion.bind(
                '<Return>',
                self.iniciarSesionAdmin
            )
            self.moduloVerificacion.mainloop()


    def cerrarModuloRegistro(self, event):
        self.moduloRegistro.destroy()
    def cerrarModuloGestion(self, event):
        self.moduloGestion.destroy()
    def cerrarModuloModificacion(self, event):
        self.moduloModificacion.destroy()
    def cerrarModuloVerificacion(self, event):
        self.moduloVerificacion.destroy()


    def cargarDatos(self):
        self.Cliente.rut = self.entryRut.get().upper()
        self.Cliente.nombres = self.entryNombres.get().upper()
        self.Cliente.apellidos = self.entryApellidos.get().upper()
        self.Cliente.nacionalidad = self.entryNacionalidad.get().upper()
        self.Cliente.sexo = self.comboBoxSexo.get().upper()
        self.Cliente.fecNacimiento = str(
            self.comboBoxDia.get()+'/'+self.comboBoxMes.get().upper()+'/'+self.comboBoxAño.get()
            )
        self.Cliente.region = self.comboBoxRegion.get().upper()
        self.Cliente.comuna = self.entryComuna.get().upper()
        self.Cliente.direccion = self.entryDireccion.get().upper()
        self.Cliente.numeroDomicilio = self.entryNumeroDomicilio.get()
        self.Cliente.fono = self.entryFono.get()
        self.Cliente.email = self.entryEmail.get().upper()
    
    def __registrarCliente(self, event):
        try:
            self.labelEstado.configure(foreground = '#FF4861')
            if (
                self.entryRut.get() and self.entryNombres.get() and self.entryApellidos.get() and
                self.entryNacionalidad.get() and self.comboBoxSexo.get() and self.comboBoxDia.get() and
                self.comboBoxMes.get() and self.comboBoxAño.get() and self.comboBoxRegion.get() and
                self.entryComuna.get() and self.entryDireccion.get() and
                self.entryNumeroDomicilio.get() and
                self.entryFono.get() and self.entryEmail.get()
            ) == '':
                self.labelEstado['text'] = \
                    '    [ * ]  Los campos son obligatorios, vuelva a intentarlo'
            else:
                self.labelEstado['text'] = \
                    ''
                if '.' and '-' not in self.entryRut.get():
                    self.labelEstado['text'] = \
                        '    [ * ]  El rut debe tener formato [ 11.111.111-1]'
                    self.entryRut.delete(0, tk.END)
                else:
                    self.labelEstado['text'] = \
                        ''
                    if len(self.entryRut.get()) != 12:
                        self.labelEstado['text'] = \
                            '    [ * ]  El rut debe tener 12 caracteres'
                        self.entryRut.delete(0, tk.END)
                    else:
                        self.labelEstado['text'] = \
                            ''
                        if '@' and '.' not in self.entryEmail.get():
                            self.labelEstado['text'] = \
                                '    [ * ]  Email no valido'
                            self.entryEmail.delete(0, tk.END)

                        else:
                            self.labelEstado['text'] = \
                                ''
                            self.cargarDatos()
                            BaseDatos.cursorBaseDatos.execute(
                                '''
                                INSERT INTO cliente_gesv(
                                    fecha_registro, rut, nombres, apellidos, nacionalidad, sexo, fecha_nacimiento,
                                    region, comuna, direccion, nro_domicilio, fono, e_mail)
                                VALUES(CURRENT_TIMESTAMP,?,?,?,?,?,?,?,?,?,?,?,?)''',
                                (
                                    self.Cliente.rut, self.Cliente.nombres, self.Cliente.apellidos,
                                    self.Cliente.nacionalidad, self.Cliente.sexo, self.Cliente.fecNacimiento,
                                    self.Cliente.region, self.Cliente.comuna, self.Cliente.direccion,
                                    self.Cliente.numeroDomicilio, self.Cliente.fono, self.Cliente.email
                                )
                            )
                            BaseDatos.conexionBaseDatos.commit()
                            self.labelEstado.configure(foreground = '#0BD230')
                            self.labelEstado['text'] = \
                                '    [ + ]  Cliente registrado'
                            
                            self.entryRut.delete(0, tk.END)
                            self.entryNombres.delete(0, tk.END)
                            self.entryApellidos.delete(0, tk.END)
                            self.entryNacionalidad.delete(0, tk.END)
                            self.comboBoxSexo.set('')
                            self.comboBoxDia.set('')
                            self.comboBoxMes.set('')
                            self.comboBoxAño.set('')
                            self.comboBoxRegion.set('')
                            self.entryComuna.delete(0, tk.END)
                            self.entryDireccion.delete(0, tk.END)
                            self.entryNumeroDomicilio.delete(0, tk.END)
                            self.entryFono.delete(0, tk.END)
                            self.entryEmail.delete(0, tk.END)
                            self.__obtenerCliente(event)



        except Exception as e:
            e = str(e)
            BaseDatos.cursorBaseDatos.execute(
                '''
                INSERT INTO GESV(fecha_registro, errores)
                VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
            )
            BaseDatos.conexionBaseDatos.commit()
            
    def __obtenerCliente(self, event):
        registroCliente = self.treeView.get_children()
        for cliente in registroCliente:
            self.treeView.delete(cliente)

        filaCliente = BaseDatos.cursorBaseDatos.execute(
            'SELECT * FROM cliente_gesv ORDER BY fecha_registro ASC;'
        )

        for fila in filaCliente:
            self.treeView.insert(
                '', tk.END,
                values = (
                    fila[0], fila[1], fila[2], fila[3], fila[4],
                    fila[5], fila[6], fila[7], fila[8], fila[9],
                    fila[10], fila[11], fila[12]
                    )
                )
                    
        BaseDatos.conexionBaseDatos.commit()
    def __buscarCliente(self, event):
        rutCliente = str(self.entryBusqueda.get())
        seleccionCliente = []
        registrosCliente = self.treeView.get_children()

        if len(self.entryBusqueda.get()) == 0:
            self.__obtenerCliente(event)
        else:
            for cliente in registrosCliente:
                if (rutCliente.lower() or rutCliente.upper()) in self.treeView.item(cliente)['values']:
                    print(self.treeView.item(cliente)['values'])
                    seleccionCliente.append(cliente)
            for clientes in registrosCliente:
                self.treeView.delete(clientes)
            self.entryBusqueda.delete(0, tk.END) 
            clienteFila = BaseDatos.cursorBaseDatos.execute(
            'SELECT * FROM cliente_gesv WHERE rut = ?;',(rutCliente,))
            for fila in clienteFila:
                self.treeView.selection_set(self.treeView.insert(
                        '', tk.END,
                        values = (
                            fila[0], fila[1], fila[2], fila[3], fila[4],
                            fila[5], fila[6], fila[7], fila[8], fila[9],
                            fila[10], fila[11], fila[12]
                        )
                    )
                )
    def __eliminarCliente(self, event):
        try:
            confirmarEliminacion = messagebox.askyesno(
                title = 'Confirmar eliminacion',
                message = '¿Desea eliminar el Cliente seleccionado?'
                )
            
            if confirmarEliminacion == True:
                for clienteSeleccionado in self.treeView.selection():
                    BaseDatos.cursorBaseDatos.execute(
                        '''
                        DELETE FROM cliente_gesv
                        WHERE rut = ?''', (self.treeView.set(clienteSeleccionado, '#2'),))
                    self.treeView.delete(clienteSeleccionado)
                    messagebox.showinfo(
                        title = 'Cliente eliminado',
                        message = 'El Cliente ha sido eliminado correctamente'
                        )
            else:
                messagebox.showinfo(
                    title = 'Eliminacion cancelada',
                    message = 'La operacion ha sido cancelada'
                )
        except Exception as e:
            e = str(e)
            BaseDatos.cursorBaseDatos.execute(
                '''
                INSERT INTO GESV(fecha_registro, errores)
                VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
            )
            BaseDatos.conexionBaseDatos.commit()

            messagebox.showerror(
                title = 'El Cliente no ha sido seleccionado',
                message = 'Selecciona un Cliente e intentalo de nuevo')
        BaseDatos.conexionBaseDatos.commit()
        self.__obtenerCliente(event)
    def __modificarCliente(self, event):
        try:
            clienteSeleccionado = self.treeView.item(self.treeView.focus())
            rutCliente = clienteSeleccionado['values'][1]
            self.moduloModificacion = tk.Tk()
            self.moduloModificacion.configure(background = '#786271')
            self.moduloModificacion.geometry('500x700')
            self.moduloModificacion.title('Modulo de Modificación')
            self.moduloModificacion.bind(
                '<Escape>', self.cerrarModuloModificacion
            )
            
            self.frameModuloModificacion = tk.Frame(
                self.moduloModificacion, background = '#FFFFFF'
            )
            self.frameModuloModificacion.pack(
                fill = 'both', expand = True,
                padx = 10, pady = 15
            )
            self.labelFrameModificacion = tk.LabelFrame(
                self.frameModuloModificacion, text = f'Cliente {rutCliente}',
                font = ('Ubuntu light', 14), relief = 'solid', bd = 1,
                foreground = '#786271', background = '#FFFFFF'
            )
            self.labelFrameModificacion.pack(
                fill = 'x', expand = True, padx = 15, pady = 15
            )

            self.frameDatos = tk.Frame(
                    self.labelFrameModificacion, background = '#FFFFFF'
            )
            self.frameDatos.pack(
                fill = 'both', expand = True,
                padx = 10, pady = 15
            )

            self.entryFechaRegistroN = tk.Entry(
                self.frameDatos, justify = 'center',
                relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                fg = '#000000', width = 30
            )
            self.entryFechaRegistroN.pack(expand = True, padx = 20, pady = 5)
            self.entryFechaRegistroN.insert(0, clienteSeleccionado['values'][0])
            #self.entryFechaRegistroN.configure(state = tk.DISABLED)

            self.entryRutN = tk.Entry(
                self.frameDatos, justify = 'center',
                relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                fg = '#000000', width = 30
            )
            self.entryRutN.pack(expand = True, padx = 20, pady = 5)
            self.entryRutN.insert(0, clienteSeleccionado['values'][1])
            #self.entryRutN.configure(state = tk.DISABLED)

            self.entryNombresN = tk.Entry(
                self.frameDatos, justify = 'center',
                relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                fg = '#000000', width = 30
            )
            self.entryNombresN.pack(expand = True, padx = 20, pady = 5)
            self.entryNombresN.insert(0, clienteSeleccionado['values'][2])
            #self.entryNombresN.configure(state = tk.DISABLED)

            self.entryApellidosN = tk.Entry(
                self.frameDatos, justify = 'center',
                relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                fg = '#000000', width = 30
            )
            self.entryApellidosN.pack(expand = True, padx = 20, pady = 5)
            self.entryApellidosN.insert(0, clienteSeleccionado['values'][3])
            #self.entryApellidosN.configure(state = tk.DISABLED)

            self.entryNacionalidadN = tk.Entry(
                self.frameDatos, justify = 'center',
                relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                fg = '#000000', width = 30
            )
            self.entryNacionalidadN.pack(expand = True, padx = 20, pady = 5)
            self.entryNacionalidadN.insert(0, clienteSeleccionado['values'][4])
            #self.entryNacionalidadN.configure(state = tk.DISABLED)

            self.comboBoxSexoN = ttk.Combobox(
                self.frameDatos, justify = 'center',
                value = self.Cliente.listaSexo, font = ('Ubuntu light', 13),
                width = 28
            )
            self.comboBoxSexoN.pack(expand = True, padx = 20, pady = 5)
            self.comboBoxSexoN.insert(0, clienteSeleccionado['values'][5])
            self.comboBoxSexoN.configure(state = 'readonly')

            self.entryFechaNacimientoN = tk.Entry(
                self.frameDatos, justify = 'center',
                relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                fg = '#000000', width = 30
            )
            self.entryFechaNacimientoN.pack(expand = True, padx = 20, pady = 5)
            self.entryFechaNacimientoN.insert(0, clienteSeleccionado['values'][6])

            self.comboBoxRegionN = ttk.Combobox(
                self.frameDatos, justify = 'center',
                value = self.Cliente.listaRegion, font = ('Ubuntu light', 13),
                width = 28
            )
            self.comboBoxRegionN.pack(expand = True, padx = 10, pady = 8)
            self.comboBoxRegionN.insert(0, clienteSeleccionado['values'][7])
            self.comboBoxRegionN.configure(state = 'readonly')

            self.entryComunaN = tk.Entry(
                self.frameDatos, justify = 'center',
                relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                fg = '#000000', width = 30
            )
            self.entryComunaN.pack(expand = True, padx = 20, pady = 5)
            self.entryComunaN.insert(0, clienteSeleccionado['values'][8])
            #self.entryComunaN.configure(state = tk.DISABLED)

            self.entryDireccionN = tk.Entry(
                self.frameDatos, justify = 'center',
                relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                fg = '#000000',width = 30
            )
            self.entryDireccionN.pack(expand = True, padx = 20, pady = 5)
            self.entryDireccionN.insert(0, clienteSeleccionado['values'][9])
            #self.entryDireccionN.configure(state = tk.DISABLED)

            self.entryNumeroDomicilioN = tk.Entry(
                self.frameDatos, justify = 'center',
                relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                fg = '#000000', width = 30
            )
            self.entryNumeroDomicilioN.pack(expand = True, padx = 20, pady = 5)
            self.entryNumeroDomicilioN.insert(0, clienteSeleccionado['values'][10])
            #self.entryNumeroDomicilioN.configure(state = tk.DISABLED)

            self.entryFonoN = tk.Entry(
                self.frameDatos, justify = 'center',
                relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                fg = '#000000', width = 30
            )
            self.entryFonoN.pack(expand = True, padx = 20, pady = 5)
            self.entryFonoN.insert(0, clienteSeleccionado['values'][11])
            #self.entryFonoN.configure(state = tk.DISABLED)
                
            self.entryEmailN = tk.Entry(
                self.frameDatos, justify = 'center',
                relief = 'solid', bd = 1, font = ('Ubuntu light', 13),
                fg = '#000000', width = 30
            )
            self.entryEmailN.pack(expand = True, padx = 20, pady = 5)
            self.entryEmailN.insert(0, clienteSeleccionado['values'][12])
            #self.entryEmailN.configure(state = tk.DISABLED)
            self.frameConfirmacionModif = tk.Frame(
                self.frameModuloModificacion, relief = 'flat', width = 40,
                background = '#D5A27C'
            )

            self.frameConfirmacionModif.pack(
                fill = 'both', expand = True, pady = 15, padx = 15
            )
            self.labelEnterModif = tk.Label(
                self.frameConfirmacionModif, text = 'Presione [ ENTER ] para actualizar los datos',
                font = ('Ubuntu light', 14),
                foreground = '#FFFFFF', background = '#D5A27C'
            )
            self.labelEnterModif.pack(
                expand = True, pady = 15, padx = 15
            )
            self.moduloModificacion.bind(
                '<Return>',
                self.__efectuarModificacion
            )
            self.cambiarModoModificacion()

            self.moduloModificacion.mainloop()
        except Exception as e:
            e = str(e)
            BaseDatos.cursorBaseDatos.execute(
                '''
                INSERT INTO GESV(fecha_registro, errores)
                VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
            )
            BaseDatos.conexionBaseDatos.commit()
    def __efectuarModificacion(self, event):
        clienteSeleccionado = self.treeView.item(self.treeView.focus())
        rutCliente = clienteSeleccionado['values'][1]
        BaseDatos.cursorBaseDatos.execute(
            '''
            UPDATE cliente_gesv SET fecha_registro = ?, rut = ?, nombres = ?,
                                    apellidos = ?, nacionalidad = ?, sexo = ?,
                                    fecha_nacimiento = ?, region = ?, comuna = ?,
                                    direccion = ?, nro_domicilio = ?, fono = ?,
                                    e_mail = ?
            WHERE rut = ?;''', (
                (
                    self.entryFechaRegistroN.get(), self.entryRutN.get(),
                    self.entryNombresN.get(), self.entryApellidosN.get(),
                    self.entryNacionalidadN.get(), self.comboBoxSexoN.get(),
                    self.entryFechaNacimientoN.get(), self.comboBoxRegionN.get(),
                    self.entryComunaN.get(), self.entryDireccionN.get(),
                    self.entryNumeroDomicilioN.get(), self.entryFonoN.get(),
                    self.entryEmailN.get(), rutCliente
                )
            )
        )
        BaseDatos.conexionBaseDatos.commit()
        
        tk.messagebox.showinfo(
            title = 'Datos actualizados',
            message = 'Los datos han sido actualizados correctamente'
        )
        self.__obtenerCliente(event)
        self.moduloModificacion.destroy()


    def seleccionarCliente(self, event):
        try:
            clienteSeleccionado = self.treeView.item(self.treeView.focus())
            columna = self.treeView.identify_column(event.x)
            print('Columna', columna)

            if columna == '#1':
                cell_value = clienteSeleccionado['values'][0]
            elif columna == '#2':
                cell_value = clienteSeleccionado['values'][1]
            elif columna == '#3':
                cell_value = clienteSeleccionado['values'][2]
            elif columna == '#4':
                cell_value = clienteSeleccionado['values'][3]
            elif columna == '#5':
                cell_value = clienteSeleccionado['values'][4]
            elif columna == '#6':
                cell_value = clienteSeleccionado['values'][5]
            elif columna == '#7':
                cell_value = clienteSeleccionado['values'][6]
            elif columna == '#8':
                cell_value = clienteSeleccionado['values'][7]
            elif columna == '#9':
                cell_value = clienteSeleccionado['values'][8]
            elif columna == '#10':
                cell_value = clienteSeleccionado['values'][9]
            elif columna == '#11':
                cell_value = clienteSeleccionado['values'][10]
            elif columna == '#12':
                cell_value = clienteSeleccionado['values'][11]
            elif columna == '#13':
                cell_value = clienteSeleccionado['values'][12]
            print ('Valor seleccionado ', cell_value)
        except Exception as e:
            e = str(e)
            BaseDatos.cursorBaseDatos.execute(
                '''
                INSERT INTO GESV(fecha_registro, errores)
                VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
            )
            BaseDatos.conexionBaseDatos.commit()
    def operacionClick(self, event):
        try:
            self.clickDerecho.tk_popup(event.x_root, event.y_root)
        except Exception as e:
            e = str(e)
            BaseDatos.cursorBaseDatos.execute(
                '''
                INSERT INTO GESV(fecha_registro, errores)
                VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
            )
            BaseDatos.conexionBaseDatos.commit()
        finally:
            self.clickDerecho.grab_release()

    def ordenarFechaRegistroAsc(self):
        try:
            registroClientes = self.treeView.get_children()
            for cliente in registroClientes:
                self.treeView.delete(cliente)

            filasCliente = BaseDatos.cursorBaseDatos.execute(
                'SELECT * FROM cliente_gesv ORDER BY fecha_registro ASC;'
                )

            for fila in filasCliente:
                self.treeView.insert(
                    '',
                    tk.END,
                    values = (
                        fila[0], fila[1], fila[2], fila[3], fila[4],
                        fila[5], fila[6], fila[7], fila[8], fila[9],
                        fila[10], fila[11], fila[12])
                        )
                    
            BaseDatos.conexionBaseDatos.commit()
        except Exception as e:
            e = str(e)
            BaseDatos.cursorBaseDatos.execute(
                '''
                INSERT INTO GESV(fecha_registro, errores)
                VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
            )
            BaseDatos.conexionBaseDatos.commit()
    def ordenarRutAsc(self):
        try:
            registroClientes = self.treeView.get_children()
            for cliente in registroClientes:
                self.treeView.delete(cliente)

            filasCliente = BaseDatos.cursorBaseDatos.execute(
                'SELECT * FROM cliente_gesv ORDER BY rut ASC;'
                )

            for fila in filasCliente:
                self.treeView.insert(
                    '',
                    tk.END,
                    values = (
                        fila[0], fila[1], fila[2], fila[3], fila[4],
                        fila[5], fila[6], fila[7], fila[8], fila[9],
                        fila[10], fila[11], fila[12])
                        )
                    
            BaseDatos.conexionBaseDatos.commit()
        except Exception as e:
            e = str(e)
            BaseDatos.cursorBaseDatos.execute(
                '''
                INSERT INTO GESV(fecha_registro, errores)
                VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
            )
            BaseDatos.conexionBaseDatos.commit()
    def ordenarNombresAsc(self):
        try:
            registroClientes = self.treeView.get_children()
            for cliente in registroClientes:
                self.treeView.delete(cliente)

            filasCliente = BaseDatos.cursorBaseDatos.execute(
                'SELECT * FROM cliente_gesv ORDER BY nombres ASC;'
                )

            for fila in filasCliente:
                self.treeView.insert(
                    '',
                    tk.END,
                    values = (
                        fila[0], fila[1], fila[2], fila[3], fila[4],
                        fila[5], fila[6], fila[7], fila[8], fila[9],
                        fila[10], fila[11], fila[12])
                        )
                    
            BaseDatos.conexionBaseDatos.commit()
        except Exception as e:
            e = str(e)
            BaseDatos.cursorBaseDatos.execute(
                '''
                INSERT INTO GESV(fecha_registro, errores)
                VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
            )
            BaseDatos.conexionBaseDatos.commit()
    def ordenarApellidosAsc(self):
        try:
            registroClientes = self.treeView.get_children()
            for cliente in registroClientes:
                self.treeView.delete(cliente)

            filasCliente = BaseDatos.cursorBaseDatos.execute(
                'SELECT * FROM cliente_gesv ORDER BY apellidos ASC;'
                )

            for fila in filasCliente:
                self.treeView.insert(
                    '',
                    tk.END,
                    values = (
                        fila[0], fila[1], fila[2], fila[3], fila[4],
                        fila[5], fila[6], fila[7], fila[8], fila[9],
                        fila[10], fila[11], fila[12])
                        )
                    
            BaseDatos.conexionBaseDatos.commit()
        except Exception as e:
            e = str(e)
            BaseDatos.cursorBaseDatos.execute(
                '''
                INSERT INTO GESV(fecha_registro, errores)
                VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
            )
            BaseDatos.conexionBaseDatos.commit()

    def ordenarFechaRegistroDesc(self):
        try:
            registroClientes = self.treeView.get_children()
            for cliente in registroClientes:
                self.treeView.delete(cliente)

            filasCliente = BaseDatos.cursorBaseDatos.execute(
                'SELECT * FROM cliente_gesv ORDER BY fecha_registro DESC;'
                )

            for fila in filasCliente:
                self.treeView.insert(
                    '',
                    tk.END,
                    values = (
                        fila[0], fila[1], fila[2], fila[3], fila[4],
                        fila[5], fila[6], fila[7], fila[8], fila[9],
                        fila[10], fila[11], fila[12])
                        )
                    
            BaseDatos.conexionBaseDatos.commit()
        except Exception as e:
            e = str(e)
            BaseDatos.cursorBaseDatos.execute(
                '''
                INSERT INTO GESV(fecha_registro, errores)
                VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
            )
            BaseDatos.conexionBaseDatos.commit()
    def ordenarRutDesc(self):
        try:
            registroClientes = self.treeView.get_children()
            for cliente in registroClientes:
                self.treeView.delete(cliente)

            filasCliente = BaseDatos.cursorBaseDatos.execute(
                'SELECT * FROM cliente_gesv ORDER BY rut DESC;'
                )

            for fila in filasCliente:
                self.treeView.insert(
                    '',
                    tk.END,
                    values = (
                        fila[0], fila[1], fila[2], fila[3], fila[4],
                        fila[5], fila[6], fila[7], fila[8], fila[9],
                        fila[10], fila[11], fila[12])
                        )
                    
            BaseDatos.conexionBaseDatos.commit()
        except Exception as e:
            e = str(e)
            BaseDatos.cursorBaseDatos.execute(
                '''
                INSERT INTO GESV(fecha_registro, errores)
                VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
            )
            BaseDatos.conexionBaseDatos.commit()
    def ordenarNombresDesc(self):
        try:
            registroClientes = self.treeView.get_children()
            for cliente in registroClientes:
                self.treeView.delete(cliente)

            filasCliente = BaseDatos.cursorBaseDatos.execute(
                'SELECT * FROM cliente_gesv ORDER BY nombres DESC;'
                )

            for fila in filasCliente:
                self.treeView.insert(
                    '',
                    tk.END,
                    values = (
                        fila[0], fila[1], fila[2], fila[3], fila[4],
                        fila[5], fila[6], fila[7], fila[8], fila[9],
                        fila[10], fila[11], fila[12])
                        )
                    
            BaseDatos.conexionBaseDatos.commit()
        except Exception as e:
            e = str(e)
            BaseDatos.cursorBaseDatos.execute(
                '''
                INSERT INTO GESV(fecha_registro, errores)
                VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
            )
            BaseDatos.conexionBaseDatos.commit()
    def ordenarApellidosDesc(self):
        try:
            registroClientes = self.treeView.get_children()
            for cliente in registroClientes:
                self.treeView.delete(cliente)

            filasCliente = BaseDatos.cursorBaseDatos.execute(
                'SELECT * FROM cliente_gesv ORDER BY apellidos DESC;'
                )

            for fila in filasCliente:
                self.treeView.insert(
                    '',
                    tk.END,
                    values = (
                        fila[0], fila[1], fila[2], fila[3], fila[4],
                        fila[5], fila[6], fila[7], fila[8], fila[9],
                        fila[10], fila[11], fila[12])
                        )
                    
            BaseDatos.conexionBaseDatos.commit()
        except Exception as e:
            e = str(e)
            BaseDatos.cursorBaseDatos.execute(
                '''
                INSERT INTO GESV(fecha_registro, errores)
                VALUES(CURRENT_TIMESTAMP, ?)''', (e,)
            )
            BaseDatos.conexionBaseDatos.commit()

    def __obtenerFechaRegistro(self):
        registroCliente = self.treeView.get_children()
        for cliente in registroCliente:
            self.treeView.delete(cliente)

        filaCliente = BaseDatos.cursorBaseDatos.execute(
            'SELECT fecha_registro FROM cliente_gesv ORDER BY fecha_registro ASC;'
        )

        for fila in filaCliente:
            self.treeView.insert(
                '', tk.END,
                values = (fila[0],'')
                )
                    
        BaseDatos.conexionBaseDatos.commit()
    def __obtenerRut(self):
        registroCliente = self.treeView.get_children()
        for cliente in registroCliente:
            self.treeView.delete(cliente)

        filaCliente = BaseDatos.cursorBaseDatos.execute(
            'SELECT rut FROM cliente_gesv ORDER BY rut ASC;'
        )

        for fila in filaCliente:
            self.treeView.insert(
                '', tk.END,
                values = ('', fila[0])
                )
                    
        BaseDatos.conexionBaseDatos.commit()
    def __obtenerNombres(self):
        registroCliente = self.treeView.get_children()
        for cliente in registroCliente:
            self.treeView.delete(cliente)

        filaCliente = BaseDatos.cursorBaseDatos.execute(
            'SELECT nombres FROM cliente_gesv ORDER BY nombres ASC;'
        )

        for fila in filaCliente:
            self.treeView.insert(
                '', tk.END,
                values = ('', '', fila[0])
                )
                    
        BaseDatos.conexionBaseDatos.commit()
    def __obtenerApellidos(self):
        registroCliente = self.treeView.get_children()
        for cliente in registroCliente:
            self.treeView.delete(cliente)

        filaCliente = BaseDatos.cursorBaseDatos.execute(
            'SELECT apellidos FROM cliente_gesv ORDER BY apellidos ASC;'
        )

        for fila in filaCliente:
            self.treeView.insert(
                '', tk.END,
                values = ('', '', '', fila[0])
                )
                    
        BaseDatos.conexionBaseDatos.commit()
    def __obtenerNacionalidad(self):
        registroCliente = self.treeView.get_children()
        for cliente in registroCliente:
            self.treeView.delete(cliente)

        filaCliente = BaseDatos.cursorBaseDatos.execute(
            'SELECT nacionalidad FROM cliente_gesv ORDER BY nacionalidad ASC;'
        )

        for fila in filaCliente:
            self.treeView.insert(
                '', tk.END,
                values = ('', '', '', '', fila[0])
                )
                    
        BaseDatos.conexionBaseDatos.commit()
    def __obtenerSexo(self):
        registroCliente = self.treeView.get_children()
        for cliente in registroCliente:
            self.treeView.delete(cliente)

        filaCliente = BaseDatos.cursorBaseDatos.execute(
            'SELECT sexo FROM cliente_gesv ORDER BY sexo ASC;'
        )

        for fila in filaCliente:
            self.treeView.insert(
                '', tk.END,
                values = ('', '', '', '', '', fila[0])
                )
                    
        BaseDatos.conexionBaseDatos.commit()
    def __obtenerFechaNacimiento(self):
        registroCliente = self.treeView.get_children()
        for cliente in registroCliente:
            self.treeView.delete(cliente)

        filaCliente = BaseDatos.cursorBaseDatos.execute(
            'SELECT fecha_nacimiento FROM cliente_gesv ORDER BY fecha_nacimiento ASC;'
        )

        for fila in filaCliente:
            self.treeView.insert(
                '', tk.END,
                values = ('', '', '', '', '', '', fila[0])
                )
                    
        BaseDatos.conexionBaseDatos.commit()
    def __obtenerRegion(self):
        registroCliente = self.treeView.get_children()
        for cliente in registroCliente:
            self.treeView.delete(cliente)

        filaCliente = BaseDatos.cursorBaseDatos.execute(
            'SELECT region FROM cliente_gesv ORDER BY region ASC;'
        )

        for fila in filaCliente:
            self.treeView.insert(
                '', tk.END,
                values = ('', '', '', '', '', '', '', fila[0])
                )
                    
        BaseDatos.conexionBaseDatos.commit()
    def __obtenerComuna(self):
        registroCliente = self.treeView.get_children()
        for cliente in registroCliente:
            self.treeView.delete(cliente)

        filaCliente = BaseDatos.cursorBaseDatos.execute(
            'SELECT comuna FROM cliente_gesv ORDER BY comuna ASC;'
        )

        for fila in filaCliente:
            self.treeView.insert(
                '', tk.END,
                values = ('', '', '', '', '', '', '', '', fila[0])
                )
                    
        BaseDatos.conexionBaseDatos.commit()
    def __obtenerDireccion(self):
        registroCliente = self.treeView.get_children()
        for cliente in registroCliente:
            self.treeView.delete(cliente)

        filaCliente = BaseDatos.cursorBaseDatos.execute(
            'SELECT direccion FROM cliente_gesv ORDER BY direccion ASC;'
        )

        for fila in filaCliente:
            self.treeView.insert(
                '', tk.END,
                values = ('', '', '', '', '', '', '', '', '', fila[0])
                )
                    
        BaseDatos.conexionBaseDatos.commit()
    def __obtenerNroDomicilio(self):
        registroCliente = self.treeView.get_children()
        for cliente in registroCliente:
            self.treeView.delete(cliente)

        filaCliente = BaseDatos.cursorBaseDatos.execute(
            'SELECT nro_domicilio FROM cliente_gesv ORDER BY nro_domicilio ASC;'
        )

        for fila in filaCliente:
            self.treeView.insert(
                '', tk.END,
                values = ('', '', '', '', '', '', '', '', '', '', fila[0])
                )
                    
        BaseDatos.conexionBaseDatos.commit()
    def __obtenerFono(self):
        registroCliente = self.treeView.get_children()
        for cliente in registroCliente:
            self.treeView.delete(cliente)

        filaCliente = BaseDatos.cursorBaseDatos.execute(
            'SELECT fono FROM cliente_gesv ORDER BY fono ASC;'
        )

        for fila in filaCliente:
            self.treeView.insert(
                '', tk.END,
                values = ('', '', '', '', '', '', '', '', '', '', '', fila[0])
                )
                    
        BaseDatos.conexionBaseDatos.commit()
    def __obtenerEmail(self):
        registroCliente = self.treeView.get_children()
        for cliente in registroCliente:
            self.treeView.delete(cliente)

        filaCliente = BaseDatos.cursorBaseDatos.execute(
            'SELECT e_mail FROM cliente_gesv ORDER BY e_mail ASC;'
        )

        for fila in filaCliente:
            self.treeView.insert(
                '', tk.END,
                values = ('', '', '', '', '', '', '', '', '', '', '', '', fila[0])
                )
                    
        BaseDatos.conexionBaseDatos.commit()

    def iniciarSesionAdmin(self, event):
        if self.entryUsuarioAdmin.get() == '' or self.entryContraseñaAdmin.get() == '':
            tk.messagebox.showerror(
                'Campo vacio',
                'Complete todos los campos para iniciar sesión'
            )
            self.entryUsuarioAdmin.delete(0, tk.END)
            self.entryContraseñaAdmin.delete(0, tk.END)
        else:
            BaseDatos.cursorBaseDatos.execute(
                '''
                SELECT nombre_usuario AND contrasena
                FROM usuario
                WHERE nombre_usuario = ? AND contrasena = ?''',
                (self.entryUsuarioAdmin.get(), self.entryContraseñaAdmin.get())
            )
            inicioSesion = BaseDatos.cursorBaseDatos.fetchall()
            if inicioSesion:
                tk.messagebox.showinfo(
                    'Sesión iniciada',
                    f'Hola {self.entryUsuarioAdmin.get()}'
                )
                self.entryUsuarioAdmin.delete(0, tk.END)
                self.entryContraseñaAdmin.delete(0, tk.END)
                self.moduloVerificacion.destroy()
                self.sesionAdmin(event)
    def sesionAdmin(self, event):
        self.moduloAdministrador = tk.Tk()
        self.moduloAdministrador.configure(background = '#786271')
        self.moduloAdministrador.geometry('1200x400')
        self.moduloAdministrador.title(self.Configuracion.nombreOperador)
        '''self.moduloAdministrador.bind(
            '<Escape>',
            self.cerrarModuloGestion
        )'''
        self.frameModuloAdmin = tk.Frame(
            self.moduloAdministrador,
            background = '#FFFFFF'
        )
        self.frameModuloAdmin.pack(
            fill = 'both', expand = True,
            padx = 10, pady = 15
        )
        self.labelFrameAdmin = tk.LabelFrame(
            self.frameModuloAdmin, text = 'Administrador',
            font = ('Ubuntu light', 14), relief = 'solid', bd = 1,
            foreground = '#786271', background = '#FFFFFF'
        )
        self.labelFrameAdmin.pack(
            fill = 'both', expand = True, padx = 15, pady = 15
        )

        self.frameTreeViewErrores = tk.Frame(self.labelFrameAdmin)
        self.frameTreeViewErrores.pack(
            fill = 'both', expand = True,
            padx = 10, pady = 15,
            side = tk.LEFT
        )
        self.frameTreeViewUsuario = tk.Frame(self.labelFrameAdmin)
        self.frameTreeViewUsuario.pack(
            fill = 'both', expand = True,
            padx = 10, pady = 15,
            side = tk.RIGHT
        )


        self.treeViewErrores = ttk.Treeview(
            self.frameTreeViewErrores, height = 58,
            column = ('#1','#2'), show = 'headings'
        )
            
        self.treeViewErrores.pack(
            fill = 'both', expand = True, side = tk.LEFT
        )
        self.treeViewErrores.heading(
            '#1', text = 'Fecha de Registro', anchor = tk.CENTER
        )
        self.treeViewErrores.heading(
            '#2', text = 'Descripcion', anchor = tk.CENTER
        )

        self.treeViewErrores.column('#1', width = 80, anchor = 'w')
        self.treeViewErrores.column('#2', width = 100, anchor = 'center')

        self.__obtenerErrores(event)
        self.scrollBarTreeViewErrores_y = ttk.Scrollbar(
            self.treeViewErrores, orient = 'vertical',
            command = self.treeViewErrores.yview
        )
        self.scrollBarTreeViewErrores_y.pack(fill = 'y', side = tk.RIGHT)
        self.scrollBarTreeViewErrores_x = ttk.Scrollbar(
            self.treeViewErrores, orient = 'horizontal',
            command = self.treeViewErrores.xview
        )
        self.scrollBarTreeViewErrores_x.pack(fill = 'x', side = tk.BOTTOM)
        self.treeViewErrores.configure(
            yscrollcommand = self.scrollBarTreeViewErrores_y.set,
            xscrollcommand = self.scrollBarTreeViewErrores_x.set,
            style = 'Treeview'
        )



        self.treeViewUsuario = ttk.Treeview(
            self.frameTreeViewUsuario, height = 58,
            column = ('#1','#2','#3', '#4'), show = 'headings'
        )
            
        self.treeViewUsuario.pack(
            fill = 'both', expand = True, side = tk.LEFT
        )
        self.treeViewUsuario.heading(
            '#1', text = 'Fecha de Registro', anchor = tk.CENTER
        )
        self.treeViewUsuario.heading(
            '#2', text = 'Nombre de usuario', anchor = tk.CENTER
        )
        self.treeViewUsuario.heading(
            '#3', text = 'Contraseña', anchor = tk.CENTER
        )
        self.treeViewUsuario.heading(
            '#4', text = 'E-mail', anchor = tk.CENTER
        )
        self.treeViewUsuario.column('#1', width = 80, anchor = 'w')
        self.treeViewUsuario.column('#2', width = 100, anchor = 'center')
        self.treeViewUsuario.column('#3', width = 190, anchor = 'center')
        self.treeViewUsuario.column('#4', width = 190, anchor = 'center')

        self.__obtenerUsuario(event)
        self.scrollBarTreeViewUsuario_y = ttk.Scrollbar(
            self.treeViewUsuario, orient = 'vertical',
            command = self.treeViewUsuario.yview
        )
        self.scrollBarTreeViewUsuario_y.pack(fill = 'y', side = tk.RIGHT)
        self.scrollBarTreeViewUsuario_x = ttk.Scrollbar(
            self.treeViewUsuario, orient = 'horizontal',
            command = self.treeViewUsuario.xview
        )
        self.scrollBarTreeViewUsuario_x.pack(fill = 'x', side = tk.BOTTOM)
        self.treeViewUsuario.configure(
            yscrollcommand = self.scrollBarTreeViewUsuario_y.set,
            xscrollcommand = self.scrollBarTreeViewUsuario_x.set,
            style = 'Treeview'
        )
        self.moduloAdministrador.mainloop()
    def __obtenerErrores(self, event):
        registroErrores = self.treeViewErrores.get_children()
        for error in registroErrores:
            self.treeViewErrores.delete(error)

        filaError = BaseDatos.cursorBaseDatos.execute(
            'SELECT * FROM gesv ORDER BY fecha_registro ASC;'
        )

        for fila in filaError:
            self.treeViewErrores.insert(
                '', tk.END,
                values = (fila[0], fila[1])
            )
                    
        BaseDatos.conexionBaseDatos.commit()
    def __obtenerUsuario(self, event):
        registroUsuarios = self.treeViewUsuario.get_children()
        for usuario in registroUsuarios:
            self.treeViewUsuario.delete(usuario)

        filaUsuario = BaseDatos.cursorBaseDatos.execute(
            '''
            SELECT *
            FROM usuario
            GROUP BY nombre_usuario
            ORDER BY fecha_registro ASC;'''
        )

        for fila in filaUsuario:
            self.treeViewUsuario.insert(
                '', tk.END,
                values = (fila[0], fila[1], fila[2], fila[3])
            )
                    
        BaseDatos.conexionBaseDatos.commit()
if __name__ == '__main__':
    BaseDatos = BaseDatos()
    BaseDatos.iniciarServicios()
    modoClaro = True
    modoOscuro = False
    w = tk.Tk()
    app = Inicio(w)
    app.mainloop()
