'''
Lista 4 - Exercicio 5

Implementar decomposição QR por Gram-Schmidt
'''

import numpy as np


def modqrgrsch(A):

    m, n = A.shape  # tamanho da matriz A

    Q = np.zeros((m, n))  # matriz Q inicialmente zerada
    R = np.zeros((n, n))  # matriz R inicialmente zerada

    for i in range(n):  # percorre as colunas da matriz

        Q[:, i] = A[:, i]  # copia a coluna de A para Q

        for j in range(i):  # percorre as colunas anteriores

            # calcula o produto escalar entre as colunas
            R[j, i] = np.dot(Q[:, j], Q[:, i])

            # retira a projeção da coluna atual
            Q[:, i] = Q[:, i] - R[j, i] * Q[:, j]

        # calcula a norma da coluna
        R[i, i] = np.linalg.norm(Q[:, i])

        # divide a coluna pela norma para normalizar
        Q[:, i] = Q[:, i] / R[i, i]

    return Q, R


def main():

    np.set_printoptions(precision=4, suppress=True)

    # matriz utilizada no exercício
    A = np.array([
        [1, 9, 0, 5, 3, 2],
        [-6, 3, 8, 2, -8, 0],
        [3, 15, 23, 2, 1, 7],
        [3, 57, 35, 1, 7, 9],
        [3, 5, 6, 15, 55, 2],
        [33, 7, 5, 3, 5, 7]
    ], dtype=float)

    # calcula as matrizes Q e R
    Q, R = modqrgrsch(A)

    # mostra a matriz A
    print("Matriz A:")
    print(A)

    # mostra a matriz Q
    print("\nMatriz Q:")
    print(Q)

    # mostra a matriz R
    print("\nMatriz R:")
    print(R)

    # verifica se A é igual a Q vezes R
    print("\nA - Q @ R:")
    print(A - Q @ R)

    # verifica se Q.T @ Q é igual à matriz identidade
    print("\nQ.T @ Q:")
    print(Q.T @ Q)

    # calcula a decomposição QR usando a função do numpy
    Qn, Rn = np.linalg.qr(A)

    # ajusta os sinais para facilitar a comparação
    s = np.sign(np.diag(Rn))
    Qn = Qn * s
    Rn = (Rn.T * s).T

    # compara os resultados com o numpy
    print("\nComparação com numpy:")
    print("Q igual:", np.allclose(Q, Qn))
    print("R igual:", np.allclose(R, Rn))


if __name__ == "__main__":
    main()
