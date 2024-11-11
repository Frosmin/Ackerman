int ackermann(int m, int n) {
    if (m == 0) {
        return n + 1;
    } else if (m > 0 && n == 0) {
        return ackermann(m - 1, 1);
    } else if (m > 0 && n > 0) {
        return ackermann(m - 1, ackermann(m, n - 1));
    }
    return 0; // Esta línea nunca se alcanzará, pero es necesaria para evitar advertencias del compilador.
}

int main() {
    // Aumentar el límite de recursión (esto depende del compilador y del sistema operativo)
    // En muchos sistemas, esto no es posible cambiarlo directamente desde el código C++.
    // Sin embargo, puedes ajustar el límite de pila en tu entorno de desarrollo si es necesario.

    // Medir el tiempo de ejecución
    auto inicio = std::chrono::high_resolution_clock::now();
    int resultado = ackermann(3, 6);  // Ajusta los valores para evitar un exceso de recursión
    auto fin = std::chrono::high_resolution_clock::now();

    // Calcular el tiempo de ejecución
    std::chrono::duration<double> duracion = fin - inicio;

    std::cout << "Resultado: " << resultado << std::endl;
    std::cout << "Tiempo de ejecución: " << duracion.count() << " segundos" << std::endl;

    // Nota: El seguimiento de memoria como tracemalloc en Python no tiene un equivalente directo en C++ estándar.
    // Para un seguimiento de memoria más avanzado, puedes usar herramientas externas como Valgrind o el depurador de Visual Studio.

    return 0;
}