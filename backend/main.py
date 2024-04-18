import uvicorn
import pickle

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scoring import get_kmeans_silhouette_score, get_dbscan_silhouette_score
from plotting import kmeans_plot, dbscan_plot


origins = ["*"]


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Models loading
with open("pkl/kmeans.pkl", "rb") as f:
    kmeans_model = pickle.load(f)

with open("pkl/dbscan.pkl", "rb") as f:
    dbscan_model = pickle.load(f)


@app.get("/k-means/score")
def return_kmeans_silhouette_score():
    result_kmeans = get_kmeans_silhouette_score()
    return {"result": result_kmeans}


@app.get("/k-means/plot")
def return_kmeans_plot():
    return kmeans_plot(kmeans_model)


@app.get("/dbscan/score")
def return_dbscan_silhouette_score():
    result_dbscan = get_dbscan_silhouette_score()
    return {"result": result_dbscan}


@app.get("/dbscan/plot")
async def return_dbscan_plot():
    return dbscan_plot(dbscan_model)

uvicorn.run(app, host="0.0.0.0", port=8000)
