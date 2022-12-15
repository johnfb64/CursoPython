class Persona():
    #__init__ es un inicializador. Se depende de este metodo para crear objetos.
    def __init__(self,nombre,apellido,edad):
        #_nombre, _apellido y _edad, el "_" solo sirve para indicar que no se deberia modificar el atributo
        #desde los objetos, aun que puede hacerse. Esto es una convencionalidad. 
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    #Creacion de un metodo
    #El parametro self se agrega a todos los metodos de instancia. Esto es por que los metodos se van a asociar con
    #los objetos que se van a crear.
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')



#Creacion de primer objeto
Persona1 = Persona('John','Ballen',40)
print(Persona1._nombre)
print(Persona1._apellido)
print(Persona1._edad)

#Creacion de segundo objeto
Persona2 = Persona('Jenny','Perez',36)
print(f'Segundo objeto es: {Persona2._nombre}, {Persona2._apellido}, {Persona2._edad}')

#Cambio de valor de atributos de un objeto:
Persona2._nombre = 'Pepa'
Persona2._apellido = 'De la suerte'
Persona2._edad = 10

print(f'Segundo objeto es: {Persona2._nombre}, {Persona2._apellido}, {Persona2._edad}')

#Creacion de objeto con metodo
Persona3 = Persona('Esperanza','Gomez',41)
Persona3.mostrar_detalle()

#Agregar atributo
#Al agregar atributo solamente a un objeto, este nuevo atributo sera unicamente de este objeto, no de los demas.
Persona4 = Persona('Pepe','De la suerte',50)
Persona4.telefono = '3215689745'
Persona4.mostrar_detalle()
print(Persona4.telefono)