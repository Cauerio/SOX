import random

class Persona():
    def __init__(self):
        self.edad = Persona.comprobar_edad(self)
        self.sexo = input("Cual es tu genero?('H' o 'M'): ")
        self.dni = Persona.generador_dni(self)
        
    def generador_dni(self):
        numeros = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        letra = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.dni = numeros + letra

    def comprobar_edad(self):
        while True:
            edad = int(input("Cuántos años tienes?: "))
            if edad >= 18:
                return True
            else:
                print("Tienes que ser mayor de edad para seguir")
                continuar = input("Quieres volver a ingresar tu edad? (si o no): ")
                if continuar != "si":
                    return False


    def comprobacion_sexo(self):

        # Comprobacion del sexo
        if self.sexo == "M":
            self.sexo = "M"
        elif self.sexo == "H":
            self.sexo = "H"
        else: 
            self.sexo = "H"        
        
        
    def mostrar(self):
        print ("DNI: ", self.dni)
        print ("Edad: ", self.edad)
        print ("Sexo: ", self.sexo)

        
if __name__ == '__main__':
    p = Persona ()
    p.comprobacion_sexo()
    p.generador_dni()
    p.mostrar()
