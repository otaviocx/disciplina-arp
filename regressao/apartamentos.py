import numpy as np
import pandas as pd
import math


def coefficient_calculate(apartments, num_vars):
    # vetor y
    apartments_price = apartments[:, 1]

    # matrix X com 1's na primeira coluna
    apartments_vars = np.append(np.ones([len(apartments_price), 1]), apartments[:, 2:num_vars], 1)

    # vetor b
    coefficients = np.dot(
        np.linalg.inv(np.dot(np.transpose(apartments_vars), apartments_vars)),
        np.dot(np.transpose(apartments_vars), apartments_price)
    )
    return coefficients


def multi_regression(coefficients, input_values):
    return np.dot(np.transpose(coefficients), [1]+input_values)

# QUESTÃO 4
aparts = pd.read_csv("apartamentos.csv", delimiter=";").as_matrix()
foreseen_value = multi_regression(
    coefficient_calculate(aparts, 5),
    [80, 10, 9]
)
print(foreseen_value)

# QUESTÃO 5
foreseen_value = multi_regression(
    coefficient_calculate(aparts, 7),
    [100, 3, 5, 3, 2]
)
print(foreseen_value)
