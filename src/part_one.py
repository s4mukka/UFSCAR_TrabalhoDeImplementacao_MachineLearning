import pandas as pd
from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, classification_report


class PartOne:
    def __init__(self):
        self.dataframe = pd.read_csv('./src/datasets/winequality-red.csv')
        self.dataset = self.dataframe.iloc

    def decision_tree(self, X_train, y_train):
        clf = tree.DecisionTreeClassifier(criterion='entropy')
        clf.fit(X_train, y_train)

        fig = plt.figure(figsize=(100, 30))
        fig = tree.plot_tree(clf, fontsize=10)

        plt.savefig('./src/imgs/plot_decision_tree.png')

        return clf

    def report(self, clf, X_test, y_test):
        predicted = clf.predict(X_test)

        print("Relatório de avaliação do classificador: \n")
        print(f"{classification_report(y_test, predicted)}")

    def confusion_matrix(self, clf, X_test, y_test):
        title = "Matriz de Confusão"
        disp = plt.figure(figsize=(10, 15))
        disp = plot_confusion_matrix(
            clf,
            X_test,
            y_test,
            cmap=plt.cm.Blues,
        )
        disp.ax_.set_title(title)

        plt.savefig('./src/imgs/plot_confusion_matrix.png')

    def run(self):
        X = self.dataset[:, :-1]
        y = self.dataset[:, 11]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, random_state=0)

        clf = self.decision_tree(X_train, y_train)

        self.report(clf, X_test, y_test)

        self.confusion_matrix(clf, X_test, y_test)
