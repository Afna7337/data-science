# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
data = {
    "FoodType": ["Apple", "Banana", "Carrot", "Cucumber", "Potato", "Watermelon", "Onion", "Pear"],
    "Sweetness": [7, 9, 3, 2, 1, 10, 2, 6],
    "Crunchiness": [8, 2, 9, 7, 4, 3, 6, 7]
}
food = pd.DataFrame(data)
print("Dataset:\n", food)

# Features and labels
X = food[["Sweetness", "Crunchiness"]]
y = food["FoodType"]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
tomato = pd.DataFrame({"Sweetness": [4], "Crunchiness": [6]})
tomato_scaled = scaler.transform(tomato)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_scaled, y)
prediction = knn.predict(tomato_scaled)
print("\nThe predicted food type of Tomato is:", prediction[0])
