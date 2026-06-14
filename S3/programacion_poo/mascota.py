#Programacion Poo
from typing import Self


class Mascota :
     def __init__(self, nombre, especie, edad):
          self.nombre = nombre
          self.especie = especie
          self.edad = edad


     def mostrar_informacion(sefl):
          print(f"El nombre es: {sefl.nombre}")
          print(f"La especie es: {sefl.especie}")
          print(f"La edad es: {sefl.edad}")

     def hacer_sonido(self):
        especie_mascota = self.especie.lower()
        if especie_mascota == "perro":
            print(f"{self.nombre} sonido: Guau,guau")
        else:
            print(f"{self.nombre} hace un sonido extraño.")
          



