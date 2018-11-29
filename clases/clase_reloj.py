from datetime import  datetime
class reloj ():

    segundos=0
    correr = False

    def __init__(self):
        self

    def iniciar(self):
        #al inicio de la partida
        self.instanteInicial = datetime.now()

    def parar(self):
        #al final de la partida
        self.instanteActual = datetime.now()

    def get_tiempo (self):
        return self.segundos

    def reiniciar(self):
        self.instanteFinal = datetime.now()
        tiempo = self.instanteFinal - self.instanteInicial # Devuelve un objeto timedelta
        self.segundos = tiempo.seconds

relojprueba=reloj()
respuesta=input("Ingrese lo que quiera")
if respuesta == "inicio":
    relojprueba.iniciar()
respuesta = input("cuando quiera parar diga")
if respuesta == "parar":
    relojprueba.reiniciar()
print(relojprueba.get_tiempo())
