from scipy.io import loadmat
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.model_selection import learning_curve
import numpy as np
from sklearn.model_selection import KFold

from numpy import ndarray


def poly_features(X: ndarray, p: int) -> ndarray:
    for i in range(2, p + 1):
        X = np.column_stack((X, pow(X[:, 0], i)))

    return X


def plot_regression(X: ndarray, y: ndarray, reg):
    plt.scatter(X, y)

    x_plot = np.linspace(-50, 50, 101)
    y_plot = reg.predict(x_plot.reshape((-1, 1)))

    plt.plot(x_plot, y_plot)

    plt.show()



if __name__ == '__main__':
    # 1
    data = loadmat('ex5data1.mat')
    X = data['X']
    y = data['y']
    Xtest = data['Xtest']
    ytest = data['ytest']
    Xval = data['Xval']
    yval = data['yval']

    # 2
    reg = LinearRegression().fit(X, y)
    plot_regression(X, y, reg)

    train_sizes, train_scores, valid_scores = learning_curve(LinearRegression(), np.row_stack((X, Xval)), np.row_stack((y, yval)))

    train_mean = np.mean(train_scores, axis=1)
    valid_mean = np.mean(valid_scores, axis=1)

    plt.plot(train_sizes, train_mean, "o-")
    plt.plot(train_sizes, valid_mean, "o-")
    plt.show()

    # 3
    X = poly_features(X, 8)
    Xval = poly_features(Xval, 8)

    # kf = KFold(n_splits=3)
    # for a, b in kf.split(np.row_stack((X, Xval))):
    #     print(a, b)
    #
    # sys.exit()

    # print(np.row_stack((X, Xval)).shape)
    # sys.exit()

    X = normalize(X, norm='max', axis=0)
    Xval = normalize(Xval, norm='max', axis=0)

    train_sizes, train_scores, valid_scores = learning_curve(LinearRegression(), np.row_stack((X, Xval)), np.row_stack((y, yval)))

    train_mean = np.mean(train_scores, axis=1)
    valid_mean = np.mean(valid_scores, axis=1)

    plt.plot(train_sizes, train_mean, "o-")
    plt.plot(train_sizes, valid_mean, "o-")
    plt.show()

    # 4
    train_scores_list, valid_scores_list = [], []

    lambdas = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3]
    # lambdas = np.linspace(0.0001, 10, 50)
    for lambda_ in lambdas:
        train_sizes, train_scores, valid_scores = learning_curve(Ridge(alpha=lambda_),
                                                                 np.row_stack((X, Xval)), np.row_stack((y, yval)))
        print('-'*20)
        print(np.mean(train_scores, axis=1))
        print(np.mean(valid_scores, axis=1))

        train_mean = np.mean(train_scores, axis=1)[-1]
        valid_mean = np.mean(valid_scores, axis=1)[-1]

        train_scores_list.append(train_mean)
        valid_scores_list.append(valid_mean)

    print(train_scores_list)
    plt.plot(lambdas, train_scores_list, "o-")
    plt.plot(lambdas, valid_scores_list, "o-")
    plt.show()
