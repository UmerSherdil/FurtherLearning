from sklearn.linear_model import SGDClassifier
import pandas as pd

if __name__ == '__main__':
    col_names = ['Exam_1', 'Exam_2', 'Admission']

    df = pd.read_csv("ex2data1.txt", sep=",", names=col_names)

    temp = df.copy()

    y_train = temp.pop('Admission')
    X_train = temp.copy()

    clf = SGDClassifier(loss="log", learning_rate='constant', eta0=0.001)
    clf.fit(X_train.to_numpy(), y_train.to_numpy())

    print(clf.C)
    print(clf.coef_)

    print(clf.predict_proba([[45, 85]]))
