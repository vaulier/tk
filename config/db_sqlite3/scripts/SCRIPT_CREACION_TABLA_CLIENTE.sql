
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
            );