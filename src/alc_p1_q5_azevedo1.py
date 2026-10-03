import numpy as np


def norma_p_matriz_2por2(matriz, p, resolucao=1000):
    max_norm = 0.0

    for i in range(resolucao + 1):
        theta = 2 * np.pi * i / resolucao
        # Geração de vetor (x1, x2) na circunferência unitária p-norma
        x1 = np.cos(theta)
        x2 = np.sin(theta)

        # Normaliza o vetor para norma-p unitária
        norma_x = (abs(x1)**p + abs(x2)**p)**(1/p)
        x = np.array([x1 / norma_x, x2 / norma_x])

        # Multiplica Ax
        Ax = matriz @ x

        # Calcula norma-p de Ax
        norma_Ax = (abs(Ax[0])**p + abs(Ax[1])**p)**(1/p)
        max_norm = max(max_norm, norma_Ax)

    return max_norm
