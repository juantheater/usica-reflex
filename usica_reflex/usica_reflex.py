import reflex as rx

from rxconfig import config
from .ui.base import base_page


def index() -> rx.Component:
    # Welcome Page (Index)
    index_child=(
        rx.vstack(
            rx.heading(
                "Bienvenidos a Reflex!",
                size="9"
            ),
            rx.text(
                "Este es el curso de reflex ",
                rx.code(
                    f"{config.app_name}/{config.app_name}.py"
                ),
                size="5",
            ),
            rx.link(
                rx.button(
                    "Check out our docs!",
                    color_scheme="tomato"
                ),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )
    return base_page(index_child)


app = rx.App()
app.add_page(index)
