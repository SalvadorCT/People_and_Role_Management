from .persona import Persona


class Estudiante(Persona):  # subclase
    def __init__(self, id, nombre, apellido, semestre_matricula):
        super().__init__(id, nombre, apellido)  # llamando constructor superclase
        self._semestre_matricula = semestre_matricula

    @property
    def semestre_matricula(self):
        return self._semestre_matricula

    @semestre_matricula.setter
    def semestre_matricula(self, semestre_matricula):
        if semestre_matricula.isdigit() and 0 < semestre_matricula < 11:
            self._semestre_matricula = semestre_matricula
        else:
            print('Por favor ingrese un numero valido')

    @semestre_matricula.deleter
    def semestre_matricula(self):
        del self._semestre_matricula

    def avanzar_semestre(self):
        if self.semestre_matricula < 10:
            self.semestre_matricula = self.semestre_matricula + 1
        else:
            print('Felicidades! Acabaste la carrera 🥳')

    def adicional_info(self):
        semestres_restantes = 10 - self._semestre_matricula
        print(f'🎓 Los semestres restantes para graduarme son {semestres_restantes}')

    def __str__(self):
        return (f'\nHola! soy un Estudiante...'
                f'\n🆔 Identificacion: {self._id}'
                f'\n👤 Nombre: {self._nombre} {self._apellido}'
                f'\n📚 Semestre de Matricula: {self._semestre_matricula}')