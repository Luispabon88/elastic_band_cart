import streamlit as st
import pandas as pd
import numpy as np
import sympy as sp
import plotly.express as px
from scipy.integrate import trapezoid

from modules.utils import error_porcentual


def app_energia_trabajo_potencia():
    st.header("Actividad: Trabajo, Energía y Potencia")

    st.markdown("""
    Este módulo permite comparar el modelo teórico con los datos experimentales
    obtenidos desde FizziQ.
    """)

    tab1, tab2, tab3 = st.tabs(
        [
            "1. Modelo teórico",
            "2. Datos experimentales",
            "3. Comparación"
        ]
    )

    with tab1:
        modelo_teorico()

    with tab2:
        datos_experimentales()

    with tab3:
        comparacion_resultados()


def modelo_teorico():
    st.subheader("Modelo teórico")

    st.markdown("Ejemplo de entrada: `t + 2*t**3`")

    funcion_x = st.text_input(
        "Función de posición x(t)",
        value="t + 2*t**3"
    )

    masa = st.number_input(
        "Masa de la partícula o carrito (kg)",
        min_value=0.001,
        value=4.0,
        step=0.1
    )

    t_inicial = st.number_input("Tiempo inicial (s)", value=0.0)
    t_final = st.number_input("Tiempo final (s)", value=2.0)

    t = sp.symbols("t")

    try:
        x = sp.sympify(funcion_x)
        v = sp.diff(x, t)
        a = sp.diff(v, t)
        ec = sp.Rational(1, 2) * masa * v**2
        fuerza = masa * a
        potencia = fuerza * v
        trabajo = sp.integrate(potencia, (t, t_inicial, t_final))

        ec_inicial = ec.subs(t, t_inicial)
        ec_final = ec.subs(t, t_final)
        delta_ec = ec_final - ec_inicial

        st.session_state["teorico"] = {
            "masa": masa,
            "x": x,
            "v": v,
            "a": a,
            "ec": ec,
            "fuerza": fuerza,
            "potencia": potencia,
            "trabajo": float(trabajo),
            "ec_inicial": float(ec_inicial),
            "ec_final": float(ec_final),
            "delta_ec": float(delta_ec),
            "t_inicial": t_inicial,
            "t_final": t_final
        }

        col1, col2 = st.columns(2)

        with col1:
            st.latex(f"x(t) = {sp.latex(x)}")
            st.latex(f"v(t) = {sp.latex(v)}")
            st.latex(f"a(t) = {sp.latex(a)}")
            st.latex(f"E_c(t) = {sp.latex(ec)}")

        with col2:
            st.latex(f"F(t) = {sp.latex(fuerza)}")
            st.latex(f"P(t) = {sp.latex(potencia)}")
            st.metric("Trabajo teórico", f"{float(trabajo):.4f} J")
            st.metric("ΔEc teórico", f"{float(delta_ec):.4f} J")

        generar_graficas_teoricas(x, v, a, ec, fuerza, potencia, t_inicial, t_final)

    except Exception as e:
        st.error("No se pudo interpretar la función ingresada.")
        st.code(str(e))


def generar_graficas_teoricas(x, v, a, ec, fuerza, potencia, t_inicial, t_final):
    t = sp.symbols("t")

    t_vals = np.linspace(t_inicial, t_final, 200)

    funciones = {
        "x(t)": x,
        "v(t)": v,
        "a(t)": a,
        "Ec(t)": ec,
        "F(t)": fuerza,
        "P(t)": potencia
    }

    data = pd.DataFrame({"t": t_vals})

    for nombre, expr in funciones.items():
        f_num = sp.lambdify(t, expr, "numpy")
        data[nombre] = f_num(t_vals)

    st.subheader("Gráficas teóricas")

    variable = st.selectbox(
        "Selecciona la magnitud a graficar",
        ["x(t)", "v(t)", "a(t)", "Ec(t)", "F(t)", "P(t)"]
    )

    fig = px.line(
        data,
        x="t",
        y=variable,
        title=f"{variable} vs tiempo"
    )

    st.plotly_chart(fig, use_container_width=True)


