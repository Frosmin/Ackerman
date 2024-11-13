import matplotlib.pyplot as plt

# Datos
n_filas = [10, 100, 1000, 10000, 100000]
tiempo_rust = [0.5, 3, 20, 200, 2000]
tiempo_haskell = [0.8, 5, 35, 380, 4500]

# Crear la figura y el eje
plt.figure(figsize=(10, 6))

# Graficar los datos
plt.plot(n_filas, tiempo_rust, label='Rust', marker='o', linestyle='-', color='b')
plt.plot(n_filas, tiempo_haskell, label='Haskell', marker='o', linestyle='-', color='r')

# Escala logarítmica en el eje y
plt.yscale('log')

# Añadir etiquetas y título
plt.xlabel('Número de filas (n)')
plt.ylabel('Tiempo (ms)')
plt.title('Comparación de tiempos de ejecución entre Rust y Haskell')

# Añadir una leyenda
plt.legend()

# Mostrar la gráfica
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
