from fractions import Fraction


class Calculadora:
    def __init__(self, memoria, numero, operacion, opant):
        self.memoria = memoria
        self.numero = numero
        self.operacion = operacion
        self.opant = opant
    
    def setNumero(self, num):
        self.numero = num

    def setMemoria(self, mem):
        self.memoria = mem

    def setOpant (self, oa):
        self.opant = oa

    def setOperacion (self, op):
        self.op =op



    def getNumero (self):
        return self.numero

    def getMemoria (self):
        return self.memoria

    def getOp_ant(self):
        return self.opant

    def getOp(self):
        return self.operacion

    def ejecuta(self):
        if self.opant== "+":
            self.memoria= self.memoria + self.numero
        elif self.opant== "-":
            self.memoria= self.memoria - self.numero
        elif self.opant== "*":
            self.memoria= self.memoria * self.numero
        elif self.opant== "/":
            self.memoria= self.memoria / self.numero
        elif self.opant== "**":
            self.memoria= self.memoria ** self.numero
        elif self.opant== "raiz":
            self.memoria= self.memoria ** (0.5)
        elif self.opant== "":
            self.memoria= self.numero
        self.opant=self.operacion

    
print("Para utilizar la raiz cuadrada, escribir la palabra raiz")
print("\n")

calcu = Calculadora(0,0,"","") 
operacion = ""

while (operacion != "="):
    num= int(input())
    operacion = input()
    calcu.setNumero(num)
    calcu.setOperacion(operacion)
    calcu.ejecuta()


print(calcu.getMemoria())





