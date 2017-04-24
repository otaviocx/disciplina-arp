# Resolução da Prova de 2016 - 01

#### Questão 02 - Sobre o algoritmo KNN, qual o melhor valor de K? Justifique sua resposta.

###### Resposta

Um valor de K muito pequeno é sensível a ruídos (outliers das classes) e um valor de K muito grande poderá gerar uma interpretação incorreta das fronteiras de cada classe. O valor de K é a quantidade de vizinhos próximos (com as menores distâncias) da instancia que está para ser classificada. Logo, K não deve ser múltiplo da quantidade de classes existentes, para evitar que dê empate (a mesma quantidade de vizinhos para cada classe). Como já sabemos a classe de uma quantidade de instâncias (base de treinamento), o melhor valor de K será aquele que maximiza a acurácia de classificação para essas instâncias (pode-se pegar uma parte da base que já sabemos a classe para teste de acurácia). Com isso, é importante que a base de treinamento seja variada (tendo uma quantidade próxima de amostras para cada classe) e que a porção tomada para teste também seja.

___

#### Questão 03 - Na análise discriminante quadrática, as distribuições das classes são modeladas como distribuições normais multivariadas. Assume-se que as observações do vetor de atributos pertencentes à j-ésima classe estejam distribuídas de acordo com uma função densidade de probabilidade conjunta expressa pela Equação abaixo. 
**Parte 1) Mostre como obter a função discriminante quadrática e linear a partir da equação apresentada.** 

###### Resposta

**Parte 2) Discuta qual é a diferença fundamental no equacionamento das duas abordagens (quadrática e linear) e como as fronteiras geradas por ambas pode afetar a capacidade de generalização de novos objetos a serem classificados, particularmente, em objetos que porventura possam estar contaminados com ruídos de medidas instrumentais.**

###### Resposta

___

#### Questão 05 - Uma agência de seguro de automóveis deseja otimizar o atendimento de seus clientes encaminhando-os a departamentos específicos. Caso o motivo da visita a agência seja sinistro o cliente é encaminhado ao gichê 1 e caso seja roubo o cliente é encaminhado ao gichê 2. O administrador da agência identificou 3 informações que são relevantes ao para a tomada de decisão: Cor do carro (C), tipo do carro (T) e origem (O). A Tabela 1 apresenta o conhecimento prévio sobre os atendimentos da agência. Usando um classificador Bayesiano simples, a qual gichê o cliente que possui um SUV importado vermelho deve ser encaminhado?


**Tabela 1.** Dados da agência de seguros.

Amostra|	Cor|	Tipo|	Origem|	Gichê
--- | --- | --- | --- | ---
1|	Vermelho|	SUV|	Nacional|	2
2|	Amarelo|	Esportivo|	Importado|	1
3|	Vermelho|	Esportivo|	Nacional|	2
4|	Amarelo|	Esportivo|	Nacional|	1
5|	Amarelo|	Esportivo|	Importado|	2
6|	Amarelo|	SUV|	Importado|	1
7|	Amarelo|	SUV|	Importado|	2
8|	Amarelo|	SUV|	Nacional|	1
9|	Vermelho|	SUV|	Importado|	1
10|	Vermelho|	Esportivo|	Importado|	2

###### Resposta

**Teorema de Bayes:** 
<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/2185befea9e8d19e68f714add3e7da67.svg?invert_in_darkmode" align=middle width=238.5867pt height=16.438356pt/></p>

