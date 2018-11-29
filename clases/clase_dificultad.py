class dificultad():

    numeroMinas = 0
    nivelDificultad = ["facil", "normal",  "dificil"]
    dificultadActual = ""

    def get_nMinas(self):
        return self.numeroMinas
    def get_nivelDificultad(self):
        return  self.dificultadActual
    def set_nivelDificultad(self,cambioDificultad):
        self.dificultadActual = self.nivelDificultad[cambioDificultad-1]

dificultadPrueba = dificultad ()
dificultadPrueba.set_nivelDificultad(1)
print(dificultadPrueba.get_nivelDificultad())
