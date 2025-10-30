                                              # Prova pratica de Logica de Programação - CEUB #                                  
# Aluno: Rodrigo de Seabra Vieira   
                                                                # Questão 1 #

#Implemente o programa que gere a sequência dos números naturais na ordem crescente até um valor final fornecido (digitado) pelo usuário. 
#Mostre também a quantidade de valores da sequência gerada. 

valor_final = int(input("Digite o valor final: "))

if valor_final < 0:
    print("Erro: O valor deve ser um número natural (0 ou maior).")

else:
    print("Sequência gerada:")

    for numero in range(valor_final + 1):
        print(numero, end=" ")  

    quantidade = valor_final + 1

    print("")
print(f"Quantidade de valores na sequência: {quantidade}")

                                                                # Questão 2 #
#Implemente o programa que gere a sequência dos números naturais na ordem decrescente até o valor zero e o valor inicial será fornecido (digitado) pelo usuário. 
#Mostre também a quantidade de valores da sequência gerada. 

valor_inicial = int(input("Digite o valor inicial (N): "))

if valor_inicial < 0:
    print("Erro: O valor deve ser um número natural (0 ou maior).")
else:
    print("Sequência gerada:")
        
    for numero in range(valor_inicial, -1, -1):
        print(numero, end=" ")     
    print("") 
        
    quantidade = valor_inicial + 1
    print(f"Quantidade de valores na sequência: {quantidade}")

                                                                # Questão 3 #
#Elabore o programa para somar todos os números inteiros que se encontram no intervalo de um a quinhentos.

numero_inicial = 1
numero_final = 500

soma = 0

for numero in range(numero_inicial, numero):
    soma += numero

print(f"A soma de {numero_inicial} a {numero_final} é: {soma}")

                                                                # Questão 4 #
#Elabore o programa para somar todos os números inteiros que são ao mesmo tempo ímpar e múltiplo de três que se encontram no intervalo de um a quinhentos.

soma_total = 0

for numero in range(1, 501):

    impar = (numero % 2 != 0)
    multiplo = (numero % 3 == 0)
    
    if impar and multiplo:
        soma_total += numero 

print(f"A soma de todos os números ímpares e múltiplos de 3 entre 1 e 500 é: {soma_total}")