import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
data = load_iris()
X = data.data
y = data.target.reshape(-1, 1)
encoder = OneHotEncoder(sparse_output=False)  
y = encoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
input_neurons = X_train.shape[1]
hidden_neurons = 5
output_neurons = y_train.shape[1]
learning_rate = 0.01
epochs = 1000
np.random.seed(42)
W1 = np.random.randn(input_neurons, hidden_neurons) * 0.01
W2 = np.random.randn(hidden_neurons, output_neurons) * 0.01
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

for epoch in range(epochs):
    hidden_input = np.dot(X_train, W1)
    hidden_output = sigmoid(hidden_input)
    final_input = np.dot(hidden_output, W2)
    final_output = sigmoid(final_input)
    error = y_train - final_output
    d_output = error * sigmoid_derivative(final_output)
    error_hidden = d_output.dot(W2.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)
    W2 += hidden_output.T.dot(d_output) * learning_rate
    W1 += X_train.T.dot(d_hidden) * learning_rate

hidden_test = sigmoid(np.dot(X_test, W1))
output_test = sigmoid(np.dot(hidden_test, W2))

predictions = np.argmax(output_test, axis=1)
actual = np.argmax(y_test, axis=1)

print("Accuracy:", accuracy_score(actual, predictions))
