# challenge-ecom
Código sobre el desafío integrador - 1er Parte

Explicación del codigo fuente

1. **Archivo `vacuna_data.py`**

Este archivo contiene la clase `VacunaData`, que gestiona y procesa datos relacionados con la vacunación. A continuación se explican sus partes principales:

- **Atributos de Clase**:
  - `LIMITE_EDAD`: Valor constante que define la edad límite (60 años).
  - `file_path`: Ruta del archivo CSV que contiene los datos.
  - `sexo_dict`, `jurisdicciones_dict`, `vacunas_dict`, `segunda_dosis_dict`: Diccionarios que almacenan información sobre sexo, jurisdicciones, tipos de vacunas y segundas dosis, respectivamente.
  - `total_vacunas`: Contador total de vacunas aplicadas.
  - `dosis_mayores`: Contador de dosis aplicadas a personas mayores de 60 años.
  - `header`: Lista que almacena los encabezados de las columnas del archivo.

- **Métodos Principales**:
  - `register_valid`: Valida que los datos de cada fila cumplan con ciertas reglas (por ejemplo, que no estén vacíos y que los valores sean correctos).
  - `validate_arch`: Abre el archivo CSV y procesa cada fila. Registra errores en un archivo si los datos son defectuosos.
  - `procesar_datos`: Llama a otros métodos para procesar información específica como sexo, jurisdicción, vacunas y dosis.
  - `procesar_sexo`, `procesar_jurisdiccion`, `procesar_vacunas`, `procesar_dosis`: Estos métodos manejan los datos específicos y los cuentan o almacenan en sus respectivos diccionarios.
  - `formatter_list`: Convierte una fila del archivo en una lista de valores.

2. **Archivo `validators.py`**

Este archivo contiene funciones que validan diferentes tipos de datos. 

- **Funciones de Validación**:
  - `validar_no_vacio`: Verifica que un valor no esté vacío.
  - `validar_digitos`: Comprueba que un valor contenga solo dígitos.
  - `validar_num_float`: Intenta convertir un valor a un número decimal (float) y verifica si es posible.
  - `validar_grupo_etario`: Valida que el grupo etario esté en una lista predefinida de grupos válidos.
  - `validar_fecha`: Comprueba que una fecha esté en el formato correcto (YYYY-MM-DD) y que los valores de mes y día sean válidos.
Estructura del Código
Importación de Clases: Se importa la clase VacunaData, que se encargará de procesar los datos de vacunación.

2. **Archivo `main.py`**

Clase MenuEstadistico:

- `Inicialización (__init__)`:
Se recibe un objeto processor, que es una instancia de VacunaData para procesar los datos.
Se define un diccionario options que asocia números a métodos que mostrarán diferentes estadísticas.
Métodos:

- `show_menu`: Muestra el menú de opciones disponibles. Si el archivo no ha sido procesado, solo permite procesar el archivo; de lo contrario, muestra todas las opciones.
- `run`: Un bucle que muestra el menú y permite al usuario seleccionar una opción. Llama al método run_option con la opción elegida.
- `run_option`: Ejecuta la función correspondiente a la opción seleccionada.
- `process_file`: Procesa el archivo de datos solo una vez. Si ya ha sido procesado, informa al usuario.
- `mostrar_por_genero`: Muestra el número de dosis aplicadas por género. Solo se ejecuta si el archivo ha sido procesado.
- `mostrar_vacunas_tipo`: Muestra el porcentaje de vacunas aplicadas por tipo, basado en el total.
- `mostrar_dosis_jurisdiccion`: Muestra cuántas dosis se han aplicado por jurisdicción de residencia.
- `mostrar_segdosis_jurisdiccion`: Muestra la cantidad de personas que han recibido una segunda dosis por jurisdicción.
- `mostrar_refuerzos_mayores`: Informa cuántas personas mayores de 60 años han recibido dosis de refuerzo.
- `exit_menu`: Finaliza el programa y muestra un mensaje de agradecimiento.
Ejecución Principal:

Se crea una instancia de VacunaData con un archivo CSV que contiene los datos de vacunación.
Se inicializa el menú estadístico y se ejecuta el método run, que inicia la interacción con el usuario.

**ACLARACION**
- El programa se realizo utilizando el arhcivo csv llamado **'datos_nomivac_parte1.csv'** 

**`Para ejecutar el programa`**
- En la carpeta del proyecto, ejecutar el comando `python .\main.py` para iniciar el menu iterativo del programa.
