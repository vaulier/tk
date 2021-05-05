class Cliente:
    def __init__(self):
        self.rut = None
        self.nombres = None
        self.apellidos = None
        self.nacionalidad = None
        self.sexo = None
        self.fecNacimiento = None
        self.region = None
        self.comuna = None
        self.direccion = None
        self.numeroDomicilio = None
        self.fono = None
        self.email = None

        self.listaFiltro = [
            'Rut', 'Nombre completo','E-mail',
            'Region','Comuna', 'Fono'
        ]
        self.listaRegion = [
            'Tarapaca', 'Antofagasta', 'Atacama', 'Coquimbo',
            'Valparaiso', 'Del Libertador B. OHiggins', 'Del Maule',
            'Del BioBio', 'La Araucania', 'Los Lagos',
            'Aysen del Gral C. Ibañez del Campo',
            'Magallanes y de la Antartica Chilena',
            'Metropolitana de Santiago',
            'Los Rios', 'Arica y Parinacota', 'Ñuble'
        ]
        self.listaSexo = [
            'Masculino', 'Femenino', 'Otro'
        ]
        self.listaDias = []
        self.listaMes = [
            'Enero', 'Febrero', 'Marzo','Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre','Octubre', 'Noviembre', 'Diciembre'
        ]
        self.listaAños = []
        self.listaOperacion = [
            'Registrar cliente', 'Gestionar cliente', 'Consola'
        ]
        self.listaCliente = []
        self.__insertarFechaComboBox()
    def __insertarFechaComboBox(self):
        for dia in range(1,32):
            self.listaDias.append(dia)
        for año in range(1901,2022):
            self.listaAños.append(año)
    
    def mostrarDatos(self):
        print(
            f'''
            rut                      {self.rut.upper()}
            nombre completo          {self.nombres.upper()} {self.apellidos.upper()}
            nacionalidad             {self.nacionalidad.upper()}
            sexo                     {self.sexo.upper()}
            fecha de nacimiento      {self.fecNacimiento.upper()}

            region                   {self.region.upper()}
            comuna                   {self.comuna.upper()}
            direccion                {self.direccion.upper()} #{self.numeroDomicilio}

            fono                     {self.fono}
            email                    {self.email.upper()}
            '''
        )