
class Pila():
    def __initi__(self):
        self.array = []

    def push(self, valor_to_input):
        self.array.append(valor_to_input)


    def view_pila(self):
        print("Mi pila es: ", self.array)
        print ("Mi pila es de clase ", type(self.array))


    def pop (self):
        self.array.pop()


if __name__ == "__main__":
    
    pila = Pila()

    for _ in range(10):
        pila.push("Cauê")

    pila.pop()

    pila.view_pila()

    '''
    pila = []
    pila1 = []

    #Empilar
    for i in range(10):
        pila.append(i)

    for _ in range (10):
        pila1.append("Cauê")

    print("mi pila: ", pila)
    print("mi pila1: ", pila1)

    #Desempilo

    for i in range(10):
        pila.pop()
        print("Desempilo mi pila:", pila)

    pila1.pop()
    pila1.pop()
    print("Desempilo mi pila1:", pila1)

    '''