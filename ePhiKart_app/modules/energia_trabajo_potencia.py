import streamlit as st


def app_energia_trabajo_potencia():
    st.title("⚙️ Trabajo, energía y potencia")
    st.warning("Este módulo está en desarrollo.")

    st.markdown(
        """
        Próximamente este módulo permitirá calcular:

        - velocidad
        - aceleración
        - energía cinética
        - fuerza
        - potencia
        - trabajo
        - comparación teoría–experimento
        """
    )

    if "fizziq_data" in st.session_state:
        st.success("Ya existe un archivo de FizziQ cargado en la sesión.")
        st.dataframe(st.session_state["fizziq_data"], use_container_width=True)
    else:
        st.info("Primero carga un archivo desde la sección `Cargar datos FizziQ`.")
