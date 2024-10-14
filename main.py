from vacuna_data import VacunaData

class MenuEstadistico:
    def __init__(self, processor):
        self.processor = processor
        self.processed = False
        self.options = {
            "1": self.process_file,
            "2": self.mostrar_por_genero,
            "3": self.mostrar_vacunas_tipo,
            "4": self.mostrar_dosis_jurisdiccion,
            "5": self.mostrar_segdosis_jurisdiccion,
            "6": self.mostrar_refuerzos_mayores,
            "0": self.exit_menu
        }

    def show_menu(self):
        print("\n" + "-" * 35)
        print(" Menú de Resultados".center(35))
        print("-" * 35)

        if not self.processed:
            print("1. Procesar archivo de datos (obligatorio)")
        else:
            print("2. Mostrar distribución por género")
            print("3. Mostrar vacunas aplicadas por tipo")
            print("4. Mostrar dosis por jurisdicción de residencia")
            print("5. Personas con segunda dosis por jurisdicción")
            print("6. Personas mayores de 60 con dosis de refuerzo")
        print("0. Salir")
        print("-" * 35)

    def run(self):
        while True:
            self.show_menu()
            option = input("Seleccione una opción: ")
            self.run_option(option)

    def run_option(self, option):
        if option in self.options:
            self.options[option]()
        else:
            print("Opción inválida, intente nuevamente.")

    def process_file(self):
        if not self.processed:
            print("\nProcesando archivo ...")
            self.processor.validate_arch()
            self.processed = True
            print("Archivo procesado exitosamente")
        else:
            print("El archivo ya ha sido procesado.")

    def mostrar_por_genero(self):
        if self.processed:
            print("\nMostrar dosis aplicadas por género")
            for sexo, cantidad in self.processor.sexo_dict.items():
                print(f"{sexo}: {cantidad}")
        else:
            print("Error. Primero debe procesar el archivo")

    def mostrar_vacunas_tipo(self):
        if self.processed:
            total = sum(self.processor.vacunas_dict.values())
            print("\nMostrar vacunas aplicadas por tipo")
            for vacuna, cantidad in self.processor.vacunas_dict.items():
                porcentaje = (cantidad / total) * 100
                print(f"{vacuna}: {porcentaje:.2f}%")
        else:
            print("Error. Primero debe procesar el archivo")

    def mostrar_dosis_jurisdiccion(self):
        if self.processed:
            print("\nMostrar dosis aplicacdas por jurisdicción de residencia")
            for jurisdiccion, cantidad in self.processor.jurisdicciones_dict.items():
                print(f"{jurisdiccion}: {cantidad} dosis")
        else:
            print("Error. Primero debe procesar el archivo")

    def mostrar_segdosis_jurisdiccion(self):
        if self.processed:
            print("\nMostrar cantidad de personas con segunda dosis por jurisdicción")
            for jurisdiccion, cantidad in self.processor.segunda_dosis_dict.items():
                print(f"{jurisdiccion}: {cantidad} personas")
        else:
            print("Error. Primero debe procesar el archivo")

    def mostrar_refuerzos_mayores(self):
        if self.processed:
            print("\nMostrar dosis  de refuerzo aplicacdas a mayores de 60 años")
            print(f"{self.processor.dosis_mayores} personas mayores de 60 recibieron dosis de refuerzo")
        else:
            print("Error. Primero debe procesar el archivo")

    def exit_menu(self):
        print("Gracias por utilizar este programa!")
        print("Creado por Benjamin Paez")
        exit()


if __name__ == "__main__":
    archivo = VacunaData('datos_nomivac_parte1.csv')
    menu = MenuEstadistico(archivo)
    menu.run()
