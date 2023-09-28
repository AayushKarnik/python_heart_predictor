import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Step 1: Load and preprocess the data
data = pd.read_csv("filtered_heart.csv")
features = data[["age", "sex", "exng", "caa", "cp", "trtbps", "chol", "fbs", "restecg", "thalachh", "oldpeak", "slp"]]
target = data["output"]

# Step 2: Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

# Step 3: Train the machine learning model
model = LogisticRegression(max_iter=670, random_state=0)
model.fit(x_train, y_train)

# Function to make predictions
def predict_heart_disease():
    try:
        age = int(age_entry.get())
        sex = sex_var.get()
        exng = exng_var.get()
        caa = int(caa_entry.get())
        cp = cp_var.get()
        trtbps = int(trtbps_entry.get())
        chol = int(chol_entry.get())
        fbs = fbs_var.get()
        restecg = restecg_var.get()
        thalachh = int(thalachh_entry.get())
        oldpeak = float(oldpeak_entry.get())
        slp = slp_var.get()
        
        usr_data = [[age, sex, exng, caa, cp, trtbps, chol, fbs, restecg, thalachh, oldpeak, slp]]
        
        ans = model.predict(usr_data)
        result_label.config(text=f"Predicted Output: {ans[0]}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid input.")

# Create the tkinter window
window = tk.Tk()
window.title("Heart Disease Prediction")
window.geometry("800x600")  # Set the window size

# Set background color to lavender and text color to teal
window.configure(bg="lavender")
style = ttk.Style(window)
style.configure("TLabel", background="lavender", foreground="teal")

# Create a frame with a scrollbar for scrolling
frame = ttk.Frame(window)
frame.pack(fill=tk.BOTH, expand=1)

canvas = tk.Canvas(frame)
scroll_y = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scroll_y.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=1)
canvas.configure(yscrollcommand=scroll_y.set)

# Create a new frame inside the canvas
inner_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Create labels and entry fields for user input
age_label = ttk.Label(inner_frame, text="Enter Age:")
age_label.grid(row=0, column=0, padx=10, pady=5)
age_entry = ttk.Entry(inner_frame)
age_entry.grid(row=0, column=1, padx=10, pady=5)

sex_label = ttk.Label(inner_frame, text="Select Gender:")
sex_label.grid(row=1, column=0, padx=10, pady=5)
sex_var = tk.IntVar()
male_radio = ttk.Radiobutton(inner_frame, text="Male", variable=sex_var, value=1)
female_radio = ttk.Radiobutton(inner_frame, text="Female", variable=sex_var, value=0)
male_radio.grid(row=1, column=1, padx=10, pady=5)
female_radio.grid(row=1, column=2, padx=10, pady=5)

exng_label = ttk.Label(inner_frame, text="Exercise Induced Angina:")
exng_label.grid(row=2, column=0, padx=10, pady=5)
exng_var = tk.IntVar()
yes_radio = ttk.Radiobutton(inner_frame, text="Yes", variable=exng_var, value=1)
no_radio = ttk.Radiobutton(inner_frame, text="No", variable=exng_var, value=0)
yes_radio.grid(row=2, column=1, padx=10, pady=5)
no_radio.grid(row=2, column=2, padx=10, pady=5)

caa_label = ttk.Label(inner_frame, text="Number of Vessels:")
caa_label.grid(row=3, column=0, padx=10, pady=5)
caa_entry = ttk.Entry(inner_frame)
caa_entry.grid(row=3, column=1, padx=10, pady=5)

cp_label = ttk.Label(inner_frame, text="Type of Chest Pain:")
cp_label.grid(row=4, column=0, padx=10, pady=5)
cp_var = tk.IntVar()
chest_pain_options = [("Chest Pain", 1), ("Abnormal Chest Pain", 2), ("Pain Unrelated to Heart", 3), ("No Pain", 4)]
for i, (text, value) in enumerate(chest_pain_options):
    cp_radio = ttk.Radiobutton(inner_frame, text=text, variable=cp_var, value=value)
    cp_radio.grid(row=4, column=i+1, padx=10, pady=5)

trtbps_label = ttk.Label(inner_frame, text="Resting Blood Pressure:")
trtbps_label.grid(row=5, column=0, padx=10, pady=5)
trtbps_entry = ttk.Entry(inner_frame)
trtbps_entry.grid(row=5, column=1, padx=10, pady=5)

chol_label = ttk.Label(inner_frame, text="Cholesterol:")
chol_label.grid(row=6, column=0, padx=10, pady=5)
chol_entry = ttk.Entry(inner_frame)
chol_entry.grid(row=6, column=1, padx=10, pady=5)

fbs_label = ttk.Label(inner_frame, text="Fasting Blood Sugar:")
fbs_label.grid(row=7, column=0, padx=10, pady=5)
fbs_var = tk.IntVar()
fbs_options = [("Yes (> 120 mg/dl)", 1), ("No (<= 120 mg/dl)", 0)]
for i, (text, value) in enumerate(fbs_options):
    fbs_radio = ttk.Radiobutton(inner_frame, text=text, variable=fbs_var, value=value)
    fbs_radio.grid(row=7, column=i+1, padx=10, pady=5)

restecg_label = ttk.Label(inner_frame, text="Resting ECG:")
restecg_label.grid(row=8, column=0, padx=10, pady=5)
restecg_var = tk.IntVar()
ecg_options = [("Normal", 0), ("Arrhythmia", 1), ("Enlarged", 2)]
for i, (text, value) in enumerate(ecg_options):
    ecg_radio = ttk.Radiobutton(inner_frame, text=text, variable=restecg_var, value=value)
    ecg_radio.grid(row=8, column=i+1, padx=10, pady=5)

thalachh_label = ttk.Label(inner_frame, text="Maximum Heart Rate Achieved:")
thalachh_label.grid(row=9, column=0, padx=10, pady=5)
thalachh_entry = ttk.Entry(inner_frame)
thalachh_entry.grid(row=9, column=1, padx=10, pady=5)

oldpeak_label = ttk.Label(inner_frame, text="Old Peak:")
oldpeak_label.grid(row=10, column=0, padx=10, pady=5)
oldpeak_entry = ttk.Entry(inner_frame)
oldpeak_entry.grid(row=10, column=1, padx=10, pady=5)

slp_label = ttk.Label(inner_frame, text="SLP:")
slp_label.grid(row=11, column=0, padx=10, pady=5)
slp_var = tk.IntVar()
slp_options = [("0", 0), ("1", 1), ("2", 2)]
for i, (text, value) in enumerate(slp_options):
    slp_radio = ttk.Radiobutton(inner_frame, text=text, variable=slp_var, value=value)
    slp_radio.grid(row=11, column=i+1, padx=10, pady=5)

# Create a button to make predictions
predict_button = ttk.Button(inner_frame, text="Predict", command=predict_heart_disease)
predict_button.grid(row=12, column=0, columnspan=2, pady=10)

# Create a label to display the result
result_label = ttk.Label(inner_frame, text="")
result_label.grid(row=13, column=0, columnspan=2, pady=5)

# Configure the canvas scrolling region
inner_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Run the tkinter main loop
window.mainloop()
