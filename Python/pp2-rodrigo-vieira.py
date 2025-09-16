                                              # Prova pratica de Logica de Programação - CEUB #                                  
# Aluno: Rodrigo de Seabra Vieira   


                                                                # Questão 1 #
#Elabore o programa que simule a calculadora com as quatro operações aritméticas básicas. O usuário fornecerá dois números e a operação aritmética desejada.
#Mostre o menu com estes símbolos (+ , - , * , / ) para o usuário escolher a operação aritmética. 
#Utilize o comando “se . . . senão . . . ” encadeado, ou seja, “if . . . else . . . ” encadeado.


operador = input("Digie o operador matematico(+ , -  , / , * ): ")
var1 = float(input("Digie o Primeiro numero inteiro: "))
var2 = float(input("Digie o Segundo numero inteiro: "))
resultado = 0
oper = " "
if operador == "+":
   resultado = var1 + var2
   oper = "Soma"
elif operador == "-":
   resultado = var1 - var2
   oper = "subtração"
elif operador == "*":
   resultado = var1 * var2
   oper = "multiplicação"
elif operador == "/":
    resultado = var1 / var2
    oper = "Divisão"
print(f"A resposta da {oper} é: {resultado}")


                                                                # Questão 2 #
#Desenvolva o programa que leia vários valores reais e no final mostre as seguintes informações:
#A quantidade de valores digitados; A soma dos valores digitados; A média aritmética dos valores digitados;
#E a quantidade de valores digitados maior que 20.


quant = 0
soma = 0
while True:
  num = float(input("Digite um numero inteiro( Coloque 0 para parar): "))
  if num == 0:
    break
  quant = quant + 1
  soma = soma + num
print(f"Foram digitados: {quant} numeros; A soma dos numeros é {soma}, e a media total é {soma / quant}")


                                                                # Questão 3 #
# Implemente o programa que leia a nota de vários alunos de uma turma e gere uma tela de saída com as seguintes informações: 
# a quantidade de alunos que fizeram a prova, a quantidade de alunos aprovados, a quantidade de alunos reprovados e a média da turma. 
# Considere que o aluno será aprovado com nota for maior ou igual a cinco. 


quant = 0
soma = 0
aprovado = 0
reprovado = 0
while True:
  num = float(input("Digite as notas dos alunos: (Coloque -1 para parar): "))
  if num == -1:
    break
  quant = quant + 1
  soma = soma + num
  if num >= 5:
    aprovado = aprovado + 1
  if num < 5:
    reprovado = reprovado + 1
print(f"Foram registrados: {quant} notas; Foram aprovado(as) {aprovado} alunos, e reprovados(as) {reprovado} alunos. A media da turma é de {(soma / quant):.3} Pontos.")

                                                                #Brasilia - DF 01/09/2025