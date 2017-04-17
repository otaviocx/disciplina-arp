import numpy as np
import pandas as pd
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot


class NaiveBayesClassifier(object):

    def __init__(self, train_dataset, dataset_cols_names):
        self.train_dataset = train_dataset

        self.classes = []
        self.variables_labels = dataset_cols_names
        self.train_inputs, self.train_outputs = self.get_data(self.train_dataset)
        self.inputs_by_class = False

    def get_data(self, path):
        """
        Método responsável por pegar os dados em CSV e retornar uma matriz com as entradas e um vetor com as saídas
        A última coluna do CSV deve ser a variável alvo.
        :type path: String
        :param path: o caminho para o arquivo CSV
        :return: Dois arrays, um de entradas e outro com os respectivos valores de saida.
        """
        data_matrix = pd.read_csv(path).as_matrix()
        inputs = []
        outputs = []
        for row in data_matrix:
            inputs.append(row[:4])
            outputs.append(row[4])

        self.classes = np.unique(outputs)
        return inputs, outputs

    @staticmethod
    def gaussian(variance, mean, value):
        """
        Método responsável por calcular a gaussiana data uma média e uma variancia.
        :type variance: Float
        :param variance: a variancia da variavel
        :type mean: Float
        :param mean: a média da variavel
        :type value: Float
        :param value: o valor de X (entrada)

        :return: o valor de Y na gaussiana (probabilidade)
        """
        exp = math.exp(-(((value-mean)**2)/(2*variance)))
        div = math.sqrt(2*math.pi*variance)
        return (1/div)*exp

    @staticmethod
    def gaussian_vectorized(variance, mean, values):
        """
        Método que aplica a função gaussiana em uma variável para um range de valores.
        :type variance: Float
        :param variance: a variancia da variavel
        :type mean: Float
        :param mean: a média da variavel
        :type values: Array of Float
        :param values: os valors de X (array com vários valores para a mesma variavel)
        :return: vetor contendo o resultado da gaussiana para cada valor no vetor de entrada (values)
        """
        result = []
        for value in values:
            result.append(NaiveBayesClassifier.gaussian(variance, mean, value))
        return result

    @staticmethod
    def gaussian_multi(covariance_matrix, means, values):
        """
        Método responsável por calcular a gaussiana multivariada data as médias e a matriz de covariancia.
        :type covariance_matrix: Matrix of Float
        :param covariance_matrix: a matriz de covariancia
        :type means: Array of Float
        :param means: as médias das variaveis
        :type values: Array of Float
        :param values: Os valores de X (entradas)

        :return: o valor de Y na gaussiana (probabilidade)
        """
        diffs = values - means
        det = np.linalg.det(covariance_matrix)
        inv_cov_matrix = np.linalg.inv(covariance_matrix)

        el = -np.dot(np.dot(np.transpose(diffs), inv_cov_matrix), diffs)/2
        exp = math.exp(el)
        div = math.pow(2*math.pi, len(values)/2)*math.sqrt(det)

        return (1/div)*exp

    def get_inputs_by_class(self):
        """
        Método responsável por separar as entradas por variável e classe
        :return: Dicionário tendo como atributos os nomes das variáveis de entrada. Cada atributo é um outro dicionário
         contendo como atributos as classes de saída.
        """

        if self.inputs_by_class:
            return self.inputs_by_class

        variables_labels = self.variables_labels
        inputs_transpose = np.transpose(self.train_inputs)
        result = {}
        for idx, var_data in enumerate(inputs_transpose):
            if not variables_labels[idx] in result:
                result[variables_labels[idx]] = {}
            for idx_var, value in enumerate(var_data):
                if not self.train_outputs[idx_var] in result[variables_labels[idx]]:
                    result[variables_labels[idx]][self.train_outputs[idx_var]] = []
                result[variables_labels[idx]][self.train_outputs[idx_var]].append(value)

        self.inputs_by_class = result
        return result

    def __get_variances_and_means(self, var_name):
        """
        Método que calcula e retorna as variancias e médias para cada classe em uma determinada variavel.
        :param var_name: O nome da variável em questão, a ser calculadas a variancia e média.
        :return: Dois dicionários em que cada atributo corresponde a uma classe. O primeiro discionário possui as
         variancias e o segundo as médias.
        """
        variances = {}
        means = {}
        inputs_by_class = self.get_inputs_by_class()

        # calculando a variancia e a média para cada classe dessa variável
        for class_name in inputs_by_class[var_name]:
            np_vector = np.array(inputs_by_class[var_name][class_name])
            variances[class_name] = np_vector.std() ** 2
            means[class_name] = np_vector.mean()

        return variances, means

    def predict(self, test_input, debug):
        """
        Método que recebe uma entrada (vetor com variáveis da entrada) e retorna o nome da classe prevista para tal
        entrada.
        :param test_input: Vetor contendo os valores das variáveis de entrada.
        :param debug: Se informado True, imprime detalhes sobre as probabilidades em cada classe.
        :return: String com o nome da classe prevista para a entrada informada.
        """
        probabilities = self.get_probabilities(test_input)
        if debug:
            print("Entrada:", test_input, "Probabilidades:", probabilities)

        # argmax das probabilidades nas classes
        return max(probabilities, key=probabilities.get)

    def predict_and_check(self, test_dataset, debug):
        """
        Método que recebe um dataset de test e para cada entrada faz a previsão de classe e checa com as classes
        informadas no dataset.
        :param test_dataset: String com o caminho do dataset de teste.
        :param debug: Se informado imprime detalhes sobre a classificação
        """
        test_inputs, test_outputs = self.get_data(test_dataset)
        corrects = 0;
        for test_idx, test_input in enumerate(test_inputs):
            predicted = self.predict(test_input, debug)
            if predicted == test_outputs[test_idx]:
                corrects += 1
                print(predicted, "==", test_outputs[test_idx], "=> Correto!")
            else:
                print(predicted, "!=", test_outputs[test_idx], "=> Errado :(")
        print("Taxa de Acerto:", corrects/(test_idx+1)*100, "%")

    def get_probabilities(self, test_input):
        """
        Método que recebe uma entrada (vetor com valores dos atributos da entrada) e retorna as probabilidades para
        cada classe da base de treinamento.
        :param test_input:
        :return:
        """
        probabilities = {}
        for var_idx, var_name in enumerate(self.variables_labels):
            variances, means = self.__get_variances_and_means(var_name)
            for class_name in self.classes:
                if class_name not in probabilities:
                    probabilities[class_name] = 1
                # produtório das probabilidades univariadas (Classificador Naive Bayes)
                probabilities[class_name] *= self.gaussian(variances[class_name], means[class_name],
                                                           test_input[var_idx])
        return probabilities

    def plot_single_var_normal(self):
        """
        Método responsável por plotar a função normal (gaussiana) de cada classe para cada variável.
        """

        x_values = np.arange(-1, 10, 0.1)

        inputs_by_class = self.get_inputs_by_class()
        num = 1
        for var_name in inputs_by_class:
            plot.subplot(2, 2, num)
            plot.subplots_adjust(hspace=0.5)
            legend = []
            variances, means = self.__get_variances_and_means(var_name)
            for class_name in inputs_by_class[var_name]:
                y_values = self.gaussian_vectorized(variances[class_name], means[class_name], x_values)
                legend.append(class_name)
                plot.plot(x_values, y_values)
            plot.legend(legend)
            plot.xlabel(var_name)
            num += 1

        plot.show()

    def plot_two_var_normal(self, vars_combination):
        """
        Método responsável por plotar a função normal (gaussiana) de duas variáveis.
        """

        # criando range 2D para plotar os valores resultantes da gaussiana
        x_values = np.arange(-1, 10, 0.1)
        y_values = np.arange(-1, 10, 0.1)
        x_values, y_values = np.meshgrid(x_values, y_values)

        inputs_by_class = self.get_inputs_by_class()

        fig = plot.figure()
        for class_name in self.classes:
            inputs = []

            # separando apenas as variáveis informadas em um array (inputs)
            for var in vars_combination:
                input_values = inputs_by_class[var][class_name]
                inputs.append(input_values)

            # para cada classe é calculada a matriz de covariancia e as médias das variáveis informadas
            covariance_matrix = np.cov(inputs)
            means = np.mean(inputs, 1)

            # para cada x e y no range, calculando o valor resultante da gaussiana multivariada
            z_values = []
            for x in x_values[0]:
                z_line = []
                for y in x_values[0]:
                    z_line.append(self.gaussian_multi(covariance_matrix, means, [x, y]))
                z_values.append(z_line)

            # adicionando superfice ao gráfico para plotar a gaussiana dessa classe.
            ax = fig.gca(projection='3d')
            plot.xlabel(vars_combination[0])
            plot.ylabel(vars_combination[1])
            ax.plot_surface(y_values, x_values, z_values)

        plot.show()
