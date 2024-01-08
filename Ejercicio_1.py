import os

class Cuenta():
    def __init__(self):
        self.dni = int(input ("Digite su DNI: "))
        self.interes_diario = 0,25 
        self.saldo = int(input ("Ingrese una cantidad inicial de saldo: "))
        self.saldo_total = self.saldo
        
    def menu(self):
        print ("1) Visualizar saldo")
        print ("2) Ingresar ingresos")
        print ("3) Sacar ingresos")
        seleccion = input ("Que operación deseas hacer?(Seleccione un numero):")
        os.system('cls' if os.name == 'nt' else 'clear')
        while seleccion != 1 or seleccion != 2 or seleccion != 3:
            if seleccion == 1: 
                print (self.saldo_total)
            elif seleccion == 2: 
                self.ingreso = int(input ("Cuanto quieres ingresar?: "))
            else:
                self.saque = int(input ("Cuanto quieres sacar?: "))
                
    
    def actualizar_saldo(self):
        print ("Actualizando...")
        if c.menu.seleccion == 2:
            self.saldo_total = self.saldo + self.ingreso
            print ("Cantidad total de saldo: ",self.saldo_total)
        elif c.menu.seleccion == 3:
            self.saldo_total = self.saldo + self.saque
            print ("Cantidad total de saldo: ", self.saldo_total)


        
            
        
        
if __name__=='__main__':
    c= Cuenta()
    c.menu()
    
