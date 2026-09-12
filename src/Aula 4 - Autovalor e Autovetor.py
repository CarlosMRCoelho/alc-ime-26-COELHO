''' Calculo de Autovalor e Autovetor de uma matriz quadrada A'''

import numpy as np

a = np.array([[-3, 4], [-1, 2]], dtype=float)

''' o autovalor é o valor de lambda que satisfaz a equação det(A - lambda*I) = 0, onde I é a matriz identidade.'''
''' o autovetor é o vetor v que satisfaz a equação Av = lambda*v, onde lambda é o autovalor correspondente.'''

eigvals, eigvecs = np.linalg.eig(a)

print("Autovalores:")
for eigval in eigvals:
    print(f"  {eigval:.2f}")

print("Autovetores:")
for eigvec in eigvecs.T:
    print(f"  {np.round(eigvec, 2)}")

