import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()


df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['Species'] = iris.target

print("First 5 Rows of Dataset:")
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())


X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))


model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy of the Model:", round(accuracy * 100, 2), "%")


print("\nActual vs Predicted:")

for actual, predicted in zip(y_test, y_pred):
    print(f"Actual: {iris.target_names[actual]}  -->  Predicted: {iris.target_names[predicted]}")


print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))