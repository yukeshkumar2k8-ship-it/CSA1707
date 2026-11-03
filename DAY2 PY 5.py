from sklearn.tree import DecisionTreeClassifier

x = [
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0],
    [1, 1],
    [0, 0]
]

y = ["Yes", "Yes", "No", "No", "Yes", "No"]

model = DecisionTreeClassifier()
model.fit(x, y)

prediction = model.predict([[1, 0]])

print("Decision Tree Prediction:", prediction[0])
