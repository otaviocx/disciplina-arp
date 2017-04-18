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

**Os exercícios 3, 4 e 5 referem-se a base de dados "Preços de apartamentos".** 

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

Os cálculos para resolução dessa questão foram realizados em Python no script `apartamentos.py`. O valor do imóvel considerando todas as variáveis é de R$ 1.030.691,91.

___

*6) Explique com suas palavras a importância do uso da regressão no exemplo deste artigo: https://www.linkedin.com/pulse/using-regression-predict-baseball-salaries-nate-reed*

###### Resposta Q6:

O artigo descreve um trabalho realizado para predição de salários de jogadores de *baseball*. Ele começa tentando predizer as vitórias de um time e para isso calcula coeficientes de correlação entre as variáveis que ele tem e as vitórias do time. O modelo construído com regressão apresenta bons resultados com coeficiente de determinação (R^2) de 0.90. O modelo de predição de salários já não tem tanta eficiencia. Mesmo utilizando validação cruzada, obtem uma taxa de 0.68, utilizando 38 variáveis. Os autores então tentam utilzar algumas técnicas de regressão para redução da dimencionalidade do problema (número de variáveis). A importancia da regressão para esse problema se deu justamente nessa redução. Ao final do artigo eles conseguem reduzir para apenas 7 variáveis mantendo uma taxa de 0.64, bem próxima à inicial.
___

*7) Um portal da internet cobra anúncios na página principal de acordo com o número de visualizações diários da página. Um anunciante diz que o mais importante para ele é o número de "clicks" diários no seu anúncio. O portal preparou um estudo com dados dos últimos 30 dias. Foi observado o número de visitas únicas diárias do portal e o número de clicks diários do anúncio. O resultado do ajuste da regressão de Y(número de clicks) por X(número de visualizações) é mostrado no gráfico de dispersão a seguir.*

![Figura 2](https://github.com/otaviocx/disciplina-arp/raw/master/regressao/questao7.PNG "Número de clicks X visualizações diárias.")

*Assinale V ou F justificando sua resposta para as falsas:*

*(a) Apenas 0,66% das visualizações resultam em clicks. Portanto, a regressão não está boa.*

*(b) O número de visualizações é um bom preditor do número de clicks porque o R2 é alto e a reta parece bem ajustada.*

*(c) 0,7044% das visualizações são convertidas em clicks.*

*(d) As duas variáveis não estão linearmente correlacionadas porque o R2 é menor que 1.*

*(e) Se num determinado dia o site tiver 10000 visualizações, o número estimado de clicks é 66.*
 
###### Resposta Q7:

(a) Falso. O fato de apenas aproximadamente 0,66% das visualizações resultarem em clicks não tem nada a ver com a qualidade da regressão. Na verdade a regressão está justamente mostrando essa correlação entre as variáveis. O que não está bom é a taxa de conversão de visualizações em clicks do site. Mas isso, já é um dado de domínio (não impacta na qualidade da regressão).

(b) Verdadeiro. Ter um R2 de 0,70 indica que 70% da variável dependente consegue ser explicado pelo modelo de regressão linear simples. Isso indica que a veriável clicks é fortemente dependente da variável visualizações. Ou seja, a partir das visualizações conseguimos explicar razoavelmente a quantidade de clicks.

(c) Falso. Esse item mistura conceitos da regressão linear com os conceitos de domínio. Como explicado no item anterior, 0,7044 é o coeficiente de determinação. Isso indica o quão bem a variável dependente (clicks) consegue ser explicada pela variável independente (visualizações).

(d) Falso. A correlação linear entre as variáveis é alta, como demonstrado pelo gráfico e pelo coeficiente de determinação. Se o R2 fosse 1, a variável dependente seria deterministica e em função da independente. Com isso, ao invés de previsão, teriamos a certeza do valor. 

(e) Falso. Pela equação da regressão linear dada na figura, a quantidade de clicks para 10 mil visualizações será estimada em 73,3602. Seria 66 se b0 não existisse.
___

*8) Ilustre e explique uma aplicação em que a regressão logística se apresente como mais adequada do que uma regressão linear.*

###### Resposta Q8:

Em aprendizagem supervisionada existem dois tipos de problemas: regressão e classificação. A regressão é um tipo de problema cujo propósito é identificar um padrão para previsão em uma variável dependente cujos valores sejam contínuos ou discretos mas que possuam ordem (variável ordinal). A este tipo de problema a regressão linear é aplicada. Qualquer variável que se deseja predizer e que não dá a ideia de classe e sim de grandeza, pode ser prevista utilizando regressão linear. Por exemplo: tamanho, valor, temperatura, etc. Os problemas que envolvem regressão logística são aqueles cujo propósito é a classificação. Ou seja, a variável dependente é discreta e não possue ordem (variável nominal). Neste tipo de problema a proposta e predizer a classe de um determinado indivíduo. Variáveis como sexo de uma pessoa; se uma pessoa está triste, feliz, ansiosa, etc, prever o sentimento de uma pessoa; predizer a tendencia política (direita, esquerda, centro, etc) de uma determinada pessoa, são exemplos de problema de classificação, nos quais a regressão logística se aplica.

___
