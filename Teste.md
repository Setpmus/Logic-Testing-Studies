### **CARACTERES QUE QUASE NÃO ENCONTRO EM MEU TECLADO**
| backslash  |  vertical bar |
| :-------:  | :-----------: |
|     \      |     **|**     |
---


### **Conectivos Lógicos**


|     Nome Comum     |     Nome Formal     |  Símbolo(s) |  Exemplo de Leitura   |             Regra Principal (Quando é Verdadeiro?)                  |
| :----------------: | :-----------------: | :---------: | :-------------------: | :-----------------------------------------------------------------: |
| **NÃO**            | Negação             |   `¬`, `~`  | "Não P"               | Inverte o valor de verdade de P.                                    | 
| **E**              | Conjunção           |     `∧`     | "P e Q"               | Somente quando **ambos** P e Q são verdadeiros.                     | 
| **OU**             | Disjunção Inclusiva |     `∨`     | "P ou Q"              | Quando **pelo menos um** (P ou Q) é verdadeiro.                     |
| **OU...OU..**      | Disjunção Exclusiva |  `⊕`, `⊻`  | "Ou P ou Q"           | Quando **apenas um** (P ou Q) é verdadeiro, mas não ambos.          | 
| **SE... ENTÃO...** | Condicional         |     `→`     | "Se P, então Q"       | Sempre, **exceto** quando P é verdadeiro e Q é falso (V → F).       |
| **SE E SOMENTE SE**| Bicondicional       |     `↔`     | "P se e somente se Q" | Quando P e Q têm o **mesmo valor de verdade** (ambos V ou ambos F). | 
---


### **Quantificadores Lógicos**


|              Nome             | Símbolo |          Significado            |       Exemplo de Leitura         |
| :----------------------------:|:--------|:--------------------------------|:---------------------------------|                
| **Quantificador Universal**   |   `∀`   | Para todos / Qualquer que seja. | `∀x...` (Para todo x...)         |
| **Quantificador Existencial** |   `∃`   | Existe / Há pelo menos um.      | `∃x...` (Existe um x tal que...) |
---

### **1. Aritmética Básica e Símbolos de Comparação**

| Símbolo | Nome Comum / Leitura        | Significado e Exemplo de Uso                                  |
| :-----: | :-------------------------: | :----------------------------------------------------------: |
| `+`     | Mais / Adição               | Soma dois valores. Ex: `3 + 7 = 10`                          |
| `-`     | Menos / Subtração           | Subtrai um valor de outro. Ex: `10 - 4 = 6`                  |
| `×` ou `*` | Vezes / Multiplicação     | Multiplica dois valores. Ex: `5 * 2 = 10`                    |
| `÷` ou `/` | Dividido / Divisão        | Divide um valor por outro. Ex: `10 / 2 = 5`                  |
| `=`     | Igual a                     | Indica que dois valores são idênticos. Ex: `x = y`           |
| `≠`     | Diferente de                | Indica que dois valores não são idênticos. Ex: `x ≠ y`        |
| `<`     | Menor que                   | O valor à esquerda é menor que o da direita. Ex: `x < y`     |
| `>`     | Maior que                   | O valor à esquerda é maior que o da direita. Ex: `x > y`     |
| `≤`     | Menor ou igual a            | O valor à esquerda é menor ou igual ao da direita. Ex: `x ≤ y`|
| `≥`     | Maior ou igual a            | O valor à esquerda é maior ou igual ao da direita. Ex: `x ≥ y`|
| `±`     | Mais ou menos               | Indica duas possibilidades (soma e subtração). Ex: `√4 = ±2`  |
| `|x|`   | Módulo / Valor Absoluto de x| Distância do número até o zero. Ex: `|-5| = 5`               |

---


### **2. Lógica Proposicional e Quantificadores**

| Símbolo | Nome Comum        | Nome Formal          | Exemplo de Leitura                            |
| :-----: | :---------------: | :------------------: | :-------------------------------------------: |
| `¬` `~` | **NÃO**           | Negação              | "Não P"                                      |
| `∧` `&` | **E**             | Conjunção            | "P e Q"                                      |
| `∨`     | **OU**            | Disjunção Inclusiva  | "P ou Q"                                     |
| `⊕` `⊻` | **OU...OU...**    | Disjunção Exclusiva  | "Ou P ou Q"                                  |
| `→` `⇒` | **SE...ENTÃO...** | Condicional          | "Se P, então Q"                              |
| `↔` `⇔` | **SE E SOMENTE SE** | Bicondicional      | "P se e somente se Q"                        |
| `∀`     | **Para todo...**  | Quantificador Universal | "Para todo x..."                           |
| `∃`     | **Existe...**     | Quantificador Existencial | "Existe um x tal que..."                  |
| `∴`     | **Portanto...**   | Conclusão            | Conclui um argumento lógico. Ex: `P → Q, P ∴ Q`|

---


### **3. Teoria dos Conjuntos**

