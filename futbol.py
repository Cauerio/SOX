import random

class Equipo():
    def __init__(self, jugadores, club):
        self.jugadores = jugadores
        self.club = club
    

    def ocas_gol(self):
        ocas_gol = random.randint(0,1)
        if ocas_gol == 1:
            print("Hay ocasion de gol para el ", self.club)
            return 1
        else:
            return 0
            
        



class Partido ():

    def __init__(self, E1, E2, ocasiones):
        self.E1 = E1
        self.E2 = E2
        self.n_ocasiones = ocasiones
        self.golese1 = 0
        self.golese2 = 0
        
        
# 0 = no gol
# 1 = gol

    def jugar_partido(self):

        #variables
        #prob = 0.5 #probabilidad de gol
        #variables


        for i in range (self.n_ocasiones, self.golese1):
            ocas_gol = random.randint(0,1)
            if ocas_gol == 1:
                self.golese1 += self.E1.ocas_gol()
                print ("GOOOOOL")
                print ("El juego está: ", self.golese1)
            else:
                self.golese2 += self.E2.ocas_gol()
                print ("Ufff. Falló el gol...")

            

if __name__ == "__main__":
    eq1 = Equipo(["Macia", "juanjo"], "barcelona")
    eq2 = Equipo(["Mario", "Pepe"], "Madrid")
    part = Partido (eq1, eq2, 10)
    part.jugar_partido()
