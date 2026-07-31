"""Se encarga de gestionar el almacenamiento de los datos en memoria."""

from models.user import User

class UserRepository:
    # Simula mi base de datos
    _users: list[User] = []

    def __init__(self) -> None:
        pass

    def find_all(self) -> list[User]:
        """Retorna todos los usuarios registrados."""
        return self._users

    def create_one(self, user: User):
        self._users.append(user)

    def delete_one(self, index: int):
        """Elimina un usuario por su posición en la lista."""
        if 0 <= index < len(self._users):
            self._users.pop(index) 
    