\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
### **Planilha de Conectivos Lógicos**

| Nome Comum | Nome Formal | Símbolo(s) | Exemplo de Leitura | Regra Principal (Quando é Verdadeiro?) | Tabela-Verdade (P, Q) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **NÃO** | Negação | `¬`, `~` | "Não P" | Inverte o valor de verdade de P. | **P: V** → **¬P: F** <br> **P: F** → **¬P: V** |
| **E** | Conjunção | `∧` | "P e Q" | Somente quando **ambos** P e Q são verdadeiros. | V,V → **V** <br> V,F → **F** <br> F,V → **F** <br> F,F → **F** |
| **OU** | Disjunção Inclusiva | `∨` | "P ou Q" | Quando **pelo menos um** (P ou Q) é verdadeiro. | V,V → **V** <br> V,F → **V** <br> F,V → **V** <br> F,F → **F** |
| **OU... OU...** | Disjunção Exclusiva | `⊕`, `⊻` | "Ou P ou Q" | Quando **apenas um** (P ou Q) é verdadeiro, mas não ambos. | V,V → **F** <br> V,F → **V** <br> F,V → **V** <br> F,F → **F** |
| **SE... ENTÃO...** | Condicional | `→` | "Se P, então Q" | Sempre, **exceto** quando P é verdadeiro e Q é falso (V → F). | V,V → **V** <br> V,F → **F** <br> F,V → **V** <br> F,F → **V** |
| **SE E SOMENTE SE**| Bicondicional | `↔` | "P se e somente se Q" | Quando P e Q têm o **mesmo valor de verdade** (ambos V ou ambos F). | V,V → **V** <br> V,F → **F** <br> F,V → **F** <br> F,F → **V** |
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
---

### **Planilha de Quantificadores Lógicos**

|              Nome             | Símbolo |          Significado            |       Exemplo de Leitura         |
| :----------------------------:|:--------|:--------------------------------|:---------------------------------|                
| **Quantificador Universal**   |   `∀`   | Para todos / Qualquer que seja. | `∀x...` (Para todo x...)         |
| **Quantificador Existencial** |   `∃`   | Existe / Há pelo menos um.      | `∃x...` (Existe um x tal que...) |