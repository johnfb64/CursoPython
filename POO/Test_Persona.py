#Se procede a llamar la clase Persona_Encapsulada del archivo Persona_Encapsulada.py
from Persona_Encapsulada import Persona_Encapsulada

#Metodo center centra la linea indicada y se le puede dejar como adorno "-"
print ('Creacion de objetos'.center(50,'-'))
#Crea objeto de Persona_Encapsulada
persona2 = Persona_Encapsulada('Pepe', 'De la Suerte', 50)
#Manda a llamar metodo mostrar_detalle
persona2.mostrar_detalle()

print ('Eliminación de objetos'.center(30,'-'))
#Destructor de objetos - recolector de basura  - Elimina objetos de la memoria

del persona2

