# Crear clase de la base de datos
class BaseDatosauto:
    # Constructor
    def __init__(self):
        self.auto_lista = []

    def crear_un_auto(self, nuevo_auto):
        self.auto_lista.append(nuevo_auto)
        # Mera mente decorativo
        print("✅ auto creado con éxito.\n")

    def eliminar_auto(self, indice):
        if 0 <= indice < len(self.auto_lista):  # ✅ usa número 0, no la letra o
            self.auto_lista.pop(indice)
            # Condición simple meramente visual
            print("🗑️ el auto fue eliminado correctamente.\n")
        else:
            print("❌ No se encontró un auto registrado con ese número.\n")

    def mostrar_informacion(self):
        if not self.auto_lista:
            print("⚠️ No hay autos creados.\n")
            return

        for i, auto in enumerate(self.auto_lista):  # ✅ usa variable en minúscula
            print(f"\nAuto N° {i}")
            auto.mostrar_info()  # ✅ usa el método correcto de las clases hijas
