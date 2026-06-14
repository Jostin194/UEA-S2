#Programacion tradicional 

def Mascota():
    nombre = input("Ingresa nombre de la mascota")
    especie = input("Ingresa especie de la mascota")
    edad = input("Ingresa edad de la mascota")

    return nombre, especie, edad 

def mostra_mascotas(nombre, especie, edad):
    print(f"El nombre es: {nombre} y la especie es: {especie}")
    print(f"La edad es: {edad}")


nombre, especie, edad = Mascota()

mostra_mascotas(nombre, especie, edad)
