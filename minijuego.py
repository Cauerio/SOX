import random
import os
import time 


class Menu ():

    def append (self):
        global nickname
        nickname = input ("Ingresa el nombre: ")
        self.nombres_antiguos = set()
        
    
                
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
                    t.read_file()
                    volver = input ("Escribe 'exit' para volver: ")
                    if volver.lower() == "exit":
                        Menu.mostrar_menu(self)
                        os.system('cls' if os.name == 'nt' else 'clear')

            case 3:
                SystemExit   
        



class Tratamiento_fichero():

    def __init__(self, archivo):
        self.archivo = archivo
    
    def write_file(self, line_to_write):
        f = open(self.archivo, "a")
        f.write(line_to_write)
        f.write("\n")
        f.close()
        
    def read_file(self):
        f = open(self.archivo, "r")
        print(f.read())
        f.close()




class Partido ():      
    def iniciar_partida(self):
        ganar_partida = False
        global puntos
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
    
    def volver_menu(self):
        respuesta = input("Escribe 'salir' para salir del juego: ")
        if respuesta.lower() == "salir":
            print ("Estás saliendo del juego...")
            time.sleep(3)


if __name__=='__main__':
    
    m = Menu () 
    p = Partido ()
    t = Tratamiento_fichero ("jugadores.txt")
    m.append()
    m.mostrar_menu()
    t.write_file(f"\n El jugador {nickname} hizó: {puntos} puntos")
    t.read_file()
    p.volver_menu()
    
    
    
    


 