import pandas as pd


def read_fizziq_file(uploaded_file):
    """
    Lee un archivo CSV exportado desde FizziQ.
    Se intenta primero con separador coma y luego con punto y coma.
    """

    try:
        df = pd.read_csv(uploaded_file)
    except Exception:
        uploaded_file.seek(0)
        df = pd.read_csv(uploaded_file, sep=";")

    return df


def detect_columns(df):
    """
    Detección preliminar de columnas comunes en archivos de movimiento.
    No modifica el dataframe.
    """

    detected = {
        "time": None,
        "position": None,
        "velocity": None,
        "acceleration": None
    }

    for col in df.columns:
        col_lower = str(col).lower()

        if "time" in col_lower or "tiempo" in col_lower or col_lower in ["t", "t(s)", "t (s)"]:
            detected["time"] = col

        elif "position" in col_lower or "posición" in col_lower or "posicion" in col_lower or col_lower in ["x", "x(m)", "x (m)"]:
            detected["position"] = col

        elif "velocity" in col_lower or "velocidad" in col_lower or col_lower in ["v", "v(m/s)", "v (m/s)"]:
            detected["velocity"] = col

        elif "acceleration" in col_lower or "aceleración" in col_lower or "aceleracion" in col_lower or col_lower in ["a", "a(m/s2)", "a (m/s2)"]:
            detected["acceleration"] = col

    return detected
