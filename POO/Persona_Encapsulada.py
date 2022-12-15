class Persona_Encapsulada():
    #__init__ es un inicializador. Se depende de este metodo para crear objetos.
    def __init__(self,nombre,apellido,edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    #GETTER
    #@property es un decorador que no va dejar acceder a _nombre, solo se podra hacer por el getter
    @property
    def nombre(self):
        #Permite recuperar sin especificar los parentesis de atributo.
        return self._nombre

    #SETTER
    #@nombre.setter es el setter, solo se debera cambiar atributo a travez de este metodo y no directamente.
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self,edad):
        self._edad = edad


    def mostrar_detalle(self):
            print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

    #Metodo para eliminar objetos __del__, esto eliminara atributos nombre y apellido. Esto libera recursos.
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

#
#
# persona1 = Persona_Encapsulada('Pepe','Suertudo',30)
# #recupera por getter y no por atributo _nombre.
# print(f'Objeto 1. {persona1.nombre},{persona1.apellido},{persona1.edad}')
# print(persona1.nombre)
#
# #utilizando el setter para modificar atributo
# persona1.nombre = 'Juan'
# persona1.apellido = 'Pringamoso'
# persona1.edad = 50
#
# print(f'Objeto 1 modificado: {persona1.nombre},{persona1.apellido},{persona1.edad}')



