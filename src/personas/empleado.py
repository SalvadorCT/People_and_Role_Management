from .persona import Persona


class Empleado(Persona):  # subclase
    def __init__(self, id, nombre, apellido, fecha_ingreso, cargo, sueldo=2500):
        super().__init__(id, nombre, apellido)  # llamando constructor superclase
        self._fecha_ingreso = fecha_ingreso
        self._cargo = cargo
        self._sueldo = sueldo

    @property
    def fecha_ingreso(self):
        return self._fecha_ingreso

    @fecha_ingreso.setter
    def fecha_ingreso(self, fecha_ingreso):
        if len(fecha_ingreso) == 4 and fecha_ingreso.isdigit():
            self._fecha_ingreso = fecha_ingreso
        else:
            print('Por favor ingrese un anio valido')

    @fecha_ingreso.deleter
    def fecha_ingreso(self):
        del self._fecha_ingreso

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @cargo.deleter
    def cargo(self):
        del self._cargo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    @sueldo.deleter
    def sueldo(self):
        del self._sueldo

    def calcular_antiguedad(self):
        antiguedad = 2023 - self.fecha_ingreso
        print(f'La antiguedad de {self.nombre} {self.apellido} es de {antiguedad} anios.')

    def adicional_info(self):
        sueldo_anual = self._sueldo * 12
        print(f'💰 Mi sueldo anual estimado es de ${sueldo_anual}')

    def __str__(self):
        return (f'\nHola! soy un Empleado...'
                f'\n🆔 Identificacion es: {self._id}'
                f'\n👤 Nombre: {self._nombre} {self._apellido}'
                f'\n📅 Fecha de ingreso: {self._fecha_ingreso}'
                f'\n💼 Cargo: {self._cargo}'
                f'\n💰 Sueldo Mensual: ${self._sueldo}')