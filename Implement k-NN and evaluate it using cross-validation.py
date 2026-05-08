from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

data = load_iris()
X = data.data
y = data.target
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, y, cv=10)
print("Cross Validation Scores:", scores)
print("Average Accuracy:", scores.mean())