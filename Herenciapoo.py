# Clase Padre: Vehiculo
class Vehiculo:
    def __init__(self, marca, num_ruedas):
        self.marca = marca
        self.num_ruedas = num_ruedas

    def moverse(self):
        print(f"El vehículo de marca {self.marca} se está moviendo.")

# Subclase Automovil que hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca, num_ruedas, tipo_motor):
        super().__init__(marca, num_ruedas)  # Llamamos al constructor de la clase padre
        self.tipo_motor = tipo_motor         # Atributo específico de Automovil

    def moverse(self):
        print(f"El automóvil de marca {self.marca} con motor {self.tipo_motor} está conduciendo en la carretera.")

# Subclase Motocicleta que hereda de Vehiculo
class Motocicleta(Vehiculo):
    def __init__(self, marca, num_ruedas, cilindrada):
        super().__init__(marca, num_ruedas)  # Llamamos al constructor de la clase padre
        self.cilindrada = cilindrada         # Atributo específico de Motocicleta

    def moverse(self):
        print(f"La motocicleta de marca {self.marca} con cilindrada {self.cilindrada}cc está acelerando en la autopista.")

# Función que recibe un vehículo y llama a su método moverse
def mover_vehiculo(vehiculo):
    vehiculo.moverse()

# Pruebas con un Automovil y una Motocicleta
vehiculo1 = Automovil("Toyota", 4, "Gasolina")
vehiculo2 = Motocicleta("Yamaha", 2, 150)

mover_vehiculo(vehiculo1)  # Automóvil
mover_vehiculo(vehiculo2)  # Motocicleta
