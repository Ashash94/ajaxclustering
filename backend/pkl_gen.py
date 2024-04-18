import os
import pickle
import pandas as pd

from sklearn.cluster import KMeans, DBSCAN

from config import DATA_PATH
from processing import format_data


# Data loading
data = pd.read_csv(DATA_PATH)
formatted_data = format_data(data)
X = formatted_data.iloc[:, 3:].values

# Models settings
kmeans_model = KMeans(n_clusters=4, n_init="auto")
dbscan_model = DBSCAN(eps=9, min_samples=3)


# Directory for saving models
output_directory = "pkl"

# Create the directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)


# Listing model to use in loop
model_list = [kmeans_model, dbscan_model]

for model in model_list:
    model_name = type(model).__name__.lower()

    model.fit(X)
    print(f"--- {model_name} trained!")

    file_name = os.path.join(output_directory, f"{model_name}.pkl")

    with open(file_name, "wb") as f:
        pickle.dump(model, f)

    print(f"--- {model_name} saved!")
