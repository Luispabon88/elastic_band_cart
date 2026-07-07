import pandas as pd


def clean_dataframe(df):
    """
    Limpieza inicial del archivo:
    - elimina filas completamente vacías
    - elimina columnas completamente vacías
    - intenta convertir columnas numéricas
    """

    df = df.copy()

    df = df.dropna(how="all")
    df = df.dropna(axis=1, how="all")

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(",", ".", regex=False)
            )

            df[col] = pd.to_numeric(df[col], errors="ignore")

    return df
