''' SCHAUM 7.32 - Matriz Ortogonal  '''

import numpy as np
from numpy import linalg as la

def obter_vetor_inicial():

    print("Digite as componentes usando ponto decimal (exemplo: 0.6).")
    try:
        x = float(input("x: "))
        y = float(input("y: "))
        z = float(input("z: "))
    except ValueError:
        raise ValueError("Digite apenas numeros com ponto decimal.")

    vetor = np.array([x, y, z])
    norma = la.norm(vetor)
    # isclose aceita pequenos erros de arredondamento dos decimais.
    if not np.isclose(norma, 1, rtol=0, atol=1e-8):
        raise ValueError("O vetor deve ter norma 1.")

    return vetor

def calcular_vetores_perpendiculares(u1):

    x, y, z = u1

    # Usamos as duas componentes de maior modulo para evitar um vetor nulo.
    # Em cada caso, o produto interno de u1 com w2 e zero.
    if abs(x) <= abs(y) and abs(x) <= abs(z):
        w2 = np.array([0, z, -y])
    elif abs(y) <= abs(z):
        w2 = np.array([-z, 0, x])
    else:
        w2 = np.array([y, -x, 0])

    u2 = w2 / np.linalg.norm(w2)

    # O produto vetorial gera um vetor perpendicular aos dois anteriores.
    w3 = np.cross(u2, u1)
    u3 = w3 / np.linalg.norm(w3)

    return u1, u2, u3

def main():
    try:
        u1 = la.array([1, 0, 0])
        u1, u2, u3 = calcular_vetores_perpendiculares(u1)

        print("Vetor inicial (u1):", u1)
        print("Vetor perpendicular 1 (u2):", u2)
        print("Vetor perpendicular 2 (u3):", u3)

        P = np.array([u1, u2, u3])
        produto = np.dot(P, P.T)
        print("\nMatriz ortogonal P:")
        print(P)
        print("\nP vezes sua transposta:")
        print(produto)
        print("\nP e ortogonal?", np.allclose(produto, np.eye(3), rtol=0, atol=3e-8))

    except ValueError as e:
        print("Erro:", e)
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada cancelada.")

if __name__ == "__main__":
    main()
