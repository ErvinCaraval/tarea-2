import numpy as np
import matplotlib.pyplot as plt

# Constantes
q = 1  # Carga (puede ser cualquier valor, ya que solo importa la forma relativa)
L = 1  # Longitud del triángulo equilátero
C1 = (0, 0)  # Posición de la carga C1
C2 = (1, 0)  # Posición de la carga C2
C3 = (0.5, np.sqrt(3)/2)  # Posición de la carga C3

# Función para calcular el potencial de una carga
def potencial(x, y, a, b, carga):
    return carga * np.log((x - a)**2 + (y - b)**2)

# Función para calcular el potencial total
def potencial_total(x, y):
    p1 = potencial(x, y, *C1, q)
    p2 = potencial(x, y, *C2, q)
    p3 = potencial(x, y, *C3, q)
    return p1 + p2 + p3

# Crear una malla de puntos en el plano
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

# Calcular el potencial total para cada punto de la malla
Z = np.vectorize(potencial_total)(X, Y)

# Graficar las curvas equipotenciales
plt.figure(figsize=(8, 6))
contour = plt.contour(X, Y, Z, 20, cmap='viridis')
plt.colorbar(contour)
plt.title("Curvas Equipotenciales del Sistema de Tres Cargas")
plt.xlabel("x")
plt.ylabel("y")
plt.scatter([C1[0], C2[0], C3[0]], [C1[1], C2[1], C3[1]], color='red', label="Cargas")
plt.legend()
plt.grid(True)
plt.show()