onde:
* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode" align=middle width=9.395100000000005pt height=14.155350000000013pt/> é um vetor de entradas
* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/97a044cc5f5f3b616c0c9d5376399bc2.svg?invert_in_darkmode" align=middle width=59.420295pt height=24.65759999999998pt/> é a probabilidade de <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/1a567506286617473a9c0d9b2172f951.svg?invert_in_darkmode" align=middle width=19.014930000000007pt height=22.46574pt/> dado <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode" align=middle width=9.395100000000005pt height=14.155350000000013pt/>
* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/9f5b0ad969d1768472dd8c7dcaccb7e3.svg?invert_in_darkmode" align=middle width=45.458985000000006pt height=24.65759999999998pt/> é a probabilidade geral de <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/1a567506286617473a9c0d9b2172f951.svg?invert_in_darkmode" align=middle width=19.014930000000007pt height=22.46574pt/>
* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/3f93f88d371a8788c9fbbf93e5e554c0.svg?invert_in_darkmode" align=middle width=59.420295pt height=24.65759999999998pt/> é a probabilidade de <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode" align=middle width=9.395100000000005pt height=14.155350000000013pt/> dado <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/1a567506286617473a9c0d9b2172f951.svg?invert_in_darkmode" align=middle width=19.014930000000007pt height=22.46574pt/>

**Classificador Naive Bayes:**
<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/f78976251edc40c2de5fd8f9aef0d249.svg?invert_in_darkmode" align=middle width=233.46675pt height=44.897324999999995pt/></p>

onde:

* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/15f93b25ba881e5829e8fc647b680fb2.svg?invert_in_darkmode" align=middle width=12.439185000000005pt height=24.716340000000006pt/> é a classe estimada para a entrada informada
* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/a7bac395296d899b2971eaa1e4f76bf5.svg?invert_in_darkmode" align=middle width=100.70841pt height=26.438939999999977pt/> é o produtório das probabilidades de cada característica de entrada <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/9fc20fb1d3825674c6a279cb0d5ca636.svg?invert_in_darkmode" align=middle width=14.045955000000003pt height=14.155350000000013pt/> dado a classe <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/1a567506286617473a9c0d9b2172f951.svg?invert_in_darkmode" align=middle width=19.014930000000007pt height=22.46574pt/>
* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode" align=middle width=5.663295000000005pt height=21.683310000000006pt/> itera sobre as caracteristicas da entrada (vetor de entrada) e <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/63bb9849783d01d91403bc9a5fea12a2.svg?invert_in_darkmode" align=middle width=9.075495000000004pt height=22.831379999999992pt/> itera sobre as classes possíveis.
* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/c329b295e6d71511af4f29af596de771.svg?invert_in_darkmode" align=middle width=57.50976000000001pt height=14.155350000000013pt/> retorna o índice em que o maior valor está (argumento/índice do maior valor).


No problema proposto temos 3 características que compõem o vetor de entradas <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode" align=middle width=9.395100000000005pt height=14.155350000000013pt/> : Cor, Tipo e Origem. 

* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/277fbbae7d4bc65b6aa601ea481bebcc.svg?invert_in_darkmode" align=middle width=15.947580000000002pt height=14.155350000000013pt/> => Cor
* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/95d239357c7dfa2e8d1fd21ff6ed5c7b.svg?invert_in_darkmode" align=middle width=15.947580000000002pt height=14.155350000000013pt/> => Tipo
* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/2c52641cc5fa73cbbdf887c89d82f0de.svg?invert_in_darkmode" align=middle width=15.947580000000002pt height=14.155350000000013pt/> => Origem

Logo, o carro que queremos classificar pode ser representado pelo vetor <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/a90985acf5f416f5ec8b72e494025fd7.svg?invert_in_darkmode" align=middle width=233.79955499999997pt height=24.65759999999998pt/>.

O que desejamos saber ( <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/deceeaf6940a8c7a5a02373728002b0f.svg?invert_in_darkmode" align=middle width=8.649300000000004pt height=14.155350000000013pt/> ) é o Gichê, que possui 2 valores possíveis: <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/034d0a6be0424bffe9a6e7ac9236c0f5.svg?invert_in_darkmode" align=middle width=8.219277000000005pt height=21.18732pt/> ou <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/76c5792347bb90ef71cfbace628572cf.svg?invert_in_darkmode" align=middle width=8.219277000000005pt height=21.18732pt/>. Na amostra temos 10 carros, sendo 5 em cada uma das duas classes. Ou seja, exatamente a metade. Logo, a probabilidade de ser um dos dois Guichês (<img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/c0efab457afdcefe72d17c70dd4f1add.svg?invert_in_darkmode" align=middle width=40.89294pt height=24.65759999999998pt/>) é de <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/d5d5564ce0bb9999695f32da6ba7af42.svg?invert_in_darkmode" align=middle width=24.657765pt height=24.65759999999998pt/>.

* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/5d8ebc228cd30a3deea9e8b8d041fea1.svg?invert_in_darkmode" align=middle width=87.46815pt height=24.65759999999998pt/> para <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/417e9d7f078cdb8c16592aee5f8c7687.svg?invert_in_darkmode" align=middle width=39.212250000000004pt height=22.831379999999992pt/> ou <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/e7b5cd16938b689c6c74758b19ed6c18.svg?invert_in_darkmode" align=middle width=39.212250000000004pt height=22.831379999999992pt/>

A parte do produtório teremos que resolver para cada classe. Iniciaremos com a classe 1 (Guichê 1): <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/3e1f7f88de01510641cd377538cfab30.svg?invert_in_darkmode" align=middle width=462.829455pt height=24.65759999999998pt/>

* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/2b4668a21bc9f31dda93a1a7d75a03ff.svg?invert_in_darkmode" align=middle width=198.847605pt height=24.65759999999998pt/> => 1 dos 5 carros em <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/d81a84099e7856ffa4484e1572ceadff.svg?invert_in_darkmode" align=middle width=18.301470000000002pt height=22.46574pt/> é vermelho.
* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/0e45475c4fb2af9c9d538210d5883edb.svg?invert_in_darkmode" align=middle width=167.293005pt height=24.65759999999998pt/> => 3 dos 5 carros em <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/d81a84099e7856ffa4484e1572ceadff.svg?invert_in_darkmode" align=middle width=18.301470000000002pt height=22.46574pt/> são SUVs.
* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/6668c780078e0f3df0cef74841d8e4fd.svg?invert_in_darkmode" align=middle width=205.36510499999997pt height=24.65759999999998pt/> => 3 dos 5 carros em <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/d81a84099e7856ffa4484e1572ceadff.svg?invert_in_darkmode" align=middle width=18.301470000000002pt height=22.46574pt/> são importados.

temos: 
<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/ffaa3fec6cea507b25bd73468e8601ab.svg?invert_in_darkmode" align=middle width=86.75452499999999pt height=16.438356pt/></p>
<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/c102edd1503646041b634bf01936d9d5.svg?invert_in_darkmode" align=middle width=273.60134999999997pt height=44.897324999999995pt/></p>

logo:
<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/06fa36322303997ec0ce6df503572b97.svg?invert_in_darkmode" align=middle width=292.77599999999995pt height=44.897324999999995pt/></p>

Para a classe 2 (Guichê 2): <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/6a9c20686e3305cd5bc7f6d93da84264.svg?invert_in_darkmode" align=middle width=462.829455pt height=24.65759999999998pt/>

* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/cb3e20da08c5b0f55a051980c6b6ff31.svg?invert_in_darkmode" align=middle width=198.847605pt height=24.65759999999998pt/> => 3 dos 5 carros em <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/85f3e1190907b9a8e94ce25bec4ec435.svg?invert_in_darkmode" align=middle width=18.301470000000002pt height=22.46574pt/> são vermelhos.
* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/52edc6018bf70703fecced6d8a6e6c64.svg?invert_in_darkmode" align=middle width=167.293005pt height=24.65759999999998pt/> => 2 dos 5 carros em <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/85f3e1190907b9a8e94ce25bec4ec435.svg?invert_in_darkmode" align=middle width=18.301470000000002pt height=22.46574pt/> são SUVs.
* <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/c8cae5eb175cc6f354fbdceb9e7a53ee.svg?invert_in_darkmode" align=middle width=205.36510499999997pt height=24.65759999999998pt/> => 3 dos 5 carros em <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/85f3e1190907b9a8e94ce25bec4ec435.svg?invert_in_darkmode" align=middle width=18.301470000000002pt height=22.46574pt/> são importados.

temos: 
<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/fdc67f45159983ad75515bc7f3ef3fe5.svg?invert_in_darkmode" align=middle width=86.75452499999999pt height=16.438356pt/></p>
<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/d5a093cbfb84008d7ebd1316a0806bbe.svg?invert_in_darkmode" align=middle width=281.82165pt height=44.897324999999995pt/></p>

