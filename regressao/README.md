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

___

A Figura 1 apresenta os valores reais presentes na amostra (em azul), a regressão construída na Questão 1 (em laranjado), a regressão construída utilizando todos os registros (em cinza) e a regressão construída na Questão 2 (em amarelo). Como é possível observar, a que mais se aproxima da tendencia dos dados é aquela construida na Questão 2.

![Figura 1](https://github.com/otaviocx/disciplina-arp/raw/master/regressao/grafico.png "Regressões construídas para a base de dados 'Risco de ataque cardíaco'")

**Figura 1** Regressões construídas para a base de dados "Risco de ataque cardíaco".

___

*3) Qual o coeficiente de correlação entre cada uma das variáveis com o preço de apartamento? Qual a variável mais importante para explicar o preço de apartamento? Justifique sua resposta.*

###### Resposta Q3:

Os coeficientes de correlação foram calculados utilizando Excel. Os cálculos estão na planilha `apartamentos.xlsx`.

coeficientes | correlação
--- | ---	
(P) x (T)   |	0,603104
(P) x (IP)  |	-0,378349
(P) x (A)   |	0,281342
(P) x (NQ)  |	0,462967
(P) x (VG)  |	0,415587

*preco (P); tamanho (T); idade do predio (IP); andar (A); numero de quartos (NQ); vagas garagem (VG)*

A variável mais importante para explicar o preço de um apartamento é o tamanho. Isso se dá visto que ele é o que possui o maior coeficiente de correlação com o preço. Ou seja, a variável tamanho é a que está mais relacionada com a variável preço.
___

*4) O banco de dados contém informações de 40 apartamentos vendidos no mês passado.  Cada linha do banco de dados é um apartamento.  Ajuste o seguinte modelo de regressão múltipla para os dados:*

*Y=b0+b1x1+b2x2+b3x3+erro, em que:*

*Y=preço do apartamento; X1=tamanho do apartamento, em metros quadrados; X2=idade do prédio, em anos;X3=andar em que o apartamento está.*

*Obs.: Note que não usaremos todas as variáveis independentes.*

*Qual é o preço previsto de um imóvel com 80m2, 10 anos e que está no 9º andar?*

###### Resposta Q4:

Os cálculos para resolução dessa questão foram realizados em Python no script `apartamentos.py`. O valor do imóvel considerando apenas as variáveis acima é de R$ 803.396,11.
___

*5) Ajuste o modelo de regressão múltipla fazendo uso de todas as variáveis. Qual deve ser o preço de um imóvel com 100m2, 3 anos, andar de número 5, 3 quartos e 2 vagas de garagem?*

###### Resposta Q5:

Os cálculos para resolução dessa questão foram realizados em Python no script `apartamentos.py`. O valor do imóvel considerando apenas as variáveis acima é de R$ 1.030.691,91.

___

