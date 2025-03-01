import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(f"{datetime.date.today().year} dferrerllc@gmail.com", href="https://www.gmail.com", is_external=True),
        rx.text("Puno Daniel derechos reservados"),
        align_items="center"
        )
    