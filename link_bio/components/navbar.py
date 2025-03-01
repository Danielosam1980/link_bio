import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            "Danilo",
            height="100%"
        ),
        position="sticky",
        bg="blue",
        padding_x="16px",
        padding_y="8px",
        z_index="999",
        align_items="center"
    )