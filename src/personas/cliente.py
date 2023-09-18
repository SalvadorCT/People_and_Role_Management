from .persona import Persona


class Cliente(Persona):  # subclase
    def __init__(self, id, nombre, apellido, direccion_fiscal, codigo_postal, estado):
        super().__init__(id, nombre, apellido)  # llamando constructor superclase
        self._direccion_fiscal = direccion_fiscal
        self._codigo_postal = codigo_postal
        self._estado = estado

    @property
    def direccion_fiscal(self):
        return self._direccion_fiscal

    @direccion_fiscal.setter
    def direccion_fiscal(self, direccion_fiscal):
        self._direccion_fiscal = direccion_fiscal

    @direccion_fiscal.deleter
    def direccion_fiscal(self):
        del self._direccion_fiscal

    @property
    def codigo_postal(self):
        return self._codigo_postal

    @codigo_postal.setter
    def codigo_postal(self, codigo_postal):
        self._codigo_postal = codigo_postal

    @codigo_postal.deleter
    def codigo_postal(self):
        del self._codigo_postal

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @estado.deleter
    def estado(self):
        del self._estado

    def adicional_info(self):
        pass

    def __str__(self):
        return (f'\nHola! soy un Cliente...'
                f'\n🆔 Identificacion es: {self._id}'
                f'\n👤 Nombre: {self._nombre} {self._apellido}'
                f'\n🏠 Direccion fiscal: {self._direccion_fiscal}'
                f'\n📮 Codigo Postal: {self._codigo_postal}'
                f'\n🏞️  Estado de Residencia: {self._estado}')