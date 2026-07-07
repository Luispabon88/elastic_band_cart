import streamlit as st


def show_home():

    st.title("🧪 eΦKart App")

    st.subheader(
        "Plataforma para el análisis experimental de laboratorios de Física"
    )

    st.divider()

    st.markdown(
        """
La **eΦKart App** es una plataforma desarrollada por el grupo **eΦCiencia**
para complementar las actividades experimentales de Mecánica.

La aplicación **no reemplaza el experimento físico ni el análisis del video**.
Su propósito es transformar los datos obtenidos mediante **FizziQ**
en resultados científicos que permitan interpretar el fenómeno físico.
"""
    )

    st.divider()

    st.header("Objetivo")

    st.info(
        """
Transformar los datos obtenidos durante el laboratorio en evidencia
científica mediante cálculos físicos, gráficas y comparación entre
modelos teóricos y experimentales.
"""
    )

    st.divider()

    st.header("Flujo de trabajo")

    st.markdown(
        """
1️⃣ Realizar el experimento físico.

⬇️

2️⃣ Grabar el movimiento.

⬇️

3️⃣ Analizar el video con FizziQ.

⬇️

4️⃣ Exportar la tabla de datos.

⬇️

5️⃣ Cargar los datos en eΦKart App.

⬇️

6️⃣ Obtener análisis, gráficas y comparación teoría–experimento.
"""
    )

    st.divider()

    st.header("Módulos")

    col1, col2 = st.columns(2)

    with col1:

        st.success("✅ Trabajo, Energía y Potencia")

        st.info("🚧 Movimiento del carrito")

        st.info("🚧 Conservación de la energía")

    with col2:

        st.info("🚧 Dinámica")

        st.info("🚧 Cinemática")

        st.info("🚧 Próximamente...")

    st.divider()

    st.caption(
        """
Desarrollado por el grupo eΦCiencia.

Versión 0.1
"""
    )
