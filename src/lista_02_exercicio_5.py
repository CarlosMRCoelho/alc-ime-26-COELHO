''' ford_ex_6_38 e ford_ex_6_39 - Matriz Ortogonal  '''

import numpy as np
from numpy import linalg as la

# matrizes do exercicio 6.38

P1 = np.array([
    [-0.40825, 0.43644, 0.80178],
    [-0.8165, 0.21822, -0.53452],
    [-0.40825, -0.87287, 0.26726],
])
P2 = np.array([
    [-0.51450, 0.48507, 0.70711],
    [-0.68599, -0.72761, 0.00000],
    [0.51450, -0.48507, 0.70711],
])

# matrizes do exercicio 6.39

P3 = np.array([
    [0.58835, 0.70206, 0.40119],
    [-0.78446, -0.37524, -0.49377],
    [-0.19612, -0.60523, 0.77152],
])
P4 = np.array([
    [-0.47624, -0.4264, 0.30151],
    [0.087932, 0.86603, -0.40825],
    [-0.87491, -0.26112, 0.86164],
])

def is_orthogona_by_definition(P): 
    """Verifica se a matriz é ortogonal verificando se sua transposta é igual à sua inversa."""
    # Uma matriz é ortogonal se P^T = P^-1, ou seja, a transposta da matriz é igual à sua inversa.

    return np.allclose(P.T, la.inv(P), atol=1e-3, rtol=1e-3)

def is_orthogonal_by_vectors(P):
    """Verifica se a matriz é ortogonal verificando se seus vetores coluna são ortonormais."""
    # Uma matriz é ortogonal quando P^T @ P = I. Isso garante que:
    # - cada coluna tem norma 1;
    # - colunas distintas são ortogonais entre si.

    return np.allclose(P.T @ P, np.eye(3), atol=1e-3, rtol=1e-3)

def main():
    matrices = [P1, P2, P3, P4]
    for i in range(len(matrices)):
        P = matrices[i]
        print(f"Matriz P{i + 1}:")
        print("="*10)
        print(P)
        print()
        print("Ortogonal por definição:", is_orthogona_by_definition(P))
        print("Ortogonal por vetores:", is_orthogonal_by_vectors(P))
        print()

if __name__ == "__main__":
    main()