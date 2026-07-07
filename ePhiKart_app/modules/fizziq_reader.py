import pandas as pd


def read_fizziq_file(uploaded_file):

    separadores = [",", ";", "\t"]

    errores = []

    for sep in separadores:

        try:

            uploaded_file.seek(0)

            df = pd.read_csv(
                uploaded_file,
                sep=sep,
                engine="python"
            )

            # Si solo encontró una columna probablemente el separador es incorrecto
            if len(df.columns) > 1:
                return df

        except Exception as e:
            errores.append(str(e))

    raise Exception(
        "No fue posible interpretar el archivo CSV.\n\n"
        + "\n".join(errores)
    )
