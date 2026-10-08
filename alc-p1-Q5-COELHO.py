
import os

import numpy as np

# requisitos da questão:
# 1. Construir L e U sem pivotamento e lançar exceção se o pivô for nulo.
# 2. Resolver Ly = b e Ux = y por substituições implementadas manualmente.
# 3. Retornar L, U e x, nessa ordem.
# 4. Nome do arquivo segue o padrão alc-p1-Q5-<nome>.py.
# 5. Usar NumPy somente para criar arrays e matrizes auxiliares.


def resolve_lu(A, b):
    # A matriz de trabalho guarda U acima da diagonal e os multiplicadores
    # de L abaixo dela, como no algoritmo dado em sala.

    n = len(b)
    LU = np.array(A)

    for k in range(n):
        # Um pivô zero impede continuar sem pivotamento.
        if LU[k, k] == 0:
            raise Exception('Pivo nulo. Utilize outra funcao com pivotamento.')

        for i in range(k + 1, n):
            # Calcula o multiplicador e o guarda abaixo da diagonal.
            m = LU[i, k] / LU[k, k]
            LU[i, k] = m

            # Atualiza as colunas à direita do pivô para formar U.
            for j in range(k + 1, n):
                LU[i, j] = LU[i, j] - m * LU[k, j]

    # Separa manualmente L e U da matriz de trabalho.
    # np.eye cria a diagonal 1 de L; np.zeros inicia U com zeros.
    L = np.eye(n)
    U = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i > j:
                L[i, j] = LU[i, j]
            else:
                U[i, j] = LU[i, j]

    # [Item 2] Substituição progressiva manual para resolver Ly = b.
    y = np.zeros(n)
    for i in range(n):
        soma = 0
        for j in range(i):
            soma = soma + L[i, j] * y[j]
        # A diagonal de L vale 1, então não é necessário dividir.
        y[i] = b[i] - soma

    # [Item 2] Substituição regressiva manual para resolver Ux = y.
    solucao = np.zeros(n)
    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma = soma + U[i, j] * solucao[j]
        solucao[i] = (y[i] - soma) / U[i, i]

    # [Item 3] Retorna os três objetos na ordem solicitada.
    return L, U, solucao


def main():
    os.system('cls')

    # Exemplo de sistema Ax = b para demonstrar a função.
    A = np.array([[2, 1, 1], [4, 3, 3], [8, 7, 9]])
    b = np.array([4, 10, 24])

    try:
        L, U, solucao = resolve_lu(A, b)
    except Exception as e:
        print(f"Erro: {e}")
        return

    # Exibe a fatoração e a solução encontrada.
    print('Matriz L:')
    print(f'{L}\n')
    print('Matriz U:')
    print(f'{U}\n')
    print('Solucao x:')
    print(f'{solucao}')


if __name__ == '__main__':
    main()
