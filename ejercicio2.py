# from ejercicio1 import Persona

class Postulante(): 
    def __init__(self,nombre, apellidos, nota):
        self.nombre = nombre
        self.apellidos = apellidos
        self.puntaje = nota


    def carrerarofecional(self):
        if self.puntaje >=70 and self.puntaje <80:
            print("Tu puntaje solo alcanza para la carrera:\n" "ADMINISTRACION")
        elif self.puntaje >=80 and  self.puntaje < 90:
            print("Tu puntaje solo alcanza para la carrera:\n" "ADMINISTRACION\n" "INDUSTRIAL")
        elif self.puntaje >= 90 and self.puntaje < 100:
            print("Tu puntaje solo alcanza para la carrera:\n" "ADMINISTRACION\n" "INDUSTRIAL\n" "ELECTRONICA")
        elif self.puntaje >= 100 and self.puntaje <=120:
            print("Tu puntaje solo alcanza para la carrera:\n" "ADMINISTRACION\n" "INDUSTRIAL\n" "ELECTRONICA\n" "SISTEMAS")
        elif self.puntaje < 70:
            print("Necesitas estudiar más")
        else:
            print("Tu puntaje no alcanza la valla para ingresar a una carrera profesional")

puntuacion = int(input("Ingrese su putuación: "))
postulante1 = Postulante("Diego", "Torres", puntuacion)
postulante1.carrerarofecional()