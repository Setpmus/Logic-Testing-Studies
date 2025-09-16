#include <stdio.h>
/* 
int main() {
    printf("Olá, Mundo!\n");
    return 0;
}
*//* 
int main() {
    int idade = 25;
    float peso = 68.5;
    char tipo_sanguineo = 'A';

    printf("A idade do paciente é: %d anos.\n", idade);
    printf("O peso do paciente é: %f kg.\n", peso);
    printf("O tipo sanguíneo é: %c.\n", tipo_sanguineo);

    return 0;
}
*//*
int main() {
    int numero_favorito;

    printf("Por favor, digite o seu número favorito: ");

    scanf("%d", &numero_favorito);

    printf("Legal! Seu número favorito é %d.\n", numero_favorito);

    return 0;
}
*/
int main() {
    float numero1, numero2, soma;
    printf("--- Calculadora de Soma ---\n");
    printf("Digite o primeiro número: ");

    scanf("%f", &numero1);

    printf("Digite o segundo número: ");

    scanf("%f", &numero2);

    soma = numero1 + numero2;

    printf("O resultado da soma de %f e %f é: %f\n", numero1, numero2, soma);

    return 0;
}