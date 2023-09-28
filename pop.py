import pandas as pd

# Load the original dataset
data = pd.read_csv("heart.csv")

# Select only the desired columns (features and target)
selected_columns = ["age", "sex", "exng", "caa", "cp", "trtbps", "chol", "fbs", "restecg", "thalachh", "oldpeak", "slp", "output"]
filtered_data = data[selected_columns]

# Save the filtered DataFrame to a new CSV file
filtered_data.to_csv("filtered_heart.csv", index=False)
