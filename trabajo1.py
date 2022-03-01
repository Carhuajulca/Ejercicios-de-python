class Trabajador:
    def __init__(self, nombre, categoria, horas_ex, tardanza):
        self.nombre = nombre
        self.categoria = categoria
        self.horas = horas_ex
        self.tardanza = tardanza

    def __str__(self):
        return "================DATOS DE ENTRADA==================\n"\
               f"TRABAJADOR:\t\t {self.nombre}\n"\
               f"CATEGORIA:\t\t {self.categoria}\n"\
               f"HORAS EXTRAS:\t\t {self.horas}\n"\
               f"TARDANZA: (minutos)\t {self.tardanza}"              

        

class Boleta(Trabajador):
    __categoria = {'A': 3000, 'B': 2500, 'C': 2000}
    
    def __init__(self, nombre, categoria, horas, tardanza):
        super().__init__(nombre, categoria, horas, tardanza)

    def sueldo(self):
        if self.categoria in self.__categoria:
            return self.__categoria[self.categoria] 

    def descuento(self):
        if self.categoria in self.__categoria:
            self.pago_hora = self.__categoria[self.categoria]/240
            self.pago_min = self.pago_hora/60
            self.desc_tar = self.pago_min * self.tardanza
            return round(self.desc_tar,2) 

    def pago_horas_extras(self):
        if self.categoria in self.__categoria:
            self.pago_hora = self.__categoria[self.categoria]/240
            self.pag_horas_extras= self.pago_hora * self.horas
            return round(self.pag_horas_extras,2)

    def sueldo_neto(self):
        if self.categoria in self.__categoria:
            self.sueldo_net = self.__categoria[self.categoria]-self.desc_tar + self.pag_horas_extras
            return round(self.sueldo_net,2)

    def __str__(self):
        return "================ BOLETA DE PAGO ==================\n"\
               f"TRABAJADOR:\t\t {self.nombre}\n"\
               f"CATEGORIA:\t\t {self.categoria}\n"\
               f"SUELDO BASICO\t\t {self.sueldo()}\n"\
               f"DESCUENTO POR TARDANZA\t {self.descuento()}\n"\
               f"PAGO X HORAS EXTRAS\t {self.pago_horas_extras()}\n"\
               f"SUELDO NETO:\t\t {self.sueldo_neto()}"                    

nombre = input("Ingrese un nombre: ").upper()
print("===========ESCOJA UNA CATEGORIA================\n" "A\n" "B\n" "C")
categoria = input("Ingrese una categoría: ").upper()
horas = int(input("Ingrese el número horas extras: "))
tardanza = int(input("Ingrese la cantidad de minutos de tardanza acumulada: "))
        
t1 = Boleta(nombre, categoria, horas, tardanza)
print(t1)