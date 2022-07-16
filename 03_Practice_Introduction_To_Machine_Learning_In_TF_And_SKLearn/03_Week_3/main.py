import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from pandas import DataFrame


def plot_data(df: DataFrame, x, y) -> None:
    fig, ax = plt.subplots()
    for i in range(len(df['Exam_1'])):
        if df['Admission'][i] == 0:
            c = 'r'
        else:
            c = 'g'

        ax.scatter(df['Exam_1'][i], df['Exam_2'][i], color=c)

    plt.plot(x, y)
    plt.show()


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
    col_names = ['Exam_1', 'Exam_2', 'Admission']

    df = pd.read_csv("ex2data1.txt", sep=",", names=col_names)
    # plot_data(df)

    temp = df.copy()

    y_train = temp.pop('Admission')
    X_train = temp.copy()

    # X_train['Exam_1'] = (X_train['Exam_1'] - X_train['Exam_1'].mean())/X_train['Exam_1'].std()
    # X_train['Exam_2'] = (X_train['Exam_2'] - X_train['Exam_2'].mean()) / X_train['Exam_2'].std()

    model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                        tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)])

    # model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=(2,), activation=tf.nn.sigmoid)])

    batch_gradient_descent = tf.keras.optimizers.SGD(learning_rate=0.00001, momentum=0.0)

    model.compile(optimizer='adam', loss='binary_crossentropy')

    history = model.fit(X_train, y_train, epochs=2000)

    # [array([[0.00752666],  [0.0022248 ]], dtype=float32), array([0.00063845], dtype=float32)]
    # [array([[0.0314111 ], [0.01683211]], dtype=float32), array([-0.14038813], dtype=float32)]

    plot_loss(history, None)
    plt.show()

    print(model.get_weights())

    print(model.predict([[45, 85]]))

    # x = np.linspace(30, 100, 100)
    # print(x)
    # x2 = 15 - x
    #
    # # plt.plot(x, x2)
    # # plt.show()
    #
    # plot_data(df, x, x2)
