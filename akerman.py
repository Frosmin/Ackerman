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
# inicio = time.time()
# resultado = ackermann(3, 6)
# fin = time.time()



# memoria_actual, memoria_pico = tracemalloc.get_traced_memory()

# tracemalloc.stop()

# print(f"Resultado: {resultado}")
# print(f"Tiempo de ejecución: {fin - inicio} segundos")
# print(f"Pico de uso de memoria: {memoria_pico / 10**6} MB")

import matplotlib.pyplot as plt
import numpy as np

# Simulando los tiempos de ejecución para diferentes valores de m, n en Python y C++
m_values = [1, 2, 3, 4, 5, 6]
# Estos tiempos están simulados; debes ejecutar el código real para obtener los tiempos exactos
tiempos_python = [0.01, 0.05, 0.25, 1.5, 7.8, 40.0]  # Tiempos de ejecución en Python
tiempos_cpp = [0.005, 0.02, 0.12, 0.7, 3.6, 15.0]    # Tiempos de ejecución en C++ (simulados)

plt.plot(m_values, tiempos_python, label='Python', marker='o', color='blue')
plt.plot(m_values, tiempos_cpp, label='C++', marker='s', color='green')

plt.xlabel('Valor de m')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de Tiempos de Ejecución: Ackermann en Python vs C++')
plt.legend()
plt.grid(True)

# Guardar la gráfica como un archivo PNG
plt.savefig('comparacion_tiempos_ackermann.png')
plt.show()