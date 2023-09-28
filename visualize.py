import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load and preprocess the data
data = pd.read_csv("filtered_heart.csv")
features = data[["age", "sex", "exng", "caa", "cp", "trtbps", "chol", "fbs", "restecg", "thalachh", "oldpeak", "slp"]]
target = data["output"]

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

# Train the machine learning model
model = LogisticRegression(max_iter=670, random_state=0)
model.fit(x_train, y_train)

# Create a function to visualize data using Matplotlib
def visualize_data():
    # Example: Creating a histogram of the age feature
    plt.figure(figsize=(8, 6))
    plt.hist(data["age"], bins=20, color="teal", edgecolor="black")
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    
    # You can add more visualization code here

    # Display the plot
    plt.show()

# Create the tkinter window
window = tk.Tk()
window.title("Data Visualization")
window.geometry("400x300")  # Set the window size

# Create a button to trigger data visualization
visualize_button = ttk.Button(window, text="Visualize Data", command=visualize_data)
visualize_button.pack(pady=20)

# Run the tkinter main loop
window.mainloop()
