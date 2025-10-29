print(f"\n-------Prova Prática 5 - Rodrigo Vieira-------")
#    1. Desenvolva uma função que recebe uma mensagem e um número, ela mostra a mensagem e o número e não retorna nada. 
#    A função main chama a função passando os dois argumentos lidos, ou seja, digitados pelo usuário. 

def men_num(mensagem, numero):
    print(f"\n\nSua Mensagem Foi:\n{mensagem}\n\nSeu Número Foi:\n{numero}\n\n--------------------------------")

if __name__ == '__main__':

    print(f" -------Atividade 1 : ------- ")
    msg = str(input("\nDigite Sua Mensagem: "))
    num = float(input("\nDigite Seu Número: "))
    men_num(msg, num)
#    2. Crie uma função para somar três valores. Ela recebe os três valores, calcula a soma e retorna o resultado do cálculo.
#    A função main lê os três valores inteiros, chama a função passando os valores lidos e depois mostra o valor retornado pela função, ou seja, o resultado obtido.

def calc_tres(n_um, n_dois, n_tres):
    soma_valor = n_um + n_dois + n_tres
    return soma_valor

if __name__ == '__main__':

    print(f" ------- Atividade 2 : ------- ")
    numero_um = float(input("\nDigite O Primeiro Número: "))
    numero_dois = float(input("\nDigite O Segundo Número: "))
    numero_tres = float(input("\nDigite O Terceiro Número: "))
    atv_rest2 = calc_tres(numero_um, numero_dois, numero_tres)
    print(f"A soma de: {numero_um} + {numero_dois} + {numero_tres} = {atv_rest2}")
    

#    3. Implemente uma função que calcula a idade de uma pessoa. Ela recebe o ano de nascimento da pessoa, faz o cálculo e retorna à idade.
#    A função principal (main) lê o ano de nascimento digitado pelo usuário, chama a função e mostra o valor retornado pela função calcula.

def calcula_idade(ano_nascimento):
    ano_atual = 2025
    idade = ano_atual - ano_nascimento
    return idade

if __name__ == '__main__':

    print(f" ------- Atividade 3 : ------- ")

    ano_nac = float(input("Digite o Ano do Seu Nascimento: "))
    idade = calcula_idade(ano_nac)

    if idade < 0:
        print(f"Volte depois de existir!")
    elif idade == 0:
        print(f"Esse é seu Primeiro Ano de Vida! Parabens!!!")
    else:   
        print(f"Sua idade é: {idade:.0f} Anos!")

#    4. Elabore o problema (o enunciado) de um problema que usa função e resolva o problema proposto, ou seja, faça a implementação da função def e da função principal (main).

def normal_free(frete, valor_produto):
    normal = valor_produto + frete
    return normal
def premium(valor_produto, taxa):
    premium = (valor_produto) / (1 - ( taxa / 100))
    return premium


if __name__ == '__main__':
    print(f"\n\n ------- Calculadora para E-Commerces -------\n")
    valor_produto = float(input("Digite o Valor do Produto: "))
    valor_taxa = float(input("Digite o Valor da Taxa (0 - 100%): "))
    valor_frete = float(input("Digite o Valor do Frete: "))
    free_plan = normal_free(valor_produto, valor_frete)
    premium_plan = premium(valor_produto, valor_taxa)

    print(f"   ------- Os Valores são: -------   \n")
    print(f"O Valor do Desejado é: {valor_produto:.2f}R$\n      Venda Sem Plano ou Frete é: {valor_produto:.2f}R$\n")
    print(f"O Valor do Desejado é: {valor_produto:.2f}R$\n      Venda Sem Plano com Frete é: {free_plan:.2f}R$\n")
    print(f"O Valor do Desejado é: {valor_produto:.2f}R$\n      Venda Com Plano de {valor_taxa:.0f}% sem Frete de {valor_frete:.2f}R$ é: {premium_plan:.2f}R$\n")
    print(f"O Valor do Desejado é: {valor_produto:.2f}R$\n      Venda Com Plano de {valor_taxa:.0f}% com Frete de {valor_frete:.2f}R$ é: {premium_plan + valor_frete:.2f}R$\n")
