import reflex as rx
from .nav import navbar

def base_page(child:rx.Component,*args,**kwargs)->rx.Component:
    return rx.fragment(
        navbar(),
        rx.box(
            rx.center(child),
            bg=rx.color("accent", 3),
            padding="1em",
            width="100%"
        ),
        rx.color_mode.button(position="botton-left"),
    )