from codigo_auto_menu import Autos

class Auto_BMW_serie_5(Autos):
    def __init__(self, modelo, color, motor, numero_de_puertas, capasidad_de_pasajero, tipo_de_combustible, compañia):
        super().__init__(modelo, color, motor, numero_de_puertas, capasidad_de_pasajero, tipo_de_combustible)
        self.compañia = compañia

    def luces(self):
        print("las luces están en buen estado y funcionan")

    def sistema_de_ventanas(self):
        print(f"se realizaron unas pruebas de las ventanas del auto {self.modelo}")

    def la_empresa_del_modelo(self):
        print(f"la empresa encargada del modelo es {self.compañia}")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"compañia: {self.compañia}")