'''Lista 2 - Exercicio 4 - FORD 7.32'''

import numpy as np

def main():
    print("Exercicio 4 - FORD 7.32")
    print("="*30)

    n = int(input("Entre com o valor de n: "))

    if n <= 0:
        print("O valor de n deve ser maior que zero.")
        return

    U = np.zeros(n)
    V = np.zeros(n)

    for i in range(n): # dois vetores de tamanho n
        U[i] = i + 1
        V[i] = U[i]**2

    print(f"Vetor U: {U}\n")
    print(f"Vetor V: {V}\n")

    A = U @ V.T
    print(f"Matriz A (uvT): {A}\n")

    PostoA = np.linalg.matrix_rank(A)
    print(f"Posto da matriz A (uvT): {PostoA}")

    NulidadeA = A.size - PostoA
    print(f"Nulidade da matriz A (n-PostoA): {NulidadeA}")

    Norma2U = np.linalg.norm(U)
    print(f"Norma do vetor U: {Norma2U}")

    Norma2V = np.linalg.norm(V)
    print(f"Norma do vetor V: {Norma2V}")

    Norma2A = np.linalg.norm(A)
    print(f"Norma da matriz A: {Norma2A}")

if __name__ == "__main__":
    main()