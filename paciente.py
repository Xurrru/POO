### Creacion de una clase (paciente)

class Paciente:

    PREVISIONES:set[str] = {"Fonasa", "Isapre", "Particular", "Otro"}

    def __init__(self, rut:str, nombre:str, edad:int, prevision:str):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        self.prevision = prevision

    @property
    def rut(self)->str:
        return self._rut
    @rut.setter
    def rut(self, rut:str)->None:
        if not isinstance(rut, str) or not rut.strip():
            raise ValueError("El RUT no debe estar vacio.")
        self._rut = rut.strip().upper()

    @property
    def nombre(self)->str:
            return self._nombre
    @nombre.setter
    def nombre(self, nombre:str)->None:
        if not isinstance(nombre, str) or len (nombre.strip()) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        self._nombre = nombre.upper().strip()
    
    @property
    def edad(self)->int:
        return self._edad
    @edad.setter
    def edad(self, edad:int)->None:
        if not isinstance(edad, int): 
            raise ValueError("La edad debe ser un número entero positivo.")
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120 años.")
        self._edad = edad 

    @property
    def prevision(self)->str:
            return self._prevision
    @prevision.setter
    def prevision(self, prevision:str)->None:
        if not isinstance(prevision, str):
             raise TypeError("La previsión debe ser una cadena de texto.")
        prevision_limpia = prevision.strip().capitalize()
        if prevision_limpia not in self.PREVISIONES:
             opciones = ', '.join(self.PREVISIONES)
             raise ValueError(f"Previsión inválida. Las opciones válidas son: {opciones}.")
        self._prevision = prevision_limpia



    def __str__(self) -> str:
        return f"Información del paciente:\nRUT: {self.rut}\nNombre: {self.nombre}\nEdad: {self.edad}\nPrevisión: {self.prevision}"

    def __repr__(self) -> str:
        return f"Paciente(rut='{self.rut}', nombre='{self.nombre}', edad='{self.edad}', prevision='{self.prevision}')"

    