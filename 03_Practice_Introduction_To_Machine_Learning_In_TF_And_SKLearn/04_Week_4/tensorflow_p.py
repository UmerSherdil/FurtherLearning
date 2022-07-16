from scipy.io import loadmat
import tensorflow as tf

if __name__ == '__main__':
    data = loadmat('ex3data1.mat')

    X_train = data['X']
    y_train = data['y'].reshape(5000,)

    y_train[y_train == 10] = 0

    model = tf.keras.models.Sequential([
        # tf.keras.layers.Flatten(),
        # tf.keras.layers.Dense(128, activation=tf.nn.relu),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.fit(X_train, y_train, epochs=15)
