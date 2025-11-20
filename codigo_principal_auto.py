from codigo_hija_auto_menu import Auto_BMW_serie_5
from codigo_hija2_auto_menu import Auto_Audi_A6
from base_datos_auto import BaseDatosauto

# Crear instancia de la base de datos
bads = BaseDatosauto()

# ====== Funciones ======

def crear_auto():
    print("\n🚗 Crear un nuevo auto")
    print("1. BMW Serie 5")
    print("2. Audi A6")
    tipo = input("Seleccione el tipo de auto (1 o 2): ")

    modelo = input("Modelo: ")
    color = input("Color: ")
    motor = input("Motor: ")
    numero_de_puertas = input("Número de puertas: ")
    capacidad_de_pasajeros = input("Capacidad de pasajeros: ")
    tipo_de_combustible = input("Tipo de combustible: ")

    if tipo == "1":
        compañia = input("Compañía del modelo: ")
        nuevo_auto = Auto_BMW_serie_5(
            modelo,
            color,
            motor,
            numero_de_puertas,
            capacidad_de_pasajeros,
            tipo_de_combustible,
            compañia
        )
    elif tipo == "2":
        precio = input("Precio del auto: ")
        nuevo_auto = Auto_Audi_A6(
            modelo,
            color,
            motor,
            numero_de_puertas,
            capacidad_de_pasajeros,
            tipo_de_combustible,
            precio
        )
    else:
        print("❌ Opción inválida.")
        return

    bads.crear_un_auto(nuevo_auto)


def mostrar_autos():
    print("\n📋 Autos registrados:")
    bads.mostrar_informacion()


def eliminar_auto():
    mostrar_autos()
    try:
        indice = int(input("\nIngrese el número del auto que desea eliminar: "))
        bads.eliminar_auto(indice)
    except ValueError:
        print("⚠️ Por favor, ingrese un número válido.")


# ====== MENÚ PRINCIPAL ======

while True:
    print("\n====== 🚘 MENÚ DE AUTOS ======")
    print("1. Crear un auto")
    print("2. Mostrar autos")
    print("3. Eliminar un auto")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_auto()
    elif opcion == "2":
        mostrar_autos()
    elif opcion == "3":
        eliminar_auto()
    elif opcion == "4":
        print("programa finalizado 😴")
        break
    else:
        print("❌ Opción no válida. Intente nuevamente.")
