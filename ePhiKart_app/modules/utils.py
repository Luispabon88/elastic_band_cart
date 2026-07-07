import numpy as np

def error_porcentual(valor_teorico, valor_experimental):
    if valor_teorico == 0:
        return np.nan
    return abs((valor_experimental - valor_teorico) / valor_teorico) * 100
