from pathlib import Path
import sys
import tkinter as tk
from tkinter import ttk

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from services.user_service import UserService

class AppWindow(tk.Tk):
    def __init__(self, service: UserService) -> None:
        super().__init__()

        self.service = service

        self.title("Registro de Usuarios")
        self.geometry("1100x700")
        self.configure(bg="#D6EAF8")   # Color de fondo

        self.create_widget()

    def create_widget(self):

        self.render_entries()

        self.button = tk.Button(
            self,
            text="Registrar Usuario",
            command=self.create_new_user,
            bg="#3498DB",
            fg="white"
        )
        self.button.pack(pady=5)

        self.delete_button = tk.Button(
            self,
            text="Eliminar Usuario",
            command=self.delete_user,
            bg="#E74C3C",
            fg="white"
        )
        self.delete_button.pack(pady=5)

        self.create_data_table()
        self.render_data_table()

    def render_entries(self):

        tk.Label(self, text="Nombre", bg="#D6EAF8").pack()
        self.entry_fname = tk.Entry(self)
        self.entry_fname.pack()

        tk.Label(self, text="Apellido", bg="#D6EAF8").pack()
        self.entry_lname = tk.Entry(self)
        self.entry_lname.pack()

        tk.Label(self, text="Edad", bg="#D6EAF8").pack()
        self.entry_age = tk.Entry(self)
        self.entry_age.pack()

        tk.Label(self, text="Correo", bg="#D6EAF8").pack()
        self.entry_email = tk.Entry(self)
        self.entry_email.pack()

        tk.Label(self, text="Teléfono", bg="#D6EAF8").pack()
        self.entry_telefono = tk.Entry(self)
        self.entry_telefono.pack()

        tk.Label(self, text="Carrera", bg="#4085B7").pack()
        self.entry_carrera = tk.Entry(self)
        self.entry_carrera.pack()

    def clear_entries(self):

        self.entry_fname.delete(0, "end")
        self.entry_lname.delete(0, "end")
        self.entry_age.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_telefono.delete(0, "end")
        self.entry_carrera.delete(0, "end")

        self.entry_fname.focus()

    def create_new_user(self):

        fname = self.entry_fname.get()
        lname = self.entry_lname.get()
        age = self.entry_age.get()
        email = self.entry_email.get()
        telefono = self.entry_telefono.get()
        carrera = self.entry_carrera.get()

        self.service.create_one (fname, lname, age, email, telefono, carrera )

        self.render_data_table()
        self.clear_entries()

    def delete_user(self):

        seleccionado = self.tree.selection()

        if seleccionado:
            indice = self.tree.index(seleccionado[0])
            self.service.delete_one(indice)
            self.render_data_table()

    def create_data_table(self):

        self.tree = ttk.Treeview(
            self,
            columns=("fname", "lname", "age", "email", "telefono",  "carrera"),
            show="headings"
        )

        self.tree.heading("fname", text="Nombre")
        self.tree.heading("lname", text="Apellido")
        self.tree.heading("age", text="Edad")
        self.tree.heading("email", text="Correo")
        self.tree.heading("telefono", text="Teléfono")
        self.tree.heading("carrera", text="Carrera")

        self.tree.column("fname", width=120, anchor="center")
        self.tree.column("lname", width=120, anchor="center")
        self.tree.column("age", width=60, anchor="center")
        self.tree.column("email", width=220, anchor="center")
        self.tree.column("telefono", width=130, anchor="center")
        self.tree.column("carrera", width=180, anchor="center")

        self.tree.pack(pady=20)

    def render_data_table(self):

        users = self.service.find_all()

        for item in self.tree.get_children():
            self.tree.delete(item)

        for user in users:
            self.tree.insert(
                "",
                "end",
                values=( user.fname, user.lname, user.age, user.email, user.telefono, user.carrera )
            )