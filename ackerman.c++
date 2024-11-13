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
   
    auto inicio = std::chrono::high_resolution_clock::now();
    int resultado = ackermann(3, 6);  // Ajusta los valores para evitar un exceso de recursión
    auto fin = std::chrono::high_resolution_clock::now();


    std::chrono::duration<double> duracion = fin - inicio;

    std::cout << "Resultado: " << resultado << std::endl;
    std::cout << "Tiempo de ejecución: " << duracion.count() << " segundos" << std::endl;


    return 0;
}