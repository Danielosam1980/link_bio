import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", "https://www.youtube.com"),
        link_button("Youtube", "https://www.google.com"),
        link_button("Facebook", "https://www.facebook.com"),
        link_button("Pokemon Go!", "https://www.unap.edu.pe"),
        align_items="center"   
    )