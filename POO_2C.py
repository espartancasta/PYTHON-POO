from kivy.uix.accordion import ObjectProperty

class personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre 
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa 
        self.vida = vida
        
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
      print("-Fuerza:",self.fuerza)
      print("-Inteligencia:",self.inteligencia)
      print("-defensa",self.defensa)
      print("-vida:",self.vida)
      
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia 
        self.defensa = self.defensa + defensa
    
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre,"ha muerto")
        
    def dañar(self, enemigo): 
        return self.fuerza - enemigo.defensa 
    
    def atacar(self,enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida= enemigo.vida - daño 
        print (self.nombre,"ha realizado",daño, "puntos de daño a", enemigo.nombre)
        print("Vida de",enemigo.nombre,"es",enemigo.vida)
    
mi_personaje = personaje("EsteBanDiDo", 100, 50, 45, 100)
#mi_personaje.morir()
mi_enemigo = personaje("Angel", 70, 100, 40, 100)
mi_personaje.imprimir_atributos()
mi_personaje.atacar(mi_enemigo)
#print(mi_personaje.esta_vivo())
#mi_personaje.subir_nivel(15,5,10)
#print ("valores actulizados")
#mi_personaje.imprimir_atributos()



#modificando valores de los atributos
#mi_personaje.nombre = "EstebanDido"
#mi_personaje.fuerza = 300
#mi_personaje.inteligencia = -2
#mi_personaje.defensa = 30
#mi_personaje.vida = 2

#print("El nombre de mi personaje es: ",mi_personaje.nombre)
#print("El fuerza de mi personaje es: ",mi_personaje.fuerza)
#print("El inteligencia de mi personaje es: ",mi_personaje.inteligencia)
#print("El defensa de mi personaje es: ",mi_personaje.defensa)
#print("El vida de mi personaje es: ",mi_personaje.vida)