logo:
<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/1463afaa337b8ef18034185e5cc35a8d.svg?invert_in_darkmode" align=middle width=309.21495pt height=44.897324999999995pt/></p>

Aplicando o <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/c329b295e6d71511af4f29af596de771.svg?invert_in_darkmode" align=middle width=57.50976000000001pt height=14.155350000000013pt/> no vetor resultante <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/ae56be595863e5564ccabb7ddfa9ce84.svg?invert_in_darkmode" align=middle width=106.84970999999997pt height=24.65759999999998pt/> temos que a probabilidade maior é para classe 2. Com isso, o SUV vermelho importado seria classificado para ir ao Guichê 2.
___

#### Questão 6 - O conjunto de dados apresentado pelo gráfico da Figura 4 é formado por 3 amostras da classe <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/4b4518f1b7f0fb1347fa21506ebafb19.svg?invert_in_darkmode" align=middle width=18.321105000000006pt height=14.155350000000013pt/> e 3 amostras da classe <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/f7eb0e840408d84a0c156d6efb611f3e.svg?invert_in_darkmode" align=middle width=18.321105000000006pt height=14.155350000000013pt/> constituindo um problema linearmente separável no qual pode-se aplicar o classificador SVM. Responda as questões a seguir:

<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/b4db165ce097817154baab0b8c5a2a08.svg?invert_in_darkmode" align=middle width=527.2244999999999pt height=18.75984pt/></p>

