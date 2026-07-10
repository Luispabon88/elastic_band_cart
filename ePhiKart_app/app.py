import streamlit as st

from views.home import show_home
from views.cargar_datos import show_cargar_datos
from modules.energia_trabajo_potencia import app_energia_trabajo_potencia


st.set_page_config(
    page_title="eΦKart App",
    page_icon=":racing_car:",
    layout="wide"
)


def main():
    st.sidebar.title(":racing_car: eΦKart Lab")
    st.sidebar.caption("Análisis experimental con datos de FizziQ")

    menu = st.sidebar.radio(
        "Menú principal",
        [
            "Inicio",
            "Cargar datos FizziQ",
            "Trabajo, energía y potencia"
        ]
    )

    if menu == "Inicio":
        show_home()

    elif menu == "Cargar datos FizziQ":
        show_cargar_datos()

    elif menu == "Trabajo, energía y potencia":
        app_energia_trabajo_potencia()


if __name__ == "__main__":
    main()
