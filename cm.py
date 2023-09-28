import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the data and split it into features and target as in your previous code
data = pd.read_csv("heart.csv")
features = data[["age", "sex", "exng", "caa", "cp", "trtbps", "chol", "fbs", "restecg", "thalachh"]]
target = data["output"]

# Split the data into a training and testing set
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=0)

# Train a logistic regression model as in your previous code
model = LogisticRegression(max_iter=670, random_state=0)
model.fit(x_train, y_train)

# Predict on the test set
y_pred = model.predict(x_test)

# Create a confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Create a heatmap using seaborn and matplotlib
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Calculate and print accuracy
accuracy = (conf_matrix[0, 0] + conf_matrix[1, 1]) / conf_matrix.sum()
print(f"Accuracy: {accuracy:.2f}")
