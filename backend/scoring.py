import pandas as pd
import pickle

from sklearn.metrics import silhouette_score

from config import DATA_PATH
from processing import format_data


DATA = pd.read_csv(DATA_PATH)
formatted_data = format_data(DATA)
X = formatted_data.iloc[:, 3:].values


# Models loading
with open("pkl/kmeans.pkl", "rb") as f:
    kmeans_model = pickle.load(f)

with open("pkl/dbscan.pkl", "rb") as f:
    dbscan_model = pickle.load(f)


def get_kmeans_silhouette_score():
    kmeans_labels = kmeans_model.predict(
        formatted_data[["Spending Score (1-100)", "Annual Income (k$)"]].values
    )

    return silhouette_score(X, kmeans_labels)


def get_dbscan_silhouette_score():
    dbscan_labels = dbscan_model.fit_predict(
        formatted_data[["Spending Score (1-100)", "Annual Income (k$)"]].values
    )

    return silhouette_score(X, dbscan_labels)
