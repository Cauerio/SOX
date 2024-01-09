import random

class Persona():
    def __init__(self):
        self.edad = int(input("Cuantos años tienes?: "))
        self.sexo = input("Cual es tu genero?('H' o 'M'): ")
        self.dni = p.generador_dni()
        
    def generador_dni():
        numeros = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        letra = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        dni = numeros + letra
 

    def comprobaciones(self):
        # Comprobacion de la edad
        while self.edad == False:
            if self.edad >= 18:
                self.edad = True
                return self.edad
            else:
                self.edad = False
                print ("Tienes que ser mayor de edad para seguir")
        # Comprobacion del sexo
        if self.sexo != "H" or self.sexo != "M":
            self.sexo = "H"
        else: 
            self.sexo = self.sexo        
        
        
    def mostrar(self):
        print ("DNI: ", self.dni)
        print ("Edad: ", self.edad)
        print ("Sexo: ", self.sexo)

        
if __name__ == '__main__':
    p = Persona
    Persona()
    p.generador_dni()
    p.comprobaciones()
    p.mostrar()