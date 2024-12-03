import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parámetros del sistema
m = 1  # Masa de los bloques (kg)
k = 10  # Constante del resorte exterior (N/m)
k_c = 5  # Constante del resorte intermedio (N/m)

# Sistema de ecuaciones diferenciales
def resortes_acoplados(t, y):
    x1, v1, x2, v2 = y
    dx1_dt = v1
    dv1_dt = (-k * x1 - k_c * (x1 - x2)) / m
    dx2_dt = v2
    dv2_dt = (-k * x2 - k_c * (x2 - x1)) / m
    return [dx1_dt, dv1_dt, dx2_dt, dv2_dt]

# Condiciones iniciales
x1_0 = 1  # Desplazamiento inicial del bloque 1 (m)
x2_0 = -1  # Desplazamiento inicial del bloque 2 (m)
v1_0 = 0  # Velocidad inicial del bloque 1 (m/s)
v2_0 = 0  # Velocidad inicial del bloque 2 (m/s)

# Solución numérica
sol = solve_ivp(resortes_acoplados, [0, 20], [x1_0, v1_0, x2_0, v2_0], t_eval=np.linspace(0, 20, 1000))

# Graficar los desplazamientos
plt.figure(figsize=(10, 6))

# Desplazamiento del bloque 1
plt.plot(sol.t, sol.y[0], label="Bloque 1 (x1)", color='blue')

# Desplazamiento del bloque 2
plt.plot(sol.t, sol.y[2], label="Bloque 2 (x2)", color='red', linestyle='--')

plt.title("Oscilaciones de los Bloques con Resortes Acoplados")
plt.xlabel("Tiempo (s)")
plt.ylabel("Desplazamiento (m)")
plt.legend()
plt.grid(True)
plt.show()
