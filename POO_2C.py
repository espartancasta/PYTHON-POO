from kivy.uix.accordion import ObjectProperty

class personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre 
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa 
        self.__vida = vida
        
#PREGUNTA DE EXAMEEEEEEEENNNNNN::::::: QUE ES SELF??? SELF ES UNA REFERENCIA AL MISMO OBJETO 
#### PREGUNTA DE EXAMEN, QUE ES EL MEOTOD INIT ?????? CONTRUCTOR QUE INICIALIZA LOS ATRIBUTOS DE UN ObjeTO
## por que se usa doble guin bajo ???? Dunder. Porque es un metodo magico 
#### COMO SE EJECUTA EL METODO INIT?  SE ejecuta automaticamente cuando se crea una instancia de una clase.

#atributos de la clase
   # nombre = 'Default'
   # fuerza = 0 
   # inteligencia = 0
   # defensa = 0 
   # vida = 0
#variable del constructor vacio 
    def imprimir_atributos(self):
      print(self.nombre)
      print("-Fuerza:",self.__fuerza)
      print("-Inteligencia:",self.__inteligencia)
      print("-defensa",self.__defensa)
      print("-vida:",self.__vida)
      
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia 
        self.__defensa = self.__defensa + defensa
    
    
    def esta_vivo(self):
        return self.__vida > 0
    
    def morir(self):
        self.__vida = 0
        print(self.nombre,"ha muerto")
        
    def dañar(self, enemigo): 
        return self.__fuerza - enemigo.__defensa 
    
    def atacar(self,enemigo):
        daño = self.dañar(enemigo)
        if daño < 0:
            daño = 0
        if enemigo.__vida - daño < 0: 
            enemigo.__vida = 0
        else: 
            enemigo.__vida= enemigo.__vida - daño 
        print (self.nombre,"ha realizado",daño, "puntos de daño a", enemigo.nombre)
        print("Vida de",enemigo.nombre,"es",enemigo.__vida)
    
    def get_vida(self):
        return self.__vida 
    
    def set_vida(self, vida):
        self.__vida = vida 
        if self.__vida <= 0:
            self.morir()
        
        
        
mi_personaje = personaje("EsteBanDiDo", 100, 50, 45, 100) 
#mi_personaje.morir()
mi_enemigo = personaje("Angel", 70, 100, 40, 100)
print(mi_personaje.get_vida())
mi_personaje.set_vida(-5)
mi_personaje._personaje_vida = -50
print(mi_personaje.get_vida())
#mi_personaje.vida = 0
#mi_personaje.imprimir_atributos()
#mi_personaje.atacar(mi_enemigo)
#print(mi_personaje.esta_vivo())
#mi_personaje.subir_nivel(15,5,10)
#print ("valores actulizados")
#mi_personaje.imprimir_atributos()



#modificando valores de los atributos
#mi_personaje.nombre = "EstebanDido"
#mi_personaje.__fuerza = 300
#mi_personaje.__inteligencia = -2
#mi_personaje.__defensa = 30
#mi_personaje.__vida = 2

#print("El nombre de mi personaje es: ",mi_personaje.nombre)
#print("El fuerza de mi personaje es: ",mi_personaje.__fuerza)
#print("El inteligencia de mi personaje es: ",mi_personaje.__inteligencia)
#print("El defensa de mi personaje es: ",mi_personaje.__defensa)
#print("El vida de mi personaje es: ",mi_personaje.__vida)