| Símbolo   | Nome Comum / Leitura                 | Significado e Exemplo de Uso                                   |
| :-------: | :----------------------------------: | :-----------------------------------------------------------: |
| `{ }`     | Conjunto                             | Define um conjunto. Ex: `A = {1, 2, 3}`                       |
| `∈`       | Pertence a                           | Um elemento está em um conjunto. Ex: `3 ∈ A`                  |
| `∉`       | Não pertence a                       | Um elemento não está em um conjunto. Ex: `4 notin A`           |
| `⊆`       | Está contido ou é igual a (subconjunto)| Um conjunto está dentro de outro (ou é igual). Ex: `{1, 2} ⊆ A`|
| `⊂`       | Está contido em (subconjunto próprio)| Um conjunto está dentro de outro, mas não é igual. Ex: `{1, 2} ⊂ A`|
| `⊇`       | Contém ou é igual a (superconjunto)  | Um conjunto contém outro (ou é igual). Ex: `A ⊇ {1, 2}`       |
| `⊃`       | Contém (superconjunto próprio)       | Um conjunto contém outro, mas não é igual. Ex: `A ⊃ {1, 2}`   |
| `∪`       | União                                | Todos os elementos de ambos os conjuntos. Ex: `{1,2} ∪ {2,3} = {1,2,3}` |
| `∩`       | Interseção                           | Apenas os elementos que estão em ambos os conjuntos. Ex: `{1,2} ∩ {2,3} = {2}` |
| `\` ou `-` | Diferença                            | Elementos do primeiro conjunto que não estão no segundo. Ex: `{1,2} \ {2,3} = {1}` |
| `∅` `{}`   | Conjunto Vazio                       | Um conjunto sem nenhum elemento.                              |
| `P(A)`    | Conjunto das partes de A             | O conjunto de todos os subconjuntos de A.                     |
| `|A|` `#(A)`| Cardinalidade de A                   | O número de elementos no conjunto A. Ex: `|{1, 2, 3}| = 3`   |

---


### **4. Cálculo e Análise**

| Símbolo  | Nome Comum / Leitura         | Significado e Exemplo de Uso                                      |
| :------: | :--------------------------: | :---------------------------------------------------------------:|
| `f(x)`   | Função de x                  | Uma expressão envolvendo a variável x. Ex: `f(x) = x²`            |
| `lim`    | Limite                       | O valor que uma função se aproxima. Ex: `lim(x→c) f(x)`           |
| `d/dx`   | Derivada                     | A taxa de variação instantânea. Ex: `d/dx (x²) = 2x`              |
| `∫`      | Integral                      | A área sob a curva de uma função. Ex: `∫ 2x dx = x² + C`          |
| `∑`      | Somatório                     | Soma uma sequência de termos. Ex: `∑(i=1 até n) i = 1 + 2 + ... + n`|
| `∏`      | Produtório                    | Multiplica uma sequência de termos. Ex: `∏(i=1 até n) i = 1 * 2 * ... * n`|
| `∞`      | Infinito                      | Um conceito de algo sem limite ou fim.                           |
| `∂`      | Derivada Parcial (del)        | Derivada de uma função com múltiplas variáveis.                  |
| `∇`      | Gradiente (nabla)             | Vetor das derivadas parciais de uma função.                      |

---


### **5. Álgebra Linear e Geometria**

| Símbolo  | Nome Comum / Leitura         | Significado e Exemplo de Uso                                 |
| :------: | :--------------------------: | :----------------------------------------------------------:|
| `||v||`  | Norma / Módulo de um vetor   | Comprimento de um vetor.                                    |
| `·`      | Produto Escalar              | Operação entre dois vetores que resulta em um escalar.      |
| `×`      | Produto Vetorial             | Operação entre dois vetores que resulta em outro vetor.     |
| `Aᵀ`     | Matriz Transposta            | Inverte as linhas e colunas de uma matriz.                  |
| `||`     | Paralelo a                   | Duas retas que nunca se cruzam. Ex: `r || s`                |
| `⊥`      | Perpendicular a              | Duas retas que se cruzam formando um ângulo de 90°. Ex: `r ⊥ s`|
| `∠`      | Ângulo                       | Símbolo para denotar um ângulo. Ex: `∠ABC`                  |
| `△`      | Triângulo                    | Símbolo para denotar um triângulo. Ex: `△ABC`               |
| `π`      | Pi                           | Constante matemática (aprox. 3.14159...).                   |

---


### **6. Alfabeto Grego (Letras Comuns)**

| Maiúscula | Minúscula |  Nome   |
| :-------: | :-------: | :-----: |
| `Α`       | `α`       | Alfa    |
| `Β`       | `β`       | Beta    |
| `Γ`       | `γ`       | Gama    |
| `Δ`       | `δ`       | Delta   |
| `Ε`       | `ε`       | Épsilon |
| `Ζ`       | `ζ`       | Zeta    |
| `Η`       | `η`       | Eta     |
| `Θ`       | `θ`       | Teta    |
| `Λ`       | `λ`       | Lambda  |
| `Μ`       | `μ`       | Mu (Mi) |
| `Π`       | `π`       | Pi      |
| `Ρ`       | `ρ`       | Rô      |
| `Σ`       | `σ` `ς`   | Sigma   |
| `Φ`       | `φ`       | Phi     |
| `Ψ`       | `ψ`       | Psi     |
| `Ω`       | `ω`       | Ômega   |