import streamlit as st
from modules.energia_trabajo_potencia import app_energia_trabajo_potencia

st.set_page_config(
    page_title="eΦCiencia App",
    page_icon="🧪",
    layout="wide"
)

st.title("eΦKart App")
st.subheader("Asistente de análisis experimental para laboratorios de física")

st.info(
    "La aplicación no reemplaza el experimento ni el análisis de video. "
    "Procesa los datos obtenidos por los estudiantes mediante FizziQ."
)

menu = st.sidebar.selectbox(
    "Selecciona una actividad",
    [
        "Inicio",
        "Trabajo, energía y potencia"
    ]
)

if menu == "Inicio":
    st.markdown("""
    ## Flujo de trabajo

    1. El estudiante realiza el experimento físico.
    2. Graba el movimiento.
    3. Analiza el video en FizziQ.
    4. Exporta la tabla de datos.
    5. Carga los datos en esta aplicación.
    6. Compara resultados teóricos y experimentales.
    """)

elif menu == "Trabajo, energía y potencia":
    app_energia_trabajo_potencia()
