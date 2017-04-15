from bayes.classifier import NaiveBayesClassifier

nbc = NaiveBayesClassifier("iris-treinamento.txt",
                           ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])

# LISTA 2, EX 1 - Primeira Parte
nbc.plot_single_var_normal()

# LISTA 2, EX 1 - Segunda Parte
vars_combinations = [
    ['Sepal Length', 'Sepal Width'],
    ['Sepal Length', 'Petal Width'],
    ['Sepal Length', 'Petal Length'],
    ['Petal Length', 'Petal Width'],
    ['Petal Length', 'Sepal Width'],
    ['Petal Width', 'Sepal Width']
]
for vars_combination in vars_combinations:
    nbc.plot_two_var_normal(vars_combination)

# LISTA 2, EX 2
nbc.predict_and_check("iris-teste.txt", True)
