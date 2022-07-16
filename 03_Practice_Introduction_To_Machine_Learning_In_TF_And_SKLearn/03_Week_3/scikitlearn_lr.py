from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scikitplot as skplot

from pandas import DataFrame
from numpy import ndarray

from typing import Optional


def plot_data(df: DataFrame, x: Optional[ndarray], y: Optional[ndarray]) -> None:
    fig, ax = plt.subplots()
    for i in range(len(df['Exam_1'])):
        if df['Admission'][i] == 0:
            c = 'r'
        else:
            c = 'g'

        ax.scatter(df['Exam_1'][i], df['Exam_2'][i], color=c)

    if x is not None or y is not None:
        plt.plot(x, y)

    plt.show()


def first_part() -> None:
    col_names = ['Exam_1', 'Exam_2', 'Admission']

    df = pd.read_csv("ex2data1.txt", sep=",", names=col_names)

    temp = df.copy()

    y_train = temp.pop('Admission')
    X_train = temp.copy()

    LogisticRegression(random_state=0).fit(X_train.to_numpy(), y_train.to_numpy())

    x = np.linspace(30, 100, 100)
    x2 = 124.9481 - 1.0239*x

    plot_data(df, x, x2)


def feature_mapping(X_train: ndarray) -> ndarray:
    out = X_train.copy()

    for i in range(0, 6):
        out = np.column_stack((out, out[:, 0] * pow(out[:, 1], i)))

    for i in range(0, 6):
        if i == 1:
            continue
        out = np.column_stack((out, pow(out[:, 0], i) * out[:, 1]))

    for i in range(2, 7):
        out = np.column_stack((out, pow(out[:, 0], i)))
        out = np.column_stack((out, pow(out[:, 1], i)))

    return out


if __name__ == '__main__':
    # first_part()

    inv_lambda_ = 0.01

    df = pd.read_csv("ex2data2.txt", sep=",", names=['Exam_1', 'Exam_2', 'Admission'])
    y_train = df.pop('Admission').copy().to_numpy()
    X_train = df.copy().to_numpy()
    # plot_data(df, None, None)

    X_train = feature_mapping(X_train)

    lr = LogisticRegression(C=inv_lambda_)
    lr.fit(X_train, y_train)

    print('Accuracy: ', lr.score(X_train, y_train))

    x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
    y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1

    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 119), np.linspace(y_min, y_max, 119))

    temp = np.column_stack((xx.ravel(), yy.ravel()))
    temp = feature_mapping(temp)

    Z = lr.predict(temp)

    Z = Z.reshape(np.shape(xx))

    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, s=20, edgecolor="k")

    plt.show()
