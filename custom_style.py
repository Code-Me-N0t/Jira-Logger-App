from tkinter import ttk
from color_scheme import Color

class CustomStyle:
    def __init__(self):
        self.color = Color()
        self.style = ttk.Style()
        self.create_style()

    def create_style(self):
        self.style.theme_create("custom_theme", parent="alt", settings={
            "TNotebook": {
                "configure": {
                    "tabmargins": [2, 5, 2, 0],
                    "background": self.color.secondary_bg,
                    "borderwidth": 0,
                    "foreground": self.color.secondary_fg,
                }
            },
            "TNotebook.Tab": {
                "configure": {
                    "padding": [5, 5],
                    "background": self.color.secondary_bg,
                    "borderwidth": 0,
                    "foreground": self.color.secondary_fg,
                },
                "map": {
                    "background": [
                        ("!selected", self.color.secondary_bg),
                        ("selected", self.color.primary_bg)
                    ],
                    "expand": [("selected", [1, 1, 1, 0])]
                }
            },
            "CustomFrame.TFrame": { 
                "configure": {
                    "background": self.color.primary_bg,
                }
            }
        })

    def apply_style(self):
        self.style.theme_use("custom_theme")