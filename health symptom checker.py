symptoms = input("Enter symptom: ").lower()

health = {
    "fever": "Take rest and consult doctor",
    "cold": "Drink warm fluids",
    "headache": "Take proper rest"
}

if symptoms in health:
    print(health[symptoms])
else:
    print("Consult a medical professional")