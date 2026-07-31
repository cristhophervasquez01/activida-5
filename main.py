from models.user import User
from repositories.user_repository import UserRepository
from services.user_service import UserService
from ui.app_window import AppWindow
from tkinter import ttk

def main():
    repository = UserRepository()
    service = UserService(repository)

    app_window = AppWindow(service)

    app_window.mainloop()


if __name__ == "__main__":
    main()