import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io

from fastapi.responses import StreamingResponse

from config import DATA_PATH
from processing import format_data


data = pd.read_csv(DATA_PATH)
formatted_data = format_data(data)


def kmeans_plot(model):
    labels = model.predict(
        formatted_data[["Spending Score (1-100)", "Annual Income (k$)"]].values
    )
    centroids = model.cluster_centers_

    plt.figure(1, figsize=(15, 10))
    plt.clf()

    plt.scatter(
        x=formatted_data["Spending Score (1-100)"],
        y=formatted_data["Annual Income (k$)"],
        c=labels,
        s=200,
    )
    plt.scatter(x=centroids[:, 0], y=centroids[:, 1], s=300, c="red", alpha=0.5)
    plt.ylabel("Spending Score (1-100)")
    plt.xlabel("Annual Income (k$)")

    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format="png")
    plt.close()

    img_bytes.seek(0)
    return StreamingResponse(img_bytes, media_type="image/png")


def dbscan_plot(model):
    labels = model.fit_predict(
        formatted_data[["Spending Score (1-100)", "Annual Income (k$)"]].values
    )

    core_samples_mask = np.zeros_like(model.labels_, dtype=bool)
    core_samples_mask[model.core_sample_indices_] = True

    plt.figure(1, figsize=(15, 10))
    plt.clf()

    plt.scatter(
        x=formatted_data["Spending Score (1-100)"][core_samples_mask],
        y=formatted_data["Annual Income (k$)"][core_samples_mask],
        c=labels[core_samples_mask],
        s=200,
        cmap="viridis",
        alpha=0.5,
    )

    plt.scatter(
        x=formatted_data["Spending Score (1-100)"][~core_samples_mask],
        y=formatted_data["Annual Income (k$)"][~core_samples_mask],
        c="gray",
        s=100,
        alpha=0.5,
    )

    plt.ylabel("Spending Score (1-100)")
    plt.xlabel("Annual Income (k$)")

    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format="png")
    plt.close()

    img_bytes.seek(0)
    return StreamingResponse(img_bytes, media_type="image/png")
