# Exercícios sobre Regressão

**Os exercícios abaixo referem-se a base de dados "Risco de ataque cardíaco"**

*1) Obtenha o modelo utilizando os 10 primeiros exemplos da base de dados. Calcule e apresente o erro quadrático médio aplicando o modelo de regressão nos mesmos 10 primeiros exemplos da base de dados. Depois calcule e apresente o erro quadrático médio do modelo de regressão obtido nos demais exemplos. Argumente se o modelo tem ou não uma boa capacidade de predição em novos exemplos.*

###### Resposta Q1:

Considerando o modelo criado apenas pelos 10 primeiros registros, temos os seguintes Erros Quadráticos Médios (EQM):

* EQM dos 10 primeiros registros: `0,000484240`
* EQM dos 10 últimos registros:   `0,341360000`
* EQM de todos os registros:      `0,341844045`

Como é possível observar, o EQM para os 10 primeiros registros é bem menor que para os 10 últimos. Isso se dá porque a variável dependente (Prob. Ataque Cardíaco) muda a tendência com a idade maior que 40 anos. Como o modelo so considerou indivíduos com idades menores, não reflete o comportamento de toda a massa de dados.

___

*2) Agora obtenha o modelo utilizando os 5 primeiros exemplos da base de dados e também os 5 últimos. Calcule e apresente o erro quadrático médio aplicando o modelo de regressão nos 10 exemplos utilizados para obter o modelo de regressão. Depois calcule e apresente o erro quadrático médio do modelo de regressão obtido nos demais exemplos. Argumente se o modelo tem ou não uma boa capacidade de predição em novos exemplos. Compare com os resultados do exercício anterior e argumente as possíveis diferenças de resultados.*

###### Resposta Q2:

Considerando o modelo criado apenas pelos 5 primeiros e 5 últimos registros, temos os seguintes Erros Quadráticos Médios (EQM):

* EQM dos registros utilizados no modelo:     `0,030596014`
* EQM dos registros não utilizados no modelo: `0,059786116`
* EQM de todos os registros:                  `0,090382129`

Como é possível observar, o EQM dos registros não utilizados no modelo permaneceu próximo ao EQM dos registros utilizados no modelo. Isso se deu visto que, ao construir o modelo com os 5 primeiros e 5 últimos registro, as diferentes tendências apresentadas para diferentes faixas etárias foram capturadas. Com isso, a regressão resultante cobre melhor também aqueles registros que não foram utilizados para a construção do modelo. O erro quadrático médio utilizando apenas os 5 primeiros e 5 últimos registros acaba sendo menor, inclusive, que quando utilizado todos os 20 registros da amostra para construção do modelo. 

A Figura 1 apresenta os valores reais presentes na amostra (em azul), a regressão construída na Questão 1 (em laranjado), a regressão construída utilizando todos os registros (em cinza) e a regressão construída na Questão 2 (em amarelo). Como é possível observar, a que mais se aproxima da tendencia dos dados é aquela construida na Questão 2.

___

![Figura 1](https://github.com/otaviocx/disciplina-arp/raw/master/regressao/grafico.png "Regressões construídas para a base de dados 'Risco de ataque cardíaco'")

**Figura 1** Regressões construídas para a base de dados "Risco de ataque cardíaco".


