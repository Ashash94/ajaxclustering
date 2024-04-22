import pytest
from fastapi.testclient import TestClient
from requests.exceptions import RequestException

from main import app, HOST, PORT

client = TestClient(app)

endpoints = [
    ("/k-means/score", "score"),
    ("/k-means/plot", "plot"),
    ("/dbscan/score", "score"),
    ("/dbscan/plot", "plot"),
]

PORT = str(PORT)

def test_api_endpoints():
    for endpoint, endpoint_type in endpoints:
        try:
            full_url = HOST + ":" + PORT + endpoint 
            response = client.get(full_url)
            assert response.status_code == 200, f"La requête à {full_url} a échoué avec le code {response.status_code}"

            if endpoint_type == "score":
                json_data = response.json()
                result = json_data["result"]
                print("Le résultat est le suivant:",result)
                assert -1 <= result <= 1, f"Le silhouette score de {result} ne respecte pas les valeurs attendues pour {full_url}."
            elif endpoint_type == "plot":
                headers = response.headers
                format_type = headers.get("content-type")
                print("Le format de l'image:",format_type)
                assert format_type == "image/png", f"L'API ne renvoie pas une image PNG pour {full_url}."
        except RequestException as e:
            pytest.fail(f"Erreur lors de la requête {full_url}: {e}")


