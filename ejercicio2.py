class Cancion():

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def elejir():
        eleccion_cancion = input ("Elije una cancion (c1 o c2): ")
        if eleccion_cancion == "c1": 
            c1.dame()
            c1.dame()
        else:
            c2.dame()
            c2.dame()
            
    def dame(self):
        eleccion = input ("Elije lo que quieres mostrar ('titulo', 'autor' o 'ambos')?: ")
        if eleccion == "titulo":
            print ("El titulo de la cancion es: ", self.titulo)
        elif eleccion == "autor":
            print ("El autor de la cancion es: ",self.autor)
        else:
            print ("El titulo de la cancion es: ", self.titulo)
            print ("El autor de la cancion es: ",self.autor)
            
        
if __name__ == '__main__':
    c= Cancion
    c1 = Cancion ('Someday', 'The Strokes')
    c2 = Cancion ('Where is my mind', 'Pixies')
    c.elejir()

    
        