"""Esta clase modela los datos de un usuario"""
from dataclasses import dataclass

# Decorador -> Extiende la funcionalidad de mi class o funciones
@dataclass
class User:
    fname: str
    lname: str
    age: int
    email: str
    telefono: str
    carrera: str