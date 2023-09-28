import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report 

data = pd.read_csv("filtered_heart.csv")
print(data.shape)
print(data.head())
print(data.tail())

print(data.isnull().sum())

features = data[["age" , "sex" , "exng" , "caa" , "cp" , "trtbps", "chol", "fbs", "restecg", "thalachh", "oldpeak", "slp"]]
target = data["output"]

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2)  # Corrected test_size

model = LogisticRegression(max_iter=670, random_state=0)  # Added random_state
model.fit(x_train, y_train)

cr = classification_report(y_test, model.predict(x_test))
print(cr)

d = [[43,1,1,4,0,132,247,1,0,143,0.1,1]]
ans = model.predict(d)
print(ans)



age = int(input("Enter Age "))

op = int(input("1 Male , 2 Female "))
if op == 1:
    sex = 1
else:
    sex = 0

op = int(input("Do You Have Pain after exercise 1 Yes, 2 No "))
if op == 1:
    exng = 1
else:
    exng = 0

caa = int(input("Enter the number of vessels "))

op = int(input("Enter Type Of chest Pain : 1 Chest Pain, 2 Abnormal Chest Pain, 3 Pain unrelated to the Heart, 4 No Pain "))
if op == 1:
    cp = 1
elif op == 2:
    cp = 2
elif op == 3:
    cp = 3
else:
    cp = 4

trtbps = int(input("Enter Resting Blood Pressure "))

chol = int(input("Enter Cholesterol via BMI sensor "))

op = int(input("Is FBS more than 120 : 1 Yes 2 No "))
if op == 1:
    fbs = 1
else:
    fbs = 0

op = int(input("Resting ECG : 1 Normal , 2 Arrhythmia  , 3 Enlarged "))
if op == 1:
    restecg = 0
elif op == 2:
    restecg = 1
else:
    restecg = 2

thalachh = int(input("Enter Maximum Heart Rate Achieved "))

oldpeak = float(input("Enter OldPeak "))

op = int(input("SLP : 0, 1, 2"))
if op == 0:
	slp = 0
elif op == 1:
	slp = 1
else :
	slp = 2

usr_data = [[age, sex, exng, caa, cp, trtbps, chol, fbs, restecg, thalachh, oldpeak, slp]]

ans = model.predict(usr_data)
print(ans)
