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
        respuesta = input("Escribe 'volver' para volver al menú: ")
        if respuesta.lower() == "volver":
            print ("Estás volviendo al menú...")
            time.sleep(3)
        
    def top (self):  
        lineas_con_numeros = []    
        
        with open("jugadores.txt", "r") as file:
            lineas = file.readlines()
        
            for lineas in lineas:
                last_two_caracters = lineas [-2:]
                
                try:
                    numero = int(last_two_caracters)
                    lineas_con_numeros.append(numero)
                except ValueError:
                    pass
                
            if lineas_con_numeros:
                lineas_con_numeros.sort(reverse=True)

             # Crear una lista de tuplas (nombre, puntaje) para cada línea del archivo
                resultados = [(nickname, puntaje) for puntaje in lineas_con_numeros]

                print("Top 10:")
                for i, (nombre, puntaje) in enumerate(resultados[:10], start=1):
                    puntaje_str = str(puntaje).zfill(2)
                    print(f"{nombre} obtuvo el lugar {i}: {puntaje_str}")
                else:
                    print("No se encontraron números en el archivo.")


            

if __name__=='__main__':
    
    m = Menu () 
    p = Partido ()
    t = Tratamiento_fichero ("jugadores.txt")
    m.append()
    m.mostrar_menu()
    p.iniciar_partida()
    t.write_file(f"\n El jugador {nickname} hizó: {puntos}")
    t.read_file()
    p.volver_menu()
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla
    p.top()
    
    
    


 