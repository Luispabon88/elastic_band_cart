import streamlit as st

from modules.fizziq_reader import read_fizziq_file, detect_columns
from modules.data_processing import clean_dataframe
from modules.plots import plot_basic_columns


def show_cargar_datos():
    st.title("📄 Cargar datos desde FizziQ")
    st.caption("Primera etapa: lectura, limpieza y visualización de datos exportados en CSV.")

    st.divider()

    uploaded_file = st.file_uploader(
        "Carga un archivo CSV exportado desde FizziQ",
        type=["csv"]
    )

    if uploaded_file is None:
        st.info("Carga un archivo `.csv` para comenzar.")
        return

    df_raw = read_fizziq_file(uploaded_file)

    st.subheader("1. Vista previa del archivo original")
    st.dataframe(df_raw, use_container_width=True)

    st.subheader("2. Datos limpios")
    df_clean = clean_dataframe(df_raw)
    st.dataframe(df_clean, use_container_width=True)

    st.subheader("3. Detección preliminar de columnas")
    detected = detect_columns(df_clean)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Columna de tiempo", detected.get("time", "No detectada"))

    with col2:
        st.metric("Columna de posición", detected.get("position", "No detectada"))

    with col3:
        st.metric("Columna de velocidad", detected.get("velocity", "No detectada"))

    st.subheader("4. Visualización rápida")

    columnas = df_clean.columns.tolist()

    if len(columnas) >= 2:
        x_col = st.selectbox("Eje X", columnas, index=0)
        y_col = st.selectbox("Eje Y", columnas, index=1)

        fig = plot_basic_columns(df_clean, x_col, y_col)
        st.plotly_chart(fig, use_container_width=True)

    st.session_state["fizziq_data"] = df_clean

    st.success("Archivo cargado correctamente.")
