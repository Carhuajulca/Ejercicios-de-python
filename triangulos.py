class Triangulo:
    def __init__(self, l1, l2, l3):
        self.lado1 = l1
        self.lado2 = l2
        self.lado3 = l3

    def tipos(self):
        if self.lado1 == self.lado2 & self.lado1 == self.lado3:
            return 'Es un triángulo equilátero'
        elif self.lado1 != self.lado2 & self.lado1 != self.lado3 & self.lado2 != self.lado3:
            return 'Es un triángulo escaleno'
        else:
            return 'Es un triángulo isósceles'

triangulo = Triangulo(l1=int(input('ingrese un valor:')),
                    l2=int(input('ingrese otro valor:')),
                    l3=int(input('ingrese el ultimo valor:')))
print(triangulo.tipos())

# GESLER CARHUAJULCA GARCIA 