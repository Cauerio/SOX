import time

class Car():
    def __init__(self, motor, ruedas, puertas, velocidad):
        self.motor = motor
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.velocidadactual = 0
        self.velocidadpunta = 200

    def velocidad(self, velocidadactual):
        self.velocidadactual = 0 

    def arrancar(self):
        print("voy a arrancar")
        time.sleep(4)

    def acelerar(self):
        print("acelerando...")
        while self.velocidadactual < self.velocidadpunta:
            time.sleep(0.05)
            self.velocidadactual = self.velocidadactual+ 5
            print(self.velocidadactual, "km/h")

            if (self.velocidadactual == 50):
                print("cambiar marcha")
            elif(self.velocidadactual == 100):
                print("cambiar la marcha otra vez")
            elif (self.velocidadactual == 150):
                print("cambiar la marcha otra vez")
            elif(self.velocidadactual == 200):
                print("cambiar la marcha otra vez")

    def frenar(self):
        print("frenando...")
        while self.velocidadactual > 0:
            time.sleep(0.05)
            self.velocidadactual = self.velocidadactual - 2
            print(self.velocidadactual)

            if (self.velocidadactual == 50):
                print("cambiar marcha")
            elif(self.velocidadactual == 100):
                print("cambiar la marcha otra vez")
            elif (self.velocidadactual == 150):
                print("cambiar la marcha otra vez")
            elif(self.velocidadactual == 200):
                print("cambiar la marcha otra vez")

if __name__ == "__main__":
    c1= Car("V8", "micheil", "5", "180")

    c1.arrancar() 
    c1.acelerar()
    c1.frenar()