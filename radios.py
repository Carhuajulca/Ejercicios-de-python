# hacer un programa para que ingrese el radio de un circulo y se reporte su área y longitud de la circuferencia
__pi = 3.1416
def area(r):

    are = __pi * r**2
    return are

def longitud(r):
    longi = 2 * __pi * r
    return longi

r = float(input("Ingrese un número: "))
area_circulo = area(r)
longitud_circulo = longitud(r)

print(f"el area del circulo es: {area_circulo:.2f}\n" f"la longitud es {longitud_circulo:.2f}")