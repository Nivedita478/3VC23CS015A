import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense

# Load CIFAR-10 dataset
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.cifar10.load_data()

# CIFAR-10:
# 3 = Cat
# 5 = Dog

# Keep only cats and dogs
train_filter = (y_train[:, 0] == 3) | (y_train[:, 0] == 5)
test_filter = (y_test[:, 0] == 3) | (y_test[:, 0] == 5)

X_train = X_train[train_filter]
y_train = y_train[train_filter]

X_test = X_test[test_filter]
y_test = y_test[test_filter]

# Convert:
# Cat = 0
# Dog = 1

y_train = (y_train == 5).astype(int).ravel()
y_test = (y_test == 5).astype(int).ravel()

# Normalize pixel values
X_train = X_train / 255.0
X_test = X_test / 255.0

# Create neural network
model = Sequential([
    Flatten(input_shape=(32, 32, 3)),
    Dense(128, activation="relu"),
    Dense(1, activation="sigmoid")
])

# Compile
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Train
model.fit(
    X_train,
    y_train,
    epochs=10,
    validation_split=0.2
)

# Test
loss, accuracy = model.evaluate(X_test, y_test)

print("Test Accuracy:", accuracy)