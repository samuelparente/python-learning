import numpy as np
import matplotlib.pyplot as plt

def euler_method(func, y0, t0, tf, h):
    n_steps = int((tf - t0) / h)
    t = np.linspace(t0, tf, n_steps+1)
    y = np.zeros(n_steps+1)
    y[0] = y0

    for i in range(1, n_steps+1):
        y[i] = y[i-1] + func(t[i-1], y[i-1]) * h

    return t, y

def heun_method(func, y0, t0, tf, h):
    n_steps = int((tf - t0) / h)
    t = np.linspace(t0, tf, n_steps+1)
    y = np.zeros(n_steps+1)
    y[0] = y0

    for i in range(1, n_steps+1):
        k1 = func(t[i-1], y[i-1])
        k2 = func(t[i], y[i-1] + k1 * h)
        y[i] = y[i-1] + 0.5 * (k1 + k2) * h

    return t, y

def func_example(t, y):
    return -2 * y

# Parâmetros
t0 = 0
tf = 2
h = 0.5
y0 = 1

# Integração usando Euler e Heun
t_euler, y_euler = euler_method(func_example, y0, t0, tf, h)
t_heun, y_heun = heun_method(func_example, y0, t0, tf, h)

# Saída da tabela
print("Metodo de Euler:")
print(" t\t| y")
print("--------------------")
for i in range(len(t_euler)):
    print(f"{t_euler[i]:.2f}\t| {y_euler[i]:.5f}")

print("\nMetodo de Heun:")
print(" t\t| y")
print("--------------------")
for i in range(len(t_heun)):
    print(f"{t_heun[i]:.2f}\t| {y_heun[i]:.5f}")

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(t_euler, y_euler, label='Euler')
plt.plot(t_heun, y_heun, label='Heun')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Integracao Numerica: Euler vs Heun')
plt.legend()
plt.grid(True)
plt.show()
