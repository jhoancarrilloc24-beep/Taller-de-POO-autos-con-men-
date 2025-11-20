class Autos:
    def __init__(self, modelo, color, motor, numero_de_puertas, capasidad_de_pasajero, tipo_de_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_de_puertas = numero_de_puertas
        self.capasidad_de_pasajero = capasidad_de_pasajero
        self.tipo_de_combustible = tipo_de_combustible

    def arranque(self):
        if self.motor:
            print("el auto arranca 🚗")
        else:
            print("el auto no arranca 🚗")

    def apagado(self):
        print("el motor del auto está apagado")

    def aceleracion_y_frenado(self):
        print("el auto acelera y frena bien")

    def sistema_de_direccion(self):
        print("el sistema de dirección funciona correctamente ✅")

    def climatizacion(self):
        print("la climatización (aire acondicionado) está funcionando")

    def tipo_de_seguridad(self):
        print("seguridad: puertas cerradas")

    def mostrar_info(self):
        print(f"modelo: {self.modelo}")
        print(f"color: {self.color}")
        print(f"motor: {self.motor}")
        print(f"numero de puertas: {self.numero_de_puertas}")
        print(f"capasidad de pasajero: {self.capasidad_de_pasajero}")
        print(f"tipo de combustible: {self.tipo_de_combustible}")
