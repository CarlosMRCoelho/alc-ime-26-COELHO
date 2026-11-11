"""Lista 03 - Questão 2.

Produto vetorial (crossprod) de dois vetores de R³ e produtos escalares
<u x v, u> e <v x u, v>.
"""

import os

import numpy as np


def verifica_r3(vetor):
    """Verifica se o vetor pertence a R³."""
    if len(vetor) != 3:
        raise ValueError("O vetor não pertence a R³")
    return True


def ler_vetor(nome):
    """Lê um vetor com três coordenadas inteiras."""
    entrada = input(f"Digite o vetor {nome} (ex: 1,2,3): ")
    return np.array([int(valor.strip()) for valor in entrada.split(",")])


def crossprod(u, v):
    """Calcula o produto vetorial entre dois vetores de R³."""
    return np.array(
        [
            u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0],
        ]
    )


def main():
    os.system("cls")

    print("Cálculo do produto vetorial de dois vetores em R³")
    print("=" * 50)

    while True:
        try:
            u = ler_vetor("u")
            v = ler_vetor("v")

            if verifica_r3(u) and verifica_r3(v):
                break

        except ValueError as erro:
            print(f"\nErro: {erro}")
            print("Digite os vetores novamente.\n")

        except KeyboardInterrupt:
            print("\nPrograma interrompido pelo usuário.")
            return

    print("\nResultados:")
    print(f"Vetor u         : {u}")
    print(f"Vetor v         : {v}")
    print(f"Produto vetorial (u x v): {crossprod(u, v)}")
    print(f"Produto vetorial (v x u): {crossprod(v, u)}")
    print(f"Produto escalar <u x v, u>: {np.dot(crossprod(u, v), u)}")
    print(f"Produto escalar <v x u, v>: {np.dot(crossprod(v, u), v)}")


if __name__ == "__main__":
    main()
