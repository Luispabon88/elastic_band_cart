import streamlit as st

from views.home import show_home
from modules.energia_trabajo_potencia import app_energia_trabajo_potencia


st.set_page_config(
    page_title="eΦKart App",
    page_icon="🛒",
    layout="wide"
)


def main():
    st.sidebar.title("eΦKart App")

    menu = st.sidebar.radio(
        "Selecciona una sección",
        [
            "Inicio",
            "Trabajo, energía y potencia"
        ]
    )

    if menu == "Inicio":
        show_home()

    elif menu == "Trabajo, energía y potencia":
        app_energia_trabajo_potencia()


if __name__ == "__main__":
    main()
