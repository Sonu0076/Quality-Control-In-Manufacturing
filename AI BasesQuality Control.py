import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Sample data
data = {
    'weight':    [10.1, 9.8, 10.5, 10.0, 9.2, 8.9, 10.3, 9.5, 10.4, 10.2],
    'length':    [5.0, 5.1, 5.0, 5.2, 4.8, 4.5, 5.0, 4.9, 5.3, 5.1],
    'width':     [3.0, 3.1, 2.9, 3.0, 2.8, 2.6, 3.2, 2.9, 3.1, 3.0],
    'temperature': [22, 23, 21, 22, 25, 27, 22, 24, 21, 22],
    'label':     [1, 1, 1, 1, 0, 0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)
X = df.drop('label', axis=1)
y = df['label']

# Train/Test Split with stratify to ensure both classes are present
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Model Evaluation:\n")
print(classification_report(y_test, y_pred, zero_division=0))

# Predict on new data
new_products = pd.DataFrame([
    {'weight': 9.7, 'length': 5.0, 'width': 3.0, 'temperature': 22},
    {'weight': 8.8, 'length': 4.6, 'width': 2.7, 'temperature': 26},
    {'weight': 10.4, 'length': 5.1, 'width': 3.2, 'temperature': 21},
])

predictions = model.predict(new_products)

# Output
print("\nNew Product Predictions:")
for i, pred in enumerate(predictions):
    status = "PASS" if pred == 1 else "FAIL"
    print(f"Product {i+1}: {status}")