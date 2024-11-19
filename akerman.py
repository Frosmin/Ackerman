# import time
# import tracemalloc

# def ackermann(m, n):
#     if m == 0:
#         return n + 1
#     elif m > 0 and n == 0:
#         return ackermann(m - 1, 1)
#     elif m > 0 and n > 0:
#         return ackermann(m - 1, ackermann(m, n - 1))
    
# tracemalloc.start()
# inicio = time.perf_counter()  # Más preciso que time.time()
# resultado = ackermann(0, 10)
# fin = time.perf_counter()

# memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
# tracemalloc.stop()

# print(f"Resultado: {resultado}")
# print(f"Tiempo de ejecución: {fin - inicio:.10f} segundos")
# print(f"Pico de uso de memoria: {memoria_pico / 10**6} MB")

import matplotlib.pyplot as plt
import numpy as np

# Datos para Python (4 valores)
m_values_python = [1, 2, 3, 4]
tiempos_python = [0.00000140, 0.0000050, 0.00018, 0.096]

# Datos para C++ (6 valores)
m_values_cpp = [1, 2, 3, 4, 5]
tiempos_cpp = [0.000001, 0.000001, 0.000001, 0.000001, 1.4]  # Usando valores muy pequeños en lugar de 0

plt.figure(figsize=(10, 6))

# Graficar Python hasta donde hay datos
plt.plot(m_values_python, tiempos_python, label='Python', marker='o', color='blue')
# Graficar C++ completo
plt.plot(m_values_cpp, tiempos_cpp, label='C++', marker='s', color='green')

plt.xlabel('Valor de m')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de Tiempos de Ejecución: Ackermann en Python vs C++')
plt.legend()
plt.grid(True)
plt.yscale('log')  # Escala logarítmica para mejor visualización

plt.savefig('comparacion_tiempos_ackermann.png')
plt.show()