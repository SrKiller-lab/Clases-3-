class Coche:
    def __init__ (self, gasolina):
        self.gasolina = gasolina

    def arrancar(self):
        if self.gasolina >0:
            print("arrancar")
        else:
            print("no arrancar")
        
    def avanzar(self):
        if self.gasolina >= 5:
            self.gasolina -= 5
            print(f"El coche a avanzado, gasolina perdida {self.gasolina}")
        else:
            print("No hay gasolina")

BMW=Coche(1500)
BMW.arrancar()

while BMW.gasolina >= 5:
    BMW.avanzar()

BMW.avanzar()