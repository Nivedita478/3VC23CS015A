import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dataset
data = {
    "Area": [500, 700, 900, 1100, 1300, 1500, 1700, 2000],
    "Price": [2000000, 2800000, 3600000, 4500000, 5300000, 6100000, 6900000, 8000000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Input and Output
X = df[["Area"]]
y = df["Price"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# User Input
area = float(input("Enter house area (sq ft): "))

# Prediction
predicted_price = model.predict([[area]])

print(f"Predicted House Price: ₹{predicted_price[0]:,.2f}")

# Plot
plt.scatter(df["Area"], df["Price"], color="blue", label="Actual Data")
plt.plot(df["Area"], model.predict(X), color="red", label="Regression Line")
plt.xlabel("Area (sq ft)")
plt.ylabel("House Price")
plt.title("House Price Prediction")
plt.legend()
plt.show()