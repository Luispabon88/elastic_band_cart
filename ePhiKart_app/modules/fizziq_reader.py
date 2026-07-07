import pandas as pd
from io import StringIO


def read_fizziq_file(uploaded_file):
    """
    Lector específico para archivos CSV exportados desde FizziQ.
    Detecta la fila donde inicia la tabla: #;t;x;Vx;Ax
    """

    uploaded_file.seek(0)
    content = uploaded_file.read().decode("utf-8", errors="ignore")

    lines = content.splitlines()

    header_index = None

    for i, line in enumerate(lines):
        clean_line = line.strip()

        if clean_line.startswith("#;") or clean_line.startswith("#,"):
            header_index = i
            break

    if header_index is None:
        raise ValueError(
            "No se encontró la fila de encabezados de FizziQ. "
            "Debe existir una fila tipo: #;t;x;Vx;Ax"
        )

    table_text = "\n".join(lines[header_index:])

    # Detectar separador
    header_line = lines[header_index]

    if ";" in header_line:
        sep = ";"
    elif "," in header_line:
        sep = ","
    else:
        sep = "\t"

    df = pd.read_csv(
        StringIO(table_text),
        sep=sep,
        decimal=",",
        engine="python"
    )

    # Limpiar columnas
    df.columns = [str(col).strip() for col in df.columns]

    # Convertir datos numéricos
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def detect_columns(df):
    detected = {
        "time": None,
        "position": None,
        "velocity": None,
        "acceleration": None
    }

    for col in df.columns:
        col_lower = str(col).lower().strip()

        if col_lower in ["t", "tiempo", "time", "t(s)", "t (s)"]:
            detected["time"] = col

        elif col_lower in ["x", "posición", "posicion", "position", "x(m)", "x (m)"]:
            detected["position"] = col

        elif col_lower in ["vx", "v", "velocidad", "velocity", "v(m/s)", "v (m/s)"]:
            detected["velocity"] = col

        elif col_lower in ["ax", "a", "aceleracion", "aceleración", "acceleration", "a(m/s2)", "a (m/s2)"]:
            detected["acceleration"] = col

    return detected
