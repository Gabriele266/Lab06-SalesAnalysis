import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()


    def handle_year_select(self, event):
        d = event.data
        if d == "none":
            self._model.selected_year = None
        else:
            self._model.selected_year = int(d)

    def handle_brand_select(self, event):
        d = event.data
        if d == "none":
            self._model.selected_brand = None
        else:
            self._model.selected_brand = d