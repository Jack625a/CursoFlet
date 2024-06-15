import flet as ft

class Tarea(ft.Row):
    def __init__(self, texto):
        super().__init__()
        self.texto_vista = ft.Text(texto)
        self.texto_editar = ft.TextField(value=texto, visible=False)
        self.boton_editar = ft.IconButton(icon=ft.icons.EDIT, on_click=self.editar)
        self.boton_guardar = ft.IconButton(icon=ft.icons.SAVE, visible=False, on_click=self.guardar)
        self.controls = [
            ft.Checkbox(),
            self.texto_vista,
            self.texto_editar,
            self.boton_editar,
            self.boton_guardar,
        ]

    def editar(self, e):
        self.texto_vista.visible = False
        self.texto_editar.visible = True
        self.boton_editar.visible = False
        self.boton_guardar.visible = True
        self.update()

    def guardar(self, e):
        self.texto_vista.value = self.texto_editar.value
        self.texto_vista.visible = True
        self.texto_editar.visible = False
        self.boton_editar.visible = True
        self.boton_guardar.visible = False
        self.update()
