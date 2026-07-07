import streamlit as st


def show_home():
    st.title("🛒 eΦKart App")
    st.subheader("Asistente de análisis experimental para laboratorios de Física")

    st.divider()

    st.markdown(
        """
        La **eΦKart App** permite procesar datos experimentales obtenidos
        con **FizziQ** durante actividades de laboratorio.

        Esta aplicación **no reemplaza el experimento físico ni el análisis de video**.
        Su función es ayudar a transformar los datos obtenidos por los estudiantes
        en gráficas, cálculos e interpretaciones físicas.
        """
    )

    st.info(
        """
        Flujo general: experimento físico → video → análisis en FizziQ →
        exportación CSV → análisis en eΦKart App.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("✅ Lectura de datos FizziQ")
        st.caption("Carga y visualización inicial de archivos CSV.")

    with col2:
        st.warning("🚧 Trabajo, energía y potencia")
        st.caption("Cálculos teóricos y experimentales.")

    with col3:
        st.warning("🚧 Reportes")
        st.caption("Exportación futura de resultados.")

    st.divider()

    st.caption("Desarrollado por eΦCiencia · Versión 0.1")
