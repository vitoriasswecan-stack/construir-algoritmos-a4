import pandas as pd     
import numpy as np


def regressao_linear(arquivo):
    df = pd.read_csv(arquivo)
    area = df["area_util_m2"].to_list()
    quartos = df["quantidade_quartos"].to_list()


    preco = df["preco_venda"].to_list()

    X = np.column_stack((
        np.ones(len(area)),
        area,
        quartos
    ))


    Y = np.array(preco)


    beta = np.linalg.inv(X.T @ X) @ X.T @ Y

    return beta.tolist()