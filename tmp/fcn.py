import numpy as np

def relu(x):
    return np.maximum(0, x)

def softmax(x):
    x = x - np.max(x, axis=1, keepdims=True)
    return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)

x = np.ones((3, 5))
y = softmax(x)
z = np.sum(np.exp(x), axis=1, keepdims=True)

print()
