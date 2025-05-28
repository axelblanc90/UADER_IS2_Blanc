import copy

# ------------------------------------------
# 1. Singleton - Cálculo de factorial
# ------------------------------------------
class FactorialSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FactorialSingleton, cls).__new__(cls)
        return cls._instance

    def calcular(self, n):
        if n < 0:
            raise ValueError("No se puede calcular el factorial de un número negativo")
        if n == 0 or n == 1:
            return 1
        return n * self.calcular(n - 1)

# ------------------------------------------
# 2. Clase de cálculo de impuestos
# ------------------------------------------
class CalculadoraImpuestos:
    def calcular_total(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones = base_imponible * 0.012
        return base_imponible + iva + iibb + contribuciones

# ------------------------------------------
# 3. Strategy - Entrega de hamburguesa
# ------------------------------------------
class Entrega:
    def entregar(self):
        pass

class EntregaMostrador(Entrega):
    def entregar(self):
        print("Entregada en mostrador")

class RetiroCliente(Entrega):
    def entregar(self):
        print("Retirada por el cliente")

class Delivery(Entrega):
    def entregar(self):
        print("Enviada por delivery")

class Hamburguesa:
    def __init__(self, metodo_entrega: Entrega):
        self.metodo_entrega = metodo_entrega

    def entregar(self):
        self.metodo_entrega.entregar()

# ------------------------------------------
# 4. Factory Method - Factura según condición impositiva
# ------------------------------------------
class Factura:
    def __init__(self, importe):
        self.importe = importe

    def mostrar(self):
        pass

class FacturaResponsable(Factura):
    def mostrar(self):
        print(f"Factura A - Responsable Inscripto - Total: {self.importe}")

class FacturaNoInscripto(Factura):
    def mostrar(self):
        print(f"Factura C - No Inscripto - Total: {self.importe}")

class FacturaExento(Factura):
    def mostrar(self):
        print(f"Factura E - IVA Exento - Total: {self.importe}")

class FacturaFactory:
    def crear_factura(self, tipo, importe):
        if tipo == "Responsable":
            return FacturaResponsable(importe)
        elif tipo == "NoInscripto":
            return FacturaNoInscripto(importe)
        elif tipo == "Exento":
            return FacturaExento(importe)
        else:
            raise ValueError("Tipo de factura no válido")

# ------------------------------------------
# 5. Builder - Construcción de un avión
# ------------------------------------------
class Avion:
    def __init__(self):
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def mostrar_partes(self):
        print("Partes del avión:", self.partes)

class AvionBuilder:
    def __init__(self):
        self.avion = Avion()

    def construir_body(self):
        self.avion.agregar_parte("Body")

    def construir_turbinas(self):
        self.avion.agregar_parte("Turbina 1")
        self.avion.agregar_parte("Turbina 2")

    def construir_alas(self):
        self.avion.agregar_parte("Ala 1")
        self.avion.agregar_parte("Ala 2")

    def construir_tren_aterrizaje(self):
        self.avion.agregar_parte("Tren de aterrizaje")

    def obtener_avion(self):
        return self.avion

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir_avion_completo(self):
        self.builder.construir_body()
        self.builder.construir_turbinas()
        self.builder.construir_alas()
        self.builder.construir_tren_aterrizaje()
        return self.builder.obtener_avion()

# ------------------------------------------
# 6. Prototype - Clonado de objetos
# ------------------------------------------
class Prototipo:
    def clonar(self):
        return copy.deepcopy(self)

class Producto(Prototipo):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(f"Producto: {self.nombre}")

# ------------------------------------------
# 7. Abstract Factory - Interfaz para diferentes SO
# ------------------------------------------
class Boton:
    def render(self):
        pass

class BotonWindows(Boton):
    def render(self):
        print("Renderizando botón en Windows")

class BotonLinux(Boton):
    def render(self):
        print("Renderizando botón en Linux")

class FabricaAbstracta:
    def crear_boton(self):
        pass

class FabricaWindows(FabricaAbstracta):
    def crear_boton(self):
        return BotonWindows()

class FabricaLinux(FabricaAbstracta):
    def crear_boton(self):
        return BotonLinux()

def crear_ui(fabrica: FabricaAbstracta):
    boton = fabrica.crear_boton()
    boton.render()

# ------------------------------------------
# TEST DE TODAS LAS CLASES
# ------------------------------------------
if __name__ == "__main__":
    # 1. Singleton - Factorial
    factorial = FactorialSingleton()
    print("Factorial de 5:", factorial.calcular(5))

    # 2. Impuestos
    imp = CalculadoraImpuestos()
    print("Importe con impuestos:", imp.calcular_total(1000))

    # 3. Hamburguesa con método de entrega
    h1 = Hamburguesa(EntregaMostrador())
    h2 = Hamburguesa(RetiroCliente())
    h3 = Hamburguesa(Delivery())
    h1.entregar()
    h2.entregar()
    h3.entregar()

    # 4. Factura según condición
    factory = FacturaFactory()
    f1 = factory.crear_factura("Responsable", 1200)
    f2 = factory.crear_factura("NoInscripto", 950)
    f3 = factory.crear_factura("Exento", 800)
    f1.mostrar()
    f2.mostrar()
    f3.mostrar()

    # 5. Builder de Avión
    builder = AvionBuilder()
    director = Director(builder)
    avion = director.construir_avion_completo()
    avion.mostrar_partes()

    # 6. Prototype
    prod1 = Producto("Smartphone")
    prod2 = prod1.clonar()
    prod2.mostrar()

    # 7. Abstract Factory
    print("UI para Windows:")
    crear_ui(FabricaWindows())
    print("UI para Linux:")
    crear_ui(FabricaLinux())
