from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
# Load dataset (Iris dataset)
data = load_iris()
X = data.data # Features
y = data.target # Target labels
# Create k-NN model (k = 5)
knn = KNeighborsClassifier(n_neighbors=5)
# Perform 10-fold Cross Validation
scores = cross_val_score(knn, X, y, cv=10)
# Print results
print("Cross Validation Scores:", scores)
print("Average Accuracy:", scores.mean())