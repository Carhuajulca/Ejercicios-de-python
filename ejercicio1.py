class Persona:
    def __init__(self,nombre, apellidos, dni):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni

class Vendedor(Persona):
    __sueldo = 1100
    __comision = 0.17
    def __init__(self, nombre, apellidos, dni, ventas):
        super().__init__(nombre, apellidos, dni)
        self.ventas = ventas

    def calcular(self):
        self.comision_v = self.__comision * self.ventas
        self.comision_t = self.__sueldo * self.comision_v
        return self.comision_t

    def sueldo_total(self):
        self.sueldo = self.__sueldo + self.comision_t
        return self.sueldo

    def __str__(self):
        return "\n" \
               f"VENDEDOR:\t\t {self.nombre} {self.apellidos}\n" \
               f"DNI:\t\t\t {self.dni}\n" \
               f"SUELDO:\t\t\t {self.__sueldo}\n" \
               f"COMISIÓN X VENTAS\t {self.calcular()}\n" \
               f"SUELDO NETO\t\t {self.sueldo_total()}"

nVentas = int(input('INGRESE NÙMERO DE VENTAS: '))

vendedor1 = Vendedor('GESLER', 'CARHUAJULCA', 7021011, nVentas)
print(vendedor1)