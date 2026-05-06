import flet as ft

from database.StatisticsDAO import StatisticsDAO

class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite by Gabri", color="blue", size=24)
        self._page.controls.append(self._title)

        self._page.controls.append(ft.Row(
            controls=[
                ft.Dropdown(
                    label="Anno",
                    options=
                        self.__map_years_to_options__(),
                    on_select=self._controller.handle_year_select
                ),
                ft.Dropdown(
                    label="Brand",
                    options=self.__map_brand_to_options(),
                    on_select=self._controller.handle_brand_select
                ),
                ft.Dropdown(
                    label="Retailer",
                    width=500,
                    options=self.__map_retailer_to_option(),
                    on_select=self._controller.handle_retailer_select
                )
            ]
        ))
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    def __map_years_to_options__(self):
        options = [
            ft.DropdownOption(
                key="none",
                text="Seleziona un anno"
            )
        ]

        years = StatisticsDAO.load_years_list()
        for y in years:
            options.append(ft.DropdownOption(
                key=str(y),
                text=str(y)
            ))

        return options

    def __map_brand_to_options(self):
        options = [
            ft.DropdownOption(
                key="none",
                text="Nessun brand selezionato"
            )
        ]

        brand = StatisticsDAO.load_brand_list()
        for b in brand:
            options.append(ft.DropdownOption(
                key=b,
                text=b
            ))

        return options

    def __map_retailer_to_option(self):
        options = [
            ft.DropdownOption(
                key="none",
                text="Nessun retailer selezionato"
            )
        ]

        retailer = StatisticsDAO.load_retailer_list()
        for r in retailer:
            options.append(ft.DropdownOption(
                key=str(r.code),
                text=r.name,
                data=r
            ))

        return options


    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
