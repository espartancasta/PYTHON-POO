class personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida


    def imprimir_atributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defesa = self.defesa + defensa
    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f"{self.nombre} ha muerto")

    def dañar(self, enemigo):
        return max(0, self.fuerza - enemigo.defensa)

    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = max(0, enemigo.vida - daño)
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("Vida de", enemigo.nombre, "es", enemigo.vida)

class Guerrero(personaje):

   #Sobreescribir el constructor 
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        self.fuerza = self.fuerza + 100
        self.inteligencia = self.inteligencia + 500
        self.defensa = self.defensa + 50

        #Sobrescribrir impresión de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("Espada:",self.espada)
    #Sobreescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.fuerza*self.espada 
#Escoger navaja
    def escoger_navaja(self):
        opcion =int(input("Escoge la navaja de la muerte:\n(1) Navaja suiza, daño 10.\n(2) Navaja pioja, daño 6.\n>>>>>"))
        if(opcion == 1):
            self.espada = 10
        elif(opcion == 2):
            self.espada = 6
        else:
            print("Opción no válida, intente nuevamente")
            #Vuelva a ejecutar el método escoger la navaja
            self.escoger_navaja()


class Mago(personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, hechizo):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.hechizo = hechizo
        self.inteligencia = self.inteligencia + 200
        self.defensa = self.defensa + 20
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("hechizo:",self.hechizo)
    #Sobreescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.inteligencia*self.hechizo 
#Escoger navaja
    def escoger_hechizo(self):
        opcion =int(input("Escoge el hechizo de la muerte:\n(1) Hechizo Hocus Poccus, daño 100.\n(2) Hechizo Kabum, daño 6.\n>>>>>"))
        if(opcion == 1):
            self.hechizo = 100
        elif(opcion == 2):
            self.hechizo = 6
        else:
            print("Opción no válida, intente nuevamente")
            #Vuelva a ejecutar el método escoger la navaja
            self.escoger_hechizo()


        #Sobreescribir el cálculo del daño

#Crear todos objetos
persona = personaje("Ángel, Suárez", 20, 15, 10, 100)
arturoSuarez = Guerrero("Arturo Suárez", 20, 15, 10, 100, 5)
gandalf = Mago("Gandalf", 20, 16, 10, 100, 5)
#Atributos antes de la tragedia
persona.imprimir_atributos()
arturoSuarez.imprimir_atributos()
gandalf.imprimir_atributos()
#Ataques sin piedad
persona.atacar(arturoSuarez)
arturoSuarez.atacar(gandalf)
gandalf.atacar(persona)
#Atributos después de la tragedia
persona.imprimir_atributos()
arturoSuarez.imprimir_atributos()
gandalf.imprimir_atributos()
#Variable del cosntructor vacío 
#mi_personaje = personaje("EsteBandido", 100, 50, 45, 100)
#mi_enemigo = personaje("Ángel", 70, 100, 40, 100)
#mi_personaje.imprimir_atributos() 
#arturoSuarez = Guerrero("Arturo Suarez", 12, 3000, 2,100,.5)
#arturoSuarez.escoger_navaja()
#Mago.escoger_hechizo()
#arturoSuarez.imprimir_atributos()
#mi_personaje.atacar(mi_enemigo)
#print(mi_personaje.esta_vivo())