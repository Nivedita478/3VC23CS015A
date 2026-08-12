from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
data = load_diabetes()

X = data.data
y = (data.target > data.target.mean()).astype(int)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LogisticRegression(max_iter=1000)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Predict for one new sample
new_person = [X_test[0]]

prediction = model.predict(new_person)

if prediction[0] == 1:
    print("Prediction: Higher diabetes progression")
else:
    print("Prediction: Lower diabetes progression")