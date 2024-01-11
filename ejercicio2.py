import time

class Cancion():
    #constructor
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def elejir():
        eleccion_cancion = input ("Elije una cancion para tocar (c1 o c2): ")
        if eleccion_cancion == "c1": 
            print("...")
            time.sleep(1)
            print("""In many ways, they'll miss the good old days
Someday
Someday
Yeah, it hurts to say, but I want you to stay
Sometimes
Sometimes
When we was young, oh man, did we have fun
Always
Always
Promises, they break before they're made
Sometimes
Sometimes
Oh, Maya says I'm lacking in depth
I will do my best
You say you want to stand by my side
Darling, your head's not right
Ah, see, alone we stand, together we fall apart
Yeah, I think I'll be alright
I'm working so I won't have to try so hard
Tables, they turn sometimes
Oh, someday
No, I ain't wasting no more time
And now my fears they come to me in threes
So I
Sometimes
Say, fate, my friend, you say the strangest things
I find, sometimes
Oh, Maya says I'm lacking in depth
Shit, I will try my best
You say you want to stand by my side
Darling, your head's not right
Ah, see, alone we stand, together we fall apart
Yeah, I think I'll be alright
I'm working so I won't have to try so hard
Tables, they turn sometimes
Oh, someday
I ain't wasting no more time""")
            c1.dame()
        else:
            print("...")
            time.sleep(1)
            print("""Ooh, stop
With your feet on the air and your head on the ground
Try this trick and spin it, yeah (yeah)
Your head will collapse, and there's nothing in it
And you'll ask yourself
Where is my mind?
Where is my mind?
Where is my mind?
Way out in the water, see it swimmin'
I was swimmin' in the Caribbean
Animals were hiding behind the rock
Except the little fish
Bumped into me, I swear he was trying to talk to me, koi-koi
Where is my mind?
Where is my mind?
Where is my mind?
Way out in the water, see it swimmin'
With your feet on the air and your head on the ground
Try this trick and spin it, yeah
Your head will collapse, and there's nothing in it
And you'll ask yourself
Where is my mind?
Where is my mind?
Where is my mind?
Way out in the water, see it swimmin'
With your feet on the air and your head on the ground
Try this trick and spin it, yeah""")
            c2.dame()
            
    def dame(self):
        #eleccion de datos
        eleccion = input ("Elije para saber más ('titulo', 'autor' o 'ambos): ")
        if eleccion == "titulo":
            print ("El titulo de la cancion es: ", self.titulo)
            eleccion = input ("Quieres saber mas datos?('si' o 'no'): ")
            if eleccion == "si": #
                Cancion.dame(self)
            else: 
                SystemExit
        elif eleccion == "autor":
            print ("El autor de la cancion es: ",self.autor)
            eleccion = input ("Quieres saber mas datos?('si' o 'no'): ")
            if eleccion == "si":
                Cancion.dame(self)
            else:
                SystemExit
        else:
            print ("El titulo de la cancion es: ", self.titulo)
            print ("El autor de la cancion es: ",self.autor)
            
        
if __name__ == '__main__':
    c= Cancion
    c1 = Cancion ('Someday', 'The Strokes')
    c2 = Cancion ('Where is my mind', 'Pixies')
    c.elejir()


    
        