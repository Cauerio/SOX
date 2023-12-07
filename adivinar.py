import random
import os
import time 

class Menu ():

    def append (self):
        #global nickname_list
        #global nickname_cantidad
        global nickname
        #nickname_list = []
        #nickname_cantidad = int(input ("Cuantas personas jugarán?: "))
        #for i in range (nickname_cantidad):
        nickname = input ("Ingresa el nombre: ")
        #nickname_list.append (nickname)
                


    def mostrar_menu (self):

        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla

        print ("1) Iniciar partido")
        print("2) Ver ranking")
        print ("3) Salir")

        global opcion
        opcion = int(input("Elige una opción: "))

        while opcion != 1 and opcion != 2 and opcion != 3:
            print ("Introduce un número de 1 al 3")
            Menu.mostrar_menu()
            os.system('cls' if os.name == 'nt' else 'clear')
        match (opcion):
            case 1:
                print (Partido.iniciar_partida(self)) 
            case 2: 
                    print (Tratamiento_fichero.read_file(self, archivo = "jugadores.txt"))
                    volver = input ("Escribe 'exit' para volver: ")
                    if volver.lower() == "exit":
                        Menu.mostrar_menu()
                        os.system('cls' if os.name == 'nt' else 'clear')

            case 3:
                SystemExit


    def mostrar_menu2 ():

        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla

        print ("1) Seleccionar jugadores")
        print("2) Ver ranking")
        print ("3) Salir")

        global opcion
        opcion = int(input("Elige una opción: "))

        while opcion != 1 and opcion != 2 and opcion != 3:
            print ("Introduce un número de 1 al 3")
            Menu.mostrar_menu()
            os.system('cls' if os.name == 'nt' else 'clear')
        match (opcion):
            case 1:
                print (Partido.iniciar_partida)
            case 2: 
                    print (fjugadores)
                    volver = input ("Escribe 'exit' para volver: ")
                    if volver.lower() == "exit":
                        Menu.mostrar_menu()
                        os.system('cls' if os.name == 'nt' else 'clear')

            case 3:
                SystemExit        
        

class Tratamiento_fichero():

    def __init__(self):
        self.archivo =  "jugadores.txt"
    
    def write_file(self):
        fw = open (self.archivo, "w")
        fw.write (nickname, " tiene ", Partido.iniciar_partida.puntos, " puntos.")
        fw.write ("\n")
        fw.close()

    def read_file(self, archivo):
        global fjugadores
        fr = open (self.archivo, "r")
        fjugadores = print (fr.read())
        fr.close()

class Partido ():
    def __init__(self):
        self.puntuacion = {}
        
    def add_puntuacion(self, nickname, puntuacion):
        self.puntuacion[nickname] = puntuacion

    def actualizar_punt(self, nickname, new_puntuacion):
        if nickname in self.puntuacion and new_puntuacion > self.puntuacion[nickname]:
            self.puntuacion[nickname] = new_puntuacion
            print(f"¡Nuevo récord para {nickname} con un puntaje de {new_puntuacion}!")

    def ranking(self):
        sorted_ranking = sorted(self.puntuacion.items(), key=lambda x: x[1], reverse=True)
        return {name: rank + 1 for rank, (name, puntuacion) in enumerate(sorted_ranking)}
        
    def iniciar_partida(self):
        ganar_partida = False
        puntos = 10
        num_random = random.randint (1, 10)
        
        while not ganar_partida:
            print ("introduce un valor de 1 al 10: ")
            num_intr = int(input())
            if num_intr == num_random:
                ganar_partida = True
            else:
                puntos = puntos -1
                
                
        print(f"El número generado fue {num_random}.")  

        print(f"{nickname} tienes {puntos} puntos.")
        
        return puntos

        #for i in range(len(nickname_list)):
            #num_intr = int(input(f"{nickname_list[i]}, inserte un num de 1 al 10: "))
            #if opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5 and opcion != 6 and opcion != 7 and opcion != 8 and opcion != 9 and opcion != 10:
                #print ("Por favor, ingresa un valor válido.")
            #else: 
                    #print ("Ahora el siguiente...")            
                
        #puntos = Partido.ranking()

        
    
    def volver_menu(self):
        respuesta = input("Escribe 'volver' para volver al menú: ")
        if respuesta.lower() == "volver":
            print ("Estás volviendo al menú...")
            time.sleep(3)
        

if __name__=='__main__':
    
    #Menu.mostrar_menu2()


    m = Menu ()
    p = Partido ()
    t = Tratamiento_fichero ()
    m.append()
    m.mostrar_menu()
    p.iniciar_partida()
    p.volver_menu()
    t.write_file()
    t.read_file("jugadores.txt")
    
    


    #p.ranking()
    #Menu.mostrar_menu()