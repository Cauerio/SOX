import random
import os

class Menu ():

    def append ():
        global nickname_list
        nickname_list = []
        nickname_cantidad = int(input ("Cuantas personas jugarán?: "))
        for i in range (nickname_cantidad):
            nickname = input ("Ingresa el nombre: ")
            nickname_list.append (nickname)
                


    def mostrar_menu ():

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
                print (Partido.iniciar_partida)
            case 2: 
                    print ("Ranking:", ", ".join(nickname_list))
                    volver = input ("Escribe 'exit' para volver: ")
                    if volver.lower() == "exit":
                        Menu.mostrar_menu()
                        os.system('cls' if os.name == 'nt' else 'clear')

            case 3:
                SystemExit

        
        

class Partido ():
    def iniciar_partida():

        global num_random
        global num_intr
        num_random = random.randint (1, 10)
    
        num_intr = int(input("Inserte un num de 1 al 10: "))
        if opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5 and opcion != 6 and opcion != 7 and opcion != 8 and opcion != 9 and opcion != 10:
            print ("Por favor, ingresa un número válido.")
        else:
            puntos = Partido.ranking(num_intr, num_random)
            print(f"El número generado fue {num_random}. Obtuviste {puntos} puntos.")

    def ranking ():

        diferencia = abs(num_intr - num_random)

        if diferencia == 0:
            puntos = 10  # Máxima puntuación si el número es exacto
            print ("Has sumado 10 puntos")
        elif diferencia <= 1:
            puntos = 9   # Puntuación intermedia si está cerca (por ejemplo, a 2 números de diferencia)
            print ("Has sumado 9 puntos")
        elif diferencia <= 2:
            puntos = 8
            print ("Has sumado 8 puntos")
        elif diferencia <= 3:
            puntos = 7
            print ("Has sumado 7 puntos")
        elif diferencia <= 4:
            puntos = 6
            print ("Has sumado 6 puntos")
        elif diferencia <= 5:
            puntos = 5
            print ("Has sumado 5 puntos")
        elif diferencia <= 6:
            puntos = 4
            print ("Has sumado 4 puntos")
        elif diferencia <= 7:
            puntos = 3
            print ("Has sumado 3 puntos")
        elif diferencia <= 8:
            puntos = 2
            print ("Has sumado 2 puntos")
        elif diferencia <= 9:
            puntos = 1
            print ("Has sumado 1 punto")
        else:
            puntos = 0   # Sin puntos si la diferencia es mayor

            return puntos
    


if __name__=='__main__':
    
    Menu.append()
    Menu.mostrar_menu()
    Partido.iniciar_partida()
    Partido.ranking()