def datos_experimentales():
    st.subheader("Datos experimentales desde FizziQ")

    archivo = st.file_uploader(
        "Carga el archivo .csv o .xlsx exportado desde FizziQ",
        type=["csv", "xlsx"]
    )

    if archivo is None:
        st.warning("Carga un archivo para continuar.")
        return

    if archivo.name.endswith(".csv"):
        df = pd.read_csv(archivo)
    else:
        df = pd.read_excel(archivo)

    st.write("Vista previa de los datos:")
    st.dataframe(df)

    columnas = df.columns.tolist()

    col_t = st.selectbox("Columna de tiempo", columnas)
    col_x = st.selectbox("Columna de posición", columnas)

    masa = st.number_input(
        "Masa experimental del carrito o partícula (kg)",
        min_value=0.001,
        value=4.0,
        step=0.1,
        key="masa_exp"
    )

    df = df[[col_t, col_x]].dropna()
    df = df.rename(columns={col_t: "t", col_x: "x"})
    df = df.sort_values("t")

    df["v"] = np.gradient(df["x"], df["t"])
    df["a"] = np.gradient(df["v"], df["t"])
    df["Ec"] = 0.5 * masa * df["v"]**2
    df["F"] = masa * df["a"]
    df["P"] = df["F"] * df["v"]

    trabajo_exp = trapezoid(df["P"], df["t"])
    delta_ec_exp = df["Ec"].iloc[-1] - df["Ec"].iloc[0]

    st.session_state["experimental"] = {
        "df": df,
        "trabajo": float(trabajo_exp),
        "delta_ec": float(delta_ec_exp),
        "ec_inicial": float(df["Ec"].iloc[0]),
        "ec_final": float(df["Ec"].iloc[-1])
    }

    st.subheader("Datos procesados")
    st.dataframe(df)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Trabajo experimental", f"{trabajo_exp:.4f} J")
        st.metric("Ec inicial experimental", f"{df['Ec'].iloc[0]:.4f} J")

    with col2:
        st.metric("ΔEc experimental", f"{delta_ec_exp:.4f} J")
        st.metric("Ec final experimental", f"{df['Ec'].iloc[-1]:.4f} J")

    variable = st.selectbox(
        "Magnitud experimental a graficar",
        ["x", "v", "a", "Ec", "F", "P"]
    )

    fig = px.line(
        df,
        x="t",
        y=variable,
        markers=True,
        title=f"{variable} experimental vs tiempo"
    )

    st.plotly_chart(fig, use_container_width=True)


def comparacion_resultados():
    st.subheader("Comparación teórica y experimental")

    if "teorico" not in st.session_state:
        st.warning("Primero calcula el modelo teórico.")
        return

    if "experimental" not in st.session_state:
        st.warning("Primero carga y procesa los datos experimentales.")
        return

    teorico = st.session_state["teorico"]
    experimental = st.session_state["experimental"]

    tabla = pd.DataFrame({
        "Magnitud": [
            "Trabajo",
            "ΔEc",
            "Ec inicial",
            "Ec final"
        ],
        "Teórico": [
            teorico["trabajo"],
            teorico["delta_ec"],
            teorico["ec_inicial"],
            teorico["ec_final"]
        ],
        "Experimental": [
            experimental["trabajo"],
            experimental["delta_ec"],
            experimental["ec_inicial"],
            experimental["ec_final"]
        ]
    })

    tabla["Error porcentual (%)"] = tabla.apply(
        lambda row: error_porcentual(row["Teórico"], row["Experimental"]),
        axis=1
    )

    st.dataframe(tabla)

    st.markdown("""
    ### Interpretación sugerida

    Si el trabajo realizado por la fuerza coincide aproximadamente con la variación
    de energía cinética, los datos experimentales son consistentes con el teorema
    trabajo-energía.
    """)

    fig = px.bar(
        tabla,
        x="Magnitud",
        y=["Teórico", "Experimental"],
        barmode="group",
        title="Comparación entre valores teóricos y experimentales"
    )

    st.plotly_chart(fig, use_container_width=True)
