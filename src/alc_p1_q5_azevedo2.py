import numpy as np


def norma_p_matriz_2por2(matriz, p, resolucao=1000):
    max_norm = 0.0

    dx = 2/resolucao

    x_0 = -1.0
    x_f = 1.0

    norms = []

    for i in range(resolucao + 1):
        x = x_0 + i*dx
        abs_y = np.power(1.0 - np.power(np.abs(x), p), 1/p)

        xy_transf = matriz @ np.array([[x],[abs_y]])

        x_ = xy_transf[0]
        y_ = xy_transf[1]

        norms.append(np.power(np.power(np.abs(x_), p) + np.power(np.abs(y_), p), 1/p))

    norma_matriz = max(norms)
    norma_matriz = norma_matriz[0]

    return norma_matriz
