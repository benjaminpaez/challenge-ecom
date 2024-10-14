from validators import (
    validar_no_vacio, validar_digitos, validar_num_float,
    validar_grupo_etario, validar_fecha
)


class VacunaData:
    LIMITE_EDAD = 60

    def __init__(self, file_path):
        self.file_path = file_path
        self.sexos = {}
        self.sexo_dict = {}
        self.jurisdicciones_dict = {}
        self.vacunas_dict = {}
        self.segunda_dosis_dict = {}
        self.total_vacunas = 0
        self.dosis_mayores = 0
        self.header = []

    def register_valid(self, data_result):
        if len(data_result) != len(self.header):
            return False

        registros_validos = {
            'sexo': lambda x: x in ['M', 'F'],
            'grupo_etario': validar_grupo_etario,
            'jurisdiccion_residencia': validar_no_vacio,
            'jurisdiccion_residencia_id': validar_digitos,
            'depto_residencia': validar_no_vacio,
            'depto_residencia_id': validar_digitos,
            'jurisdiccion_aplicacion': validar_no_vacio,
            'jurisdiccion_aplicacion_id': validar_digitos,
            'depto_aplicacion': validar_no_vacio,
            'depto_aplicacion_id': validar_digitos,
            'fecha_aplicacion': validar_fecha,
            'vacuna': validar_no_vacio,
            'cod_dosis_generica': validar_digitos,
            'nombre_dosis_generica': validar_no_vacio,
            'condicion_aplicacion': validar_no_vacio,
            'orden_dosis': validar_digitos,
            'lote_vacuna': validar_no_vacio,
            'id_persona_dw': validar_num_float
        }

        for campo, registro in registros_validos.items():
            if not registro(data_result[self.header.index(campo)]):
                return False

        return True

    def validate_arch(self):
        with open('reg_errores.txt', 'a', encoding='utf-8') as error_file:
            with open(self.file_path, 'r', encoding='utf-8') as arch:
                for index, row in enumerate(arch):
                    result = row.strip()
                    if index == 0:
                        self.header = self.formatter_list(result)
                        continue

                    data_result = self.formatter_list(result)
                    result_dict = dict(zip(self.header, data_result))

                    if not self.register_valid(data_result):
                        error_file.write(f"Registro defectuoso o incompleto en la fila {index + 1}: \n {result_dict} \n")
                    else:
                        self.procesar_datos(data_result)

    def procesar_datos(self, data_result):
        self.procesar_sexo(data_result[self.header.index('sexo')])
        self.procesar_jurisdiccion(data_result[self.header.index('jurisdiccion_residencia')],
                                   data_result[self.header.index('jurisdiccion_aplicacion')])
        self.procesar_vacunas(data_result[self.header.index('vacuna')])

        edad_mayor = self.procesar_edad(data_result[self.header.index('grupo_etario')])

        self.procesar_dosis(data_result[self.header.index('cod_dosis_generica')],
                            data_result[self.header.index('jurisdiccion_aplicacion')],
                            edad_mayor)

    def procesar_edad(self, edad_rango):
        edad_mayor = False
        if edad_rango.startswith('<') or edad_rango.startswith('>'):
            edad_value = int(edad_rango[1:])
            if edad_value > self.LIMITE_EDAD:
                edad_mayor = True
        else:
            min_edad, max_edad = map(int, edad_rango.split('-'))
            if min_edad > self.LIMITE_EDAD:
                edad_mayor = True
        return edad_mayor

    def procesar_sexo(self, sexo_type):
        if sexo_type not in self.sexo_dict:
            self.sexo_dict[sexo_type] = 0
        self.sexo_dict[sexo_type] += 1

    def procesar_jurisdiccion(self, residencia, aplicacion):
        if residencia not in self.jurisdicciones_dict:
            self.jurisdicciones_dict[residencia] = 0
        self.jurisdicciones_dict[residencia] += 1

        if aplicacion not in self.jurisdicciones_dict:
            self.jurisdicciones_dict[aplicacion] = 0
        self.jurisdicciones_dict[aplicacion] += 1

    def procesar_vacunas(self, vacuna):
        if vacuna not in self.vacunas_dict:
            self.vacunas_dict[vacuna] = 0
        self.vacunas_dict[vacuna] += 1
        self.total_vacunas += 1

    def procesar_dosis(self, dosis, jurisdiccion_aplicacion, edad_mayor):
        if dosis == '14' and edad_mayor:
            self.dosis_mayores += 1
        if dosis == '3':
            if jurisdiccion_aplicacion not in self.segunda_dosis_dict:
                self.segunda_dosis_dict[jurisdiccion_aplicacion] = 0
            self.segunda_dosis_dict[jurisdiccion_aplicacion] += 1

    @staticmethod
    def formatter_list(row):
        return row.split(',')
