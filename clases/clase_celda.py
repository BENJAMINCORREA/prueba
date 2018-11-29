from tkinter import Button
class celda(Button()):

    estado = False
    minas = False
    bandera = False
    #minas_cerca = 0

    def __init__(self):
        self

    def cambiar_estado(self):
        self.estado = True
        self.set_bandera()

    def es_mina(self):
        self.minas = True

    def set_bandera(self):
        if (self.bandera):
            self.bandera = False
        else:
            self.bandera = True

prueba = celda()
prueba.com
prueba.pack(side=BOTTOM)
prueba.mainloop()