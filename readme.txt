# **Trabalho de Implementação** - *Aprendizado de Máquina*

Este projeto tem consiste na execução e validação de algorítmos de aprendizado supervisionado para classificação *(árvore de decisão)* e não supervisionado para agrupamento *(K-means)* estudados na disciplina **Inteligência Artificial** do curso **Bacharelado em Ciência da Computação** na universidade **Universidade Federal de São Carlos**.


## **Main**

O arquivo *main&#46;py* serve para inicializar o programa, mostrando um menu para que se escolha qual programa ira rodar, *part_one&#46;py (Parte 1)* ou *part_two&#46;py (Parte 2)*

## **Parte 1** - *Avaliação de árvore de decisão com métricas para classificação*

### Dataset utilizado

Foi utilzado o dataset winequality-red.csv retirado do site http://archive.ics.uci.edu/ml/datasets/Wine.

Atributos:
- fixed acidity
- volatile acidity
- citric acid
- residual sugar
- chlorides
- free sulfur dioxide
- total sulfur dioxide
- density
- pH
- sulphates
- alcohol
- quality

### Classe PartOne

- O *construtor* inicializa as variáveis *dataframe (utilizando read_csv do pandas)* e *dataset (utilizando dataframe.iloc)*
- O método *decision_tree* recebe como argumentos *X_train* e *y_train* e tem como função gerar a árvore de decisão para classificação. O método retorna a árvore.
- O método *report* recebe como argumentos *clf*, *X_test* e *y_test* e tem como função gerar o relatório de avaliação do classificador
- O método *confusion_matrix* recebe como argumentos *clf*, *X_test* e *y_test* e tem como função gerar a matriz de classificação
- O método *run* não recebe nada como argumento e tem como função rodar o algoritmo pedido.
  - Separar o conjunto de dados em matriz de atributos (X) e vetor de classes (y). Onde o (y) é o atributo *quality*, o qual é o atríbuto que queremos prever, e o (X) são os restantes dos atributos.
  - Dividir o conjunto de dados em um conjunto de treinamento e um conjunto de teste.
  - Aplicar o algoritmo de indução de árvore de decisão no conjunto de treinamento.
  - Fazer a avaliação do modelo gerado usando os dados de teste e mostrando os resultados.
  
## **Parte 2** - *Avaliação de árvore de decisão com métricas para classificação*

### Dataset utilizado

Foi utilzado o dataset BitcoinHeistData.csv retirado do site https://archive.ics.uci.edu/ml/datasets/BitcoinHeistRansomwareAddressDataset, porém com um tamanho reduzido, pois o tamanho original estava consumindo toda a minha RAM

Atributos:
- address *Este atríbuto acabou não sendo utilizado pois não é necessário para o estudo*
- year
- day
- length
- weight
- count
- looped
- neighbors
- income
- label

### Classe PartTwo

- O *construtor* inicializa as variáveis *dataframe (utilizando read_csv do pandas e com um drop na coluna 'address')*, *categorical_features (year, day and label)* e *continuous_features (o restante das colunas)*
- O método *transform_categorical_features_in_binary* não recebe nada como argumento e tem como função transformar os atributos nominais em binários
- O método *scale_continuous_features* tem como função normalizar os atributos contínuos e retorna *data_transformed*
- O método *grouping_for_each_group_quantity* recebe como argumentos *data_transformed* e *K*, tem como função aplicar o algoritmo k-means no conjunto de dados para todos os valores do intervalo *K* e coletar o valor do índice ‘soma quadrática das distâncias’ para todos os agrupamentos encontrados e retorna *Sum_of_squared_distances*
- O método *build_the_graph_number_of_clusters* recebe como argumentos *K* e *Sum_of_squared_distances* e tem como função gerar o gráfico dos índices encontrados para cada número de grupos
- O método *run* não recebe nada como argumento e tem como função rodar o algoritmo pedido.
  - Transformar atributos nominais em binários.
  - Normalizar os atributos contínuos.
  - Aplicar o algoritmo k-means no conjunto de dados.
  - Coletar o valor do índice ‘soma quadrática das distâncias’ para todos os agrupamentos encontrados.
  - Plotar o gráfico dos índices encontrados para cada número de grupos.

## Makefile

 O Makefile serve apenas para rodar o programa com python3 src/main.py
 