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
                    volver = input ("Escribe 'exit' para volver: ")
                    if volver.lower() == "exit":
                        Menu.mostrar_menu()
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
    t = Tratamiento_fichero ("jugadores.txt")
    m.append()
    m.mostrar_menu()
    p.iniciar_partida()
    
    p.volver_menu()
    t.write_file("Estas en el top 1 ")
    t.read_file()
    
    


    #p.ranking()
    #Menu.mostrar_menu()