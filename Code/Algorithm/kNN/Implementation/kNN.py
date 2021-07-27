import numpy as np
from math import sqrt
from collections import Counter


def kNN(K, X_train, Y_train, x):
    # kNN, the only one method does not need training process, or the training process is model
    assert 1 <= K <= X_train.shape[0], "K must be valid"
    assert X_train.shape[0] == Y_train.shape[0], "K must be valid"
    assert X_train.shape[1] == x.shape[0], "K must be valid"

    distance = [sqrt(np.sum((x_train - x) ** 2)) for x_train in X_train]
    nearest = np.argsort(distance)

    topK_y = [Y_train[i] for i in nearest[:K]]
    votes = Counter(topK_y)

    return votes.most_common(1)[0][0]
