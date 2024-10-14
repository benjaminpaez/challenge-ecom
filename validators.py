def validar_no_vacio(valor):
    return bool(valor)


def validar_digitos(valor):
    return valor.isdigit()


def validar_num_float(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


def validar_grupo_etario(grupo_etario):
    valid_group_ages = ['<12', '18-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-99']
    return isinstance(grupo_etario, str) and grupo_etario in valid_group_ages


def validar_fecha(fecha):
    if len(fecha) != 10 or fecha[4] != '-' or fecha[7] != '-':
        return False
    year, month, day = fecha.split('-')
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False
    if not (1 <= int(month) <= 12 and 1 <= int(day) <= 31):
        return False
    return True
