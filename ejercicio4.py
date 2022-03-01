# Ingresar el nombre de un trabajador, el número de su turno en el que trabaja: mañana
# (1), tarde (2), o noche (3), y el numero de su categoría: (1) Obrero y (2) Empleado.
# Calcular el sueldo según su turno y categoría.

class Trabajador:
    __turnos = {1:'MAÑANA', 2:'TARDE', 3:'NOCHE'}
    __category = {1: 'OBRERO', 2: 'EMPLEADO'}
    def __init__(self, nombre, turno, categoria):
        self.nombre = nombre
        self.turno = turno
        self.categoria = categoria

    def category(self):
        if self.categoria in self.__category:
            return self.__category[self.categoria]
        else:
            return "Ingreso un dato incorrecto"

    def turnos(self):
        if self.turno in self.__turnos:
            return self.__turnos[self.turno]
        else:
            "ingreso un dato incorrecto" 

    def sueldo(self):
        if self.__category[self.categoria] == 'OBRERO':
            if self.__turnos[self.turno] == 'MAÑANA':
                return 600
            elif self.__turnos[self.turno]  == 'TARDE':
                return 800
            elif self.__turnos[self.turno]  == 'NOCHE':
                return 1200 
        elif self.__category[self.categoria] == 'EMPLEADO':
            if self.__turnos[self.turno]  == 'MAÑANA':
                return 850
            elif self.__turnos[self.turno]  == 'TARDE':
                return 1000
            elif self.__turnos[self.turno] == 'NOCHE':
                return 1500

    def __str__(self):
        return "==========================================\n""SUELDO A PAGAR SEGUN SU CATEGORIA Y TURNO\n" \
               f"NOMBRE:\t\t {self.nombre}\n" \
               f"CATEGORIA:\t {self.category()}\n" \
               f"TURNO:\t\t {self.turnos()}\n" \
               f"SUELDO:\t\t {self.sueldo()}"   

nombre = input("ingrese nombre del trabajador: ").upper()
print("===========ESCOJA UNA CATEGORIA================\n" "1 OBRERO\n" "2 EMPLEADO")
categoria = int(input("Escoja que categoría pertenece: "))
print("===========ESCOJA EL TURNO================\n" "1 DIA\n" "2 TARDE\n" "3 NOCHE")
turno = int(input("Seleccione a que turno pertenece: "))

trabajador1 = Trabajador(nombre, turno, categoria)
print(trabajador1)