import os
import time
from datetime import date 

class Cuenta():
    def __init__(self):
        self.dni = int(input ("Digite su DNI: "))
        self.interes_diario = 0.025
        self.interes_anual = self.interes_diario * 365
        self.saldo_total = int(input ("Ingrese una cantidad inicial de saldo: "))
        
        
    def menu(self):
        print ("1) Visualizar cuenta")
        print ("2) Ingresar ingresos")
        print ("3) Sacar ingresos")
        seleccion = int(input ("Que operación deseas hacer?(Seleccione un numero): "))
        match(seleccion):
            case 1:
                print ("DNI: ",self.dni)
                print ("Tu saldo total es: ",self.saldo_total, "€")
                print ("Interés anual ",self.interes_anual) 
            case 2: 
                Cuenta.ingresar(self)
            case 3:
                Cuenta.sacar(self)
                
    
    def ingresar(self):
        self.ingreso = int(input ("Cuanto quieres ingresar?: "))
        print ("Actualizando...")
        time.sleep(3)
        self.saldo_total = self.saldo_total + self.ingreso
        print ("Cantidad total de saldo: ",self.saldo_total)
        
        
    def sacar(self):
        self.saque = int(input ("Cuanto quieres sacar?: "))
        print ("Actualizando...")
        time.sleep(3)
        self.saldo_total = self.saldo_total - self.saque
        print ("Cantidad total de saldo: ", self.saldo_total)

    def actualizar_saldo(self):
        today = date.today()
        self.saldo_total_dia = (self.saldo_total*self.interes_diario)
        self.saldo_total = (self.saldo_total - self.saldo_total_dia)    
        
        
        
        
        
if __name__=='__main__':
    c= Cuenta()
    c.menu()
    c.actualizar_saldo()
    
    
    
    