![Figura 4](https://github.com/otaviocx/disciplina-arp/raw/master/estudos/questao6.png "Dados de treinamento da questão 6.")

**Figura 4** Dados de treinamento da questão 6.

1. **Considerando as amostras apresentadas no gráfico, escreva o sistema linear cuja solução retorna os multiplicadores de Lagrange para o hiperplano que separa as duas classes.**

###### Resposta

Observando as amostras no gráfico, podemos traçar um hiperplano <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/208fbcc5ce29722c2f701868ac31fc3c.svg?invert_in_darkmode" align=middle width=20.216955000000006pt height=22.46574pt/> no limite da classe <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/4b4518f1b7f0fb1347fa21506ebafb19.svg?invert_in_darkmode" align=middle width=18.321105000000006pt height=14.155350000000013pt/> passando pelos pontos <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/5f408b8eb206b0fec18bad40b6366f35.svg?invert_in_darkmode" align=middle width=81.09766499999999pt height=27.656969999999987pt/> e <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/6c48bcb61a0d30b3d1ecaa3a20969c9f.svg?invert_in_darkmode" align=middle width=81.09766499999999pt height=27.656969999999987pt/>. Também é possível passar um hiperplano <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/912631c954499428b64ab8d828ac8cb6.svg?invert_in_darkmode" align=middle width=20.216955000000006pt height=22.46574pt/> no limite da classe <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/f7eb0e840408d84a0c156d6efb611f3e.svg?invert_in_darkmode" align=middle width=18.321105000000006pt height=14.155350000000013pt/> passando pelos pontos <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/ca43186885031ce54a4109d2b5b83474.svg?invert_in_darkmode" align=middle width=81.09766499999999pt height=27.656969999999987pt/> e <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/b2d2e84a937e90beee0ec02286906c47.svg?invert_in_darkmode" align=middle width=81.09766499999999pt height=27.656969999999987pt/>. Nota-se que o hiperplano paralelo à esses dois e com mesma distância aos dois é o que melhor divide as classes de acordo com as amostras dadas. A Figura 5 apresenta os hiperplanos e os vetores de suporte. 

![Figura 5](https://github.com/otaviocx/disciplina-arp/raw/master/estudos/questao6-hiper.png "Hiperplanos de limite e vetores de suporte")

**Figura 5** Hiperplanos de limite e vetores de suporte.

Para a classe <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/4b4518f1b7f0fb1347fa21506ebafb19.svg?invert_in_darkmode" align=middle width=18.321105000000006pt height=14.155350000000013pt/> (+1) os vetores de suporte são: <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/f91e446025d42b8cdf1823520b5d1dbe.svg?invert_in_darkmode" align=middle width=96.62268pt height=27.656969999999987pt/> e <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/96289b4091aa56c30b987d9337aac9aa.svg?invert_in_darkmode" align=middle width=96.62268pt height=27.656969999999987pt/>

Para a classe <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/f7eb0e840408d84a0c156d6efb611f3e.svg?invert_in_darkmode" align=middle width=18.321105000000006pt height=14.155350000000013pt/> (-1) os vetores de suporte são: <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/b15e1de392489bfb2c349afb63c7674a.svg?invert_in_darkmode" align=middle width=96.62268pt height=27.656969999999987pt/> e <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/2fbb2c98b98f3320f28f759996d783b7.svg?invert_in_darkmode" align=middle width=96.62268pt height=27.656969999999987pt/>

Nos vetores acima foi adicionada uma posição no final para bias (por conveniência) com valor 1.

O sistema então apresenta-se da seguinte forma:

<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/c3524fa52dbc4e485c53457205287ef6.svg?invert_in_darkmode" align=middle width=335.44829999999996pt height=88.984995pt/></p>

Resolvendo os produtos entre vetores temos:

<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/3bab6252e8ed613d1fa655b2344a8e55.svg?invert_in_darkmode" align=middle width=214.02644999999998pt height=88.76801999999999pt/></p>

___
2. **Apresente o equacionamento que calcula o hiperplano ótimo em função dos multiplicadores de Lagrange.**

Para a classe <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/4b4518f1b7f0fb1347fa21506ebafb19.svg?invert_in_darkmode" align=middle width=18.321105000000006pt height=14.155350000000013pt/> (+1) os vetores de suporte são: <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/f91e446025d42b8cdf1823520b5d1dbe.svg?invert_in_darkmode" align=middle width=96.62268pt height=27.656969999999987pt/> e <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/96289b4091aa56c30b987d9337aac9aa.svg?invert_in_darkmode" align=middle width=96.62268pt height=27.656969999999987pt/>

Para a classe <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/f7eb0e840408d84a0c156d6efb611f3e.svg?invert_in_darkmode" align=middle width=18.321105000000006pt height=14.155350000000013pt/> (-1) os vetores de suporte são: <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/b15e1de392489bfb2c349afb63c7674a.svg?invert_in_darkmode" align=middle width=96.62268pt height=27.656969999999987pt/> e <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/2fbb2c98b98f3320f28f759996d783b7.svg?invert_in_darkmode" align=middle width=96.62268pt height=27.656969999999987pt/>

<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/593ca5e425b2a79f367061f280a12405.svg?invert_in_darkmode" align=middle width=90.646875pt height=36.655409999999996pt/></p>
<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/77df8b419534e16424d1ba14fec31500.svg?invert_in_darkmode" align=middle width=153.55197pt height=39.45249pt/></p>

<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/8248a54d189b46956ed3e86f74b9f0f5.svg?invert_in_darkmode" align=middle width=159.984495pt height=13.881251999999998pt/></p>

equação do hiperplano: <img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/3211b74041f288d7db6239aaa5ca3946.svg?invert_in_darkmode" align=middle width=89.244375pt height=27.656969999999987pt/>
<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/aca502d2c1023e3fc8e1aea4a7c250c9.svg?invert_in_darkmode" align=middle width=385.93004999999994pt height=39.45249pt/></p>
<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/0feffd7c960c019ad32af81155f9d4a0.svg?invert_in_darkmode" align=middle width=403.71209999999996pt height=16.438356pt/></p>
<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/418a8dd68e1b51cf6e11e6921e276dcc.svg?invert_in_darkmode" align=middle width=406.97579999999994pt height=16.438356pt/></p>
<p align="center"><img src="https://rawgit.com/otaviocx/disciplina-arp/master/estudos/svgs/12796a9118666e440a9bbafa20c13841.svg?invert_in_darkmode" align=middle width=415.19609999999994pt height=16.438356pt/></p>

___