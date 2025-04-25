class Empleado:
    '''
    Crear objetos de la clase Empleado
    '''
    def __init__(self,nombre,sueldo):
    '''
        Constructor de la clase Empleado
        :param nombre: nombre del empleado
        :param sueldo:sueldo del empleado
        :param eliminado: True si esta eliminado, False si no esta eliminado
    '''
        self.nombre = nombre
        self.sueldo = sueldo
        self.eliminado = False

    @properly
         def nombre(self):
             return self._nombre

    @nombre.setter
     def nombre(self,nombre):
             self._nombre = nombre
             #dsgdfgdfg
