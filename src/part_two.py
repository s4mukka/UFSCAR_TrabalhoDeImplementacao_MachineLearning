import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics as sm
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans


class PartTwo:
    def __init__(self):
        self.dataframe = pd.read_csv(
            './src/datasets/BitcoinHeistData.csv').drop(['address'], axis=1)
        self.categorical_features = ['year', 'day', 'label']
        self.continuous_features = ['length', 'weight',
                                    'count', 'looped', 'neighbors', 'income']

    def transform_categorical_features_in_binary(self):
        for col in self.categorical_features:
            dummies = pd.get_dummies(self.dataframe[col], prefix=col)
            self.dataframe = pd.concat([self.dataframe, dummies], axis=1)
            self.dataframe.drop(col, axis=1, inplace=True)

    def scale_continuous_features(self):
        mms = MinMaxScaler()
        mms.fit(self.dataframe)
        data_transformed = mms.transform(self.dataframe)

        return data_transformed

    def grouping_for_each_group_quantity(self, data_transformed, K):
        Sum_of_squared_distances = []

        for k in K:
            km = KMeans(n_clusters=k)
            km = km.fit(data_transformed)
            Sum_of_squared_distances.append(km.inertia_)

        return Sum_of_squared_distances

    def build_the_graph_number_of_clusters(self, K, Sum_of_squared_distances):
        plt.plot(K, Sum_of_squared_distances, 'bx-')
        plt.xlabel('k')
        plt.ylabel('Soma dos quadrados das distâncias')
        plt.title('Método do Cotovelo para encontrar melhor valor de k')
        plt.savefig('./src/imgs/elbow_method_to_find_the_best_k_value.png')

    def run(self):
        self.transform_categorical_features_in_binary()
        data_transformed = self.scale_continuous_features()
        K = range(2, 15)
        Sum_of_squared_distances = self.grouping_for_each_group_quantity(
            data_transformed, K)
        self.build_the_graph_number_of_clusters(K, Sum_of_squared_distances)
