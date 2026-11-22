'''
Lista 4 - Exercício 2

Fatoração LU com pivoteamento parcial
'''

import numpy as np
from scipy.linalg import lu


def ludecomp(A):

    n = A.shape[0]  # tamanho da matriz

    L = np.eye(n)  # matriz L começa como identidade
    P = np.eye(n)  # matriz P começa como identidade

    for i in range(n - 1):  # percorre as colunas até a penúltima

        # procura o maior valor da coluna para escolher o pivô
        k = i + np.argmax(np.abs(A[i:, i]))

        # verifica se é necessário trocar as linhas
        if k != i:

            # troca as linhas da matriz A
            A[[i, k], :] = A[[k, i], :]

            # troca as linhas da matriz P
            P[[i, k], :] = P[[k, i], :]

            # troca os valores anteriores da matriz L
            L[[i, k], :i] = L[[k, i], :i]

        # calcula os multiplicadores para zerar os valores abaixo do pivô
        m = A[i + 1:, i] / A[i, i]

        # atualiza os valores da matriz A
        A[i + 1:, i:] = A[i + 1:, i:] - np.outer(m, A[i, i:])

        # guarda os multiplicadores na matriz L
        L[i + 1:, i] = m

        # zera os valores abaixo do pivô na matriz A
        A[i + 1:, i] = 0

    # a matriz A atualizada passa a ser a matriz U
    U = A

    return L, U, P


def main():

    print("Fatoração LU com pivoteamento parcial")
    print("------------------------------------")

    # matriz utilizada no exercício
    A = np.array([
        [1, 2, 3],
        [2, 4, 5],
        [3, 4, 5]
    ], dtype=float)

    # mostra a matriz A
    print("Matriz A:")
    print(A)

    print("------------------------------------")

    # calcula as matrizes L, U e P
    L, U, P = ludecomp(A.copy())

    # mostra a matriz L
    print("L:")
    print(L)

    # mostra a matriz U
    print("U:")
    print(U)

    # mostra a matriz P
    print("P:")
    print(P)

    # verifica se P @ A é igual a L @ U
    print("\nP @ A - L @ U:")
    print(P @ A - L @ U)

    # calcula a fatoração usando o scipy
    Ps, Ls, Us = lu(A, permute_l=False, p_indices=False)

    # compara os resultados com o scipy
    print("\nComparação com scipy:")
    print("L igual:", np.allclose(L, Ls))
    print("U igual:", np.allclose(U, Us))
    print("P igual:", np.allclose(P, Ps.T))


if __name__ == "__main__":
    main()
