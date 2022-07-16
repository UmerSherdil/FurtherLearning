from scipy.io import loadmat
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier

import numpy as np

if __name__ == '__main__':
    data = loadmat('ex3data1.mat')

    X_train = data['X']
    y_train = data['y'].reshape(5000,)

    number_of_rows = X_train.shape[0]
    random_indices = np.random.choice(number_of_rows, size=100)

    samples = X_train[random_indices, :]

    fig, axs = plt.subplots(10, 10)
    for i in range(10):
        for j in range(10):
            axs[i, j].imshow(samples[i + j, :].reshape((20, 20)), cmap='gray', origin="lower")
            axs[i, j].axis('off')

    plt.show()

    clf = MLPClassifier(solver='lbfgs', alpha=0, hidden_layer_sizes = (25,), activation='logistic')
    clf.fit(X_train, y_train)
    print(clf.score(X_train, y_train))

    samples = clf.coefs_[0]

    fig, axs = plt.subplots(5, 5)
    for i in range(5):
        for j in range(5):
            axs[i, j].imshow(samples[:, i + j].reshape((20, 20)), cmap='gray', origin="lower")
            axs[i, j].axis('off')

    plt.show()
