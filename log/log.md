for i in range(5):
  for j in range(5):
    print(f'{i +1}{j}', end=' ')
-------------------------------------------------------------------------------------------------------------------------------------------
n=6
for i in range(n):
    for j in range(n):
        if j == i or j == n - 1 - i:
            print("X", end="")
        else:
            print(" ", end="")
    print()   
-------------------------------------------------------------------------------------------------------------------------------------------
    clube_plaulistas = ['Santos', 'São Paulo', 'palmeiras', 'Mirasol', 'Bragantino','Corinthias'],
Clubes_cariocas = ['Fluminece', 'Vasco', 'Botafogo', 'Flamengo']

for time1 in clube_plaulistas:
    for time2 in Clubes_cariocas:
        print(f'{time1} x {time2}')
    print('F')

teste = list(range(1, 11))
teste2 = list(range(15, 20))
teste = teste2
teste.append(-10)
print(teste)
-------------------------------------------------------------------------------------------------------------------------------------------
num = int(input("Digite um numero: "))

cont = 0
while cont >= 0:
  print(cont)
  cont = cont +1
  if cont == num:
    break
list(range(cont - 1))

File "<ipython-input-61-f066208de4f7>", line 2
    for a in range(4:6)
    ^
IndentationError: unexpected indent
-------------------------------------------------------------------------------------------------------------------------------------------
valor_compra = float(input("Digite o custo do Produto: "))
valor_venda = float(input("Digite o valor da venda do Produto: "))
lucro= valor_venda - valor_compra
if lucro < 0:
     print(f"Voce teve um prejuizo de R${lucro}")
elif lucro > 0:
     print(f"Voce teve um lucro de R${lucro}")
elif lucro == 0:
     print(f"Voce nao teve lucro e nem prejuizo")
print(f"Valor do produto:{valor_compra}, Valor da Venda:{valor_venda}, Valor do Lucro:{lucro}")

-------------------------------------------------------------------------------------------------------------------------------------------
ct = 0
while True:
     numero = float(input("Digite um numero inteiro (Digite 0 para sair):"))
     if numero == 0:
          break
     ct = ct + 1
print(f"{ct} numeros digitados.")
-------------------------------------------------------------------------------------------------------------------------------------------
ct = 0
soma = 0
while True:
     numero = float(input("Digite um numero inteiro (Digite 0 para sair):"))
     if numero == 0:
          break
     elif numero > 0:
          soma = soma + numero
     elif numero < 0:
          print("Digite um numero positivo")
     ct = ct + 1
print(f"{ct} Numeros digitados. Soma dos numeros digitados: {soma}")

-------------------------------------------------------------------------------------------------------------------------------------------