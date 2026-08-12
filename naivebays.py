from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training messages
messages = [
    "Win a free prize now",
    "Congratulations you won money",
    "Claim your free gift",
    "Hello how are you",
    "Let's meet tomorrow",
    "Can you send me the notes"
]

# Labels
labels = [
    "Spam",
    "Spam",
    "Spam",
    "Not Spam",
    "Not Spam",
    "Not Spam"
]

# Convert text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Create model
model = MultinomialNB()

# Train model
model.fit(X, labels)

# New message
new_message = ["Congratulations you won a free gift"]

# Convert new message into numbers
new_X = vectorizer.transform(new_message)

# Predict
prediction = model.predict(new_X)

print("Prediction:", prediction[0])