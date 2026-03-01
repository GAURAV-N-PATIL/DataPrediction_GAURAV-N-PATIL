import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

data['Age'] = data['Age'].fillna(data['Age'].mean())
data['Fare'] = data['Fare'].fillna(data['Fare'].mean())

print("Dataset Preview")
print(data.head())

print("\nSummary Statistics")
print(data[['Age', 'Fare']].describe())

mean_age = data['Age'].mean()
median_age = data['Age'].median()

print("\nMean Age:", round(mean_age, 2))
print("Median Age:", round(median_age, 2))

plt.figure()
plt.hist(data['Age'], bins=20)
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Age Distribution of Passengers")
plt.savefig("age_distribution.png")
plt.show()

plt.figure()
plt.scatter(data['Age'], data['Fare'])
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Age vs Fare")
plt.savefig("age_vs_fare.png")
plt.show()

x = data['Age'].values
y = data['Fare'].values

coefficients = np.polyfit(x, y, 1)
slope = coefficients[0]
intercept = coefficients[1]

predicted_fare = slope * x + intercept

print("\nPrediction Equation")
print("Fare =", round(slope, 2), "* Age +", round(intercept, 2))

plt.figure()
plt.scatter(x, y)
plt.plot(x, predicted_fare)
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Fare Prediction Based on Age")
plt.savefig("fare_prediction.png")
plt.show()

future_ages = np.array([20, 30, 40, 50])
future_fares = slope * future_ages + intercept

print("\nPredicted Fare Values")
for age, fare in zip(future_ages, future_fares):
    print("Age:", age, "-> Predicted Fare:", round(fare, 2))