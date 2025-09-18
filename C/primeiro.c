#include <stdio.h>
int main() {
    int contador = 3000000;

    while (contador > 0) {
        printf("%d...\n", contador);
        contador = contador - 1; // Atualiza a variável para evitar loop infinito
    }

    printf("Fogo! 🚀\n");
    return 0;
}