# 3. Calcule el costo total de una hospitalización sabiendo el total de días y el costo de la
# habitación. El costo de la habitación será de acuerdo a la siguiente tabla:


class  Hospital:

    __costo = {'area 1': 150, 'area 2': 120, 'otros': 100}

    def __init__(self, dias,area):
        self.numdias = dias
        self.area = area

    def costo(self):
        if self.area in self.__costo:
            print('El total de los',self.numdias, 'días costará S/.', self.__costo[self.area]*self.numdias)
        else:
            print('No introdujo bien los datos')

dias = int(input('Ingrese la cantidad de días que estubo el paciente: '))
area = input('Ingrese el área donde se aloja el paciente: ').lower()

paciente = Hospital(dias, area)
paciente.costo()
