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
        while True:
            try:
                opcion = int(input("Ingresa un número (1, 2 o 3): "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
            continue  # Regresa al inicio del bucle para repetir la pregunta

            if opcion in (1, 2, 3):
                break  # Sale del bucle si la opción es válida
            else:
                print("La opción no es válida. Debe ser 1, 2 o 3.")
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

        try:    
            num_intr = int(input("Inserte un num de 1 al 10: "))
        except ValueError:
            print ("Por favor, ingresa un número válido.")
        else:
            puntos = Partido.ranking(num_intr, num_random)
            print(f"El número generado fue {num_random}. Obtuviste {puntos} puntos.")

    def ranking ():

        diferencia = abs(num_intr - num_random)

        if diferencia == 0:
            puntos = 10  # Máxima puntuación si el número es exacto
        elif diferencia <= 1:
            puntos = 9   # Puntuación intermedia si está cerca (por ejemplo, a 2 números de diferencia)
        elif diferencia <= 2:
            puntos = 8
        elif diferencia <= 3:
            puntos = 7
        elif diferencia <= 4:
            puntos = 6
        elif diferencia <= 5:
            puntos = 5
        elif diferencia <= 6:
            puntos = 4
        elif diferencia <= 7:
            puntos = 3
        elif diferencia <= 8:
            puntos = 2
        elif diferencia <= 9:
            puntos = 1
        else:
            puntos = 0   # Sin puntos si la diferencia es mayor

            return puntos
    



if __name__=='__main__':
    
    Menu.append()
    Menu.mostrar_menu()
    Partido.iniciar_partida()
    Partido.calc_puntos
