import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dataset
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Score": [35, 40, 50, 60, 65, 75, 85, 95]
}

df = pd.DataFrame(data)

# Input and Output
X = df[["Hours"]]
y = df["Score"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Prediction
hours = float(input("Enter study hours: "))
prediction = model.predict([[hours]])

print(f"Predicted Exam Score: {prediction[0]:.2f}")

# Plot
plt.scatter(df["Hours"], df["Score"], label="Actual Data")
plt.plot(df["Hours"], model.predict(X), color="red", label="Regression Line")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Student Score Prediction")
plt.legend()
plt.show()