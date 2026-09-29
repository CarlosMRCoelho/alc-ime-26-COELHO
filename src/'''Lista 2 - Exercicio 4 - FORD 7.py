'''Lista 2 - Exercicio 4 - FORD 7.32'''

import numpy as np

def main():
    print("Exercicio 4 - FORD 7.32")
    print("="*30)

    n = int(input("Entre com o valor de n: "))

    if n <= 0:
        print("O valor de n deve ser maior que zero.")
        return

    U = np.random.rand(n, 1)
    V = np.random.rand(n, 1)       

    print(f"Vetor U: {U}\n")
    print(f"Vetor V: {V}\n")

    A = np.outer(U, V) # produto externo dos vetores U e V
    print(f"Matriz A (uvT): {A}\n")

    PostoA = np.linalg.matrix_rank(A)
    print(f"Posto da matriz A (uvT): {PostoA}")

    NulidadeA = n - PostoA
    print(f"Nulidade da matriz A (n-PostoA): {NulidadeA}")

    Norma2U = np.linalg.norm(U, 2)
    Norma2V = np.linalg.norm(V, 2)
    print(f"Norma2 do vetor U x Norma2 do vetor V: {Norma2U * Norma2V:.4f}")

    Norma2A = np.linalg.norm(A, 2)
    print(f"Norma da matriz A: {Norma2A:.4f}")

if __name__ == "__main__":
    main()