import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVC

from pandas import DataFrame


def plot_data(df: DataFrame, x=None, y=None) -> None:
    fig, ax = plt.subplots()
    for i in range(len(df['Feature_1'])):
        if df['Classification'][i] == 0:
            c = 'r'
        else:
            c = 'g'

        ax.scatter(df['Feature_1'][i], df['Feature_2'][i], color=c)

    if x is not None and y is not None:
        plt.plot(x, y)

    plt.show()


if __name__ == '__main__':
    data = loadmat('ex6data1.mat')
    X_data = data['X']
    y_data = data['y'].reshape((len(data['y'])))

    df = pd.DataFrame(np.column_stack((X_data, y_data)), columns=['Feature_1', 'Feature_2', 'Classification'])
    plot_data(df)

    clf = SVC(C=100.0, kernel='linear')
    clf.fit(X_data, y_data)

    x = np.linspace(min(X_data[:, 0]), max(X_data[:, 0]), 100)
    y = -(clf.coef_[0][0]*x + clf.intercept_[0]) / clf.coef_[0][1]

    plot_data(df, x, y)

    data = loadmat('ex6data2.mat')
    X_data = data['X']
    y_data = data['y'].reshape((len(data['y'])))

    df = pd.DataFrame(np.column_stack((X_data, y_data)), columns=['Feature_1', 'Feature_2', 'Classification'])
    plot_data(df)

    clf = SVC(C=1.0)
    clf.fit(X_data, y_data)

    x_min, x_max = X_data[:, 0].min() - 1, X_data[:, 0].max() + 1
    y_min, y_max = X_data[:, 1].min() - 1, X_data[:, 1].max() + 1

    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))

    temp = np.column_stack((xx.ravel(), yy.ravel()))

    Z = clf.predict(temp)

    Z = Z.reshape(np.shape(xx))

    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X_data[:, 0], X_data[:, 1], c=y_data, s=20, edgecolor="k")

    plt.show()
