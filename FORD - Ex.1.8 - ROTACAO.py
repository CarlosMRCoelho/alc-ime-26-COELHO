''' calculo de rotação de um ponto em torno de outro ponto '''
''' FORD Exemplo 1.8'''

import numpy as np
import math
import matplotlib.pyplot as plt

T1 = np.array([[1, 0, -2], [0, 1, -11], [0, 0, 1]])  # Translação para a origem

angulo = np.radians(30)  # Ângulo de rotação em radianos

R = np.array([[math.cos(angulo), -math.sin(angulo), 0],
               [math.sin(angulo), math.cos(angulo), 0], 
               [0, 0, 1]])  # Matriz de rotação


T2 = np.array([[1, 0, 2], [0, 1, 11], [0, 0, 1]])   # Translação para o ponto de rotação

F = T2 @ R @ T1  # Matriz de transformação final

print (F)

centro = np.array([2, 11, 1])
ponto = np.array([5, 11, 1])
ponto_rotacionado = F @ ponto

plt.plot(*centro[:2], "ko", label="Centro (2, 11)")
plt.plot([centro[0], ponto[0]], [centro[1], ponto[1]], "b-o", label="Antes")
plt.plot([centro[0], ponto_rotacionado[0]],
         [centro[1], ponto_rotacionado[1]], "r-o", label="Depois (30°)")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.title("Rotação de 30° em torno do ponto (2, 11)")
plt.show()
