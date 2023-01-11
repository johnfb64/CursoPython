class FiguraGeometrica:
    def __init__(self, ancho, alto):
        #definicion atributos
        self._ancho = ancho
        self._alto = alto

    #Getter
    @property
    def ancho(self):
        return self._ancho

    #Setter
    @ancho.setter
    def ancho(self,ancho):
        self._ancho = ancho

    #Getter
    @property
    def alto(self):
        return self._alto

    #Setter
    @alto.setter
    def alto(self, alto):
        self._alto = alto


