
def metodo1():
    print ('Hello world')

def print_array (array):
    print (array)
    for i in array:
        print ("Hola me llamo ", array)


def metodo2 ():
    n1 = float (input('Escriba el primer numero: ')) 
    n2 = float (input('Escriba el segungo numero: '))
    opsuma = "+"
    opdiv = "/"
    opmult = "*"
    opres = "-"
    operador = str(input("Pon un operador (+, *, /, -): "))
    suma = (n1 + n2)
    division = (n1 // n2)
    multiplicar = (n1 * n2)
    resta = (n1 - n2)
    if (operador == "+"):
        print (suma)

    elif (operador == "-"):
        print (resta)

    elif (operador == "*"):
        print (multiplicar)
        
    elif operador == "/":    
        print (division) 

if __name__ == "__main__":
    metodo1()
    metodo2()
    array = ["Jorge", "Salvador", "Pablo"]
    print_array(array)
    





