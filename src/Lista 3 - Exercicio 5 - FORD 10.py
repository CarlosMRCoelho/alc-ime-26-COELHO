"""Lista 3 - Exercicio 5 - FORD 10.21"""

import os

import matplotlib.pyplot as plt
import numpy


def diag(n: int) -> numpy.ndarray:
    """Cria uma matriz bidiagonal de ordem n com elementos de 1 a n."""
    A = numpy.zeros((n, n))
    for i in range(n):
        A[i][i] = n - i
        if i < n - 1:
            A[i][i + 1] = n

    return A


def Plot_numero_condicao(n: int) -> None:
    """Plota o número de condição da matriz bidiagonal de ordem n."""

    cond_numeros = []
    ordens = list(range(1, n + 1))

    for ordem in ordens:
        A = diag(ordem)
        cond_A = numpy.linalg.cond(A)
        cond_numeros.append(cond_A)

    plt.plot(ordens, cond_numeros, marker="o")
    plt.title("Número de Condição da Matriz Bidiagonal")
    plt.xlabel("Ordem da Matriz (n)")
    plt.ylabel("Número de Condição")
    plt.grid()
    plt.show()


def Autovalores_perturbados() -> None:
    """Compara os autovalores da matriz de Wilkinson de ordem 20 com os da matriz perturbada em A[19][0]."""

    A = diag(20)
    autovalores_A = numpy.sort(numpy.linalg.eigvals(A))[::-1]

    B = A.copy()
    B[19][0] += 1e-10
    autovalores_B = numpy.sort(numpy.linalg.eigvals(B))[::-1]

    print()
    print("Comparação de Autovalores perturbados:")
    print("=" * 40)
    print(f"{'k':>3} | {'A':>10} | {'A perturbada':>24}")
    print("-" * 44)

    for k in range(20):
        a = autovalores_A[k]
        b = autovalores_B[k]
        print(f"{k + 1:>3} | {a.real:>10.6f} | {b.real:>12.6f} {b.imag:+10.6f}j")


def main():
    os.system("cls")
    print("Exercicio 5 - FORD 10.21")
    print("Matriz bidiagonal Wilkinson")
    print()

    # Entrada de dados

    n = int(input("Digite a ordem da matriz (n): "))

    if n < 1:
        print("A ordem da matriz deve ser maior ou igual a 1.")
        return

    A = diag(n)

    # Saida de dados

    print("Matriz A:")
    print(A)

    # Plota o número de condição da matriz.

    Plot_numero_condicao(n)

    # Compara os autovalores da matriz de Wilkinson com os da matriz perturbada.

    Autovalores_perturbados()


if __name__ == "__main__":
    main()
