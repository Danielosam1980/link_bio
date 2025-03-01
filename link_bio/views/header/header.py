import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="DL", size="4"),
        rx.text("dferrerllc@gmail.com"),
        rx.text("Hola mi nombre es Danilo"),
        rx.text("""Soy Ingeniero Informático desde ...
                luego estudié...
                luego trabajé....................................................
                jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"""),
        align="center",
        width="100%"
    )