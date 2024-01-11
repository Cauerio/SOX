#libreria
import os
import time
from datetime import date 


class Cuenta():
    #constructor
    def __init__(self, saldo_total):
        self.dni = int(input ("Digite su DNI(solo numeros): "))
        self.interes_diario = 0.025
        self.interes_anual = self.interes_diario * 365
        self.saldo_total = saldo_total
        
    
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
                
    #funcion ingresar
    def ingresar(self):
        self.ingreso = int(input ("Cuanto quieres ingresar?: "))
        print ("Actualizando...")
        time.sleep(3)
        self.saldo_total = self.saldo_total + self.ingreso
        print ("Cantidad total de saldo: ",self.saldo_total)
        
    #funcion sacar
    def sacar(self):
        self.saque = int(input ("Cuanto quieres sacar?: "))
        if self.saque <= self.saldo_total:   #si la cantidad de saque es mayor que el saldo total
            print ("Actualizando...")
            time.sleep(3)
            self.saldo_total = self.saldo_total - self.saque
            print ("Cantidad total de saldo: ", self.saldo_total)
        else:
            print("Fondos insuficientes")

    def actualizar_saldo(self):
        today = date.today()
        dias_pasados = (today - self.ultima_actualizacion).days if hasattr(self, 'ultima_actualizacion') else 0
        #hasattr verifica si el objeto tiene un atributo.
        #interes_calc= self.interes_diario * self.saldo_total
        #interes = self.saldo_total - interes_calc
        interes_acumulado = self.interes_diario * self.saldo_total * dias_pasados #calcula el interés de los dias que no has estado
        self.saldo_total = interes_acumulado
        self.ultima_actualizacion = today    
        #print("Total saldo post interés diario:",interes)
        
if __name__=='__main__':
    c= Cuenta(10500)
    c.menu()
    c.actualizar_saldo()
    
    
    
    
