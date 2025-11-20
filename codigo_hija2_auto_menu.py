from codigo_auto_menu import Autos

class Auto_Audi_A6(Autos):
    def __init__(self, modelo, color, motor, numero_de_puertas, capasidad_de_pasajero, tipo_de_combustible, precio_autos):
        super().__init__(modelo, color, motor, numero_de_puertas, capasidad_de_pasajero, tipo_de_combustible)
        self.precio_autos = precio_autos

    def reutilizacion(self):
        print(f"el modelo del auto {self.modelo} se actualizó")

    def valor_del_coche(self):
        print(f"el precio del coche es: {self.precio_autos}")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"precio: {self.precio_autos}")