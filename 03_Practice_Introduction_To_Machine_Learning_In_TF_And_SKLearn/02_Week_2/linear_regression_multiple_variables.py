import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from pandas import DataFrame, Series
from numpy import ndarray


def plot_loss(history: DataFrame, axis=None) -> None:
    if axis is None:
        plt.plot(history.history['loss'], label='loss')
    else:
        axis[1].plot(history.history['loss'], label='loss')

    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)


if __name__ == '__main__':
    col_names = ['Size', 'Number_of_Bedrooms', 'Price']

    df = pd.read_csv("ex1data2.txt", sep=",", names=col_names)

    # Plot X,Y,Z
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(df['Size'], df['Number_of_Bedrooms'], df['Price'], color='white', edgecolors='grey', alpha=0.5)
    ax.scatter(df['Size'], df['Number_of_Bedrooms'], df['Price'], c='red')
    plt.show()

    for item in col_names:
        df[item] = (df[item] - df[item].mean())/df[item].std()

    y_train = df.pop('Price')

    # Both models work
    # model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
    #                                     tf.keras.layers.Dense(1)])

    model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=(2,))])
    batch_gradient_descent = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.0)

    model.compile(optimizer=batch_gradient_descent, loss='mean_squared_error')
    history = model.fit(df, y_train, epochs=200)

    plot_loss(history, None)
    plt.show()

    print(model.summary())
