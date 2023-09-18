class Persona():  # superclase
    def __init__(self, id, nombre, apellido):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if id.isdigit():
            self._id = id
        else:
            print('Por favor ingrese un numero valido')

    @id.deleter
    def id(self):
        del self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if len(nombre) > 2:
            self._nombre = nombre
        else:
            print('Por favor ingrese un nombre valido')

    @nombre.deleter
    def nombre(self):
        del self._nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        if len(apellido) > 2:
            self._apellido = apellido
        else:
            print('Por favor ingrese un apellido valido')

    @apellido.deleter
    def apellido(self):
        del self._apellido

    def adicional_info(self):
        pass

    def __str__(self):
        return (f'\nHola! soy una Persona...'
                f'\n🆔 Identificacion: {self._id}'
                f'\n👤 Nombre: {self._nombre} {self._apellido}')
