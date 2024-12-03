import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parámetros del péndulo
gamma = 0.5  # Coeficiente de fricción
m = 1  # Masa (kg)
l = 1  # Longitud del péndulo (m)
g = 9.8  # Gravedad (m/s^2)

# Ecuación no lineal del péndulo
def pendulo_no_lineal(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -(gamma/m)*omega - (g/l)*np.sin(theta)
    return [dtheta_dt, domega_dt]

# Ecuación linealizada del péndulo
def pendulo_lineal(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -(gamma/m)*omega - (g/l)*theta  # Sin(θ) ≈ θ para pequeños ángulos
    return [dtheta_dt, domega_dt]

# Condiciones iniciales
theta_0 = 0.2  # Ángulo inicial (rad)
omega_0 = 0  # Velocidad angular inicial (rad/s)

# Solución numérica para la ecuación no lineal
sol_no_lineal = solve_ivp(pendulo_no_lineal, [0, 10], [theta_0, omega_0], t_eval=np.linspace(0, 10, 1000))

# Solución numérica para la ecuación lineal
sol_lineal = solve_ivp(pendulo_lineal, [0, 10], [theta_0, omega_0], t_eval=np.linspace(0, 10, 1000))

# Graficar resultados
plt.figure(figsize=(10, 6))

# Solución no lineal
plt.plot(sol_no_lineal.t, sol_no_lineal.y[0], label="Solución No Lineal", color='blue')

# Solución lineal
plt.plot(sol_lineal.t, sol_lineal.y[0], label="Solución Lineal", color='red', linestyle='--')

plt.title("Comparación entre la Solución Lineal y No Lineal del Péndulo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Ángulo (rad)")
plt.legend()
plt.grid(True)
plt.show()

# Solo ejecutar si este archivo es el principal
if __name__ == "__main__":
    ejecutar_pendulo()