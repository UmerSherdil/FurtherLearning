import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

from pandas import DataFrame, Series
from numpy import ndarray


def plot_horsepower(x: ndarray, y: ndarray, train_features: Series, train_labels: Series, axis) -> None:
  axis[0].scatter(train_features, train_labels, label='Data')
  axis[0].plot(x, y, color='k', label='Predictions')
  # plt.ylim([-5, 30])
  plt.xlabel('Population')
  plt.ylabel('Profit')
  plt.legend()


def plot_loss(history: DataFrame, axis) -> None:
  axis[1].plot(history.history['loss'], label='loss')
  plt.xlabel('Epoch')
  plt.ylabel('Loss')
  plt.legend()
  plt.grid(True)


def check_loss(df: DataFrame):
    X = df['Population'].to_numpy()
    X = np.column_stack((np.ones(97), X))
    y = df['Profit'].to_numpy()
    prediction = np.dot(X, np.array([-3.03, 1.08]))
    error = prediction - y
    squared_error = pow(error, 2)
    sum_squared_error = sum(squared_error)
    average_squared_error = sum_squared_error / 97
    print(average_squared_error)  # 9.14651058453295


if __name__ == '__main__':
    df = pd.read_csv("ex1data1.txt", sep=",",  names=['Population', 'Profit'])

    model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
    batch_gradient_descent = tf.keras.optimizers.SGD(learning_rate=0.001, momentum=0.0)

    model.compile(optimizer=batch_gradient_descent, loss='mean_squared_error')
    history = model.fit(df['Population'], df['Profit'], epochs=1000)

    x = np.linspace(0.0, 30, 31)
    y = model.predict(x)

    _, axis = plt.subplots(1, 2)
    plot_horsepower(x, y, df['Population'], df['Profit'], axis)
    plot_loss(history, axis)

    theta_0 = np.linspace(-10, 10, 10)
    theta_1 = np.linspace(-1, 4, 10)
    J = np.zeros((len(theta_0), len(theta_1)), dtype=float)

    for i in range(0, len(theta_0)):
        for j in range(0, len(theta_1)):
            model.set_weights([np.array([[theta_1[j]]]), np.array([theta_0[i]])])
            J[i, j] = model.evaluate(df['Population'], df['Profit'], verbose=0)

    theta_0, theta_1 = np.meshgrid(theta_0, theta_1)

    fig = plt.figure()
    axes = fig.gca(projection='3d')
    axes.plot_surface(theta_0, theta_1, J)
    plt.show()

    plt.contour(theta_0, theta_1, J, np.logspace(-2, 3, 20))
    plt.show()
