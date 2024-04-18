import requests

URL_API = "http://localhost:8000"

list_url = [
    URL_API + "/k-means/score",
    URL_API + "/k-means/plot",
    URL_API + "/dbscan/score",
    URL_API + "/dbscan/plot",
]


def check_response(list_link):
    for u in list_link:
        try:
            response = requests.get(u)
            if response.status_code == 200:
                if "score" in u:
                    print(u)
                    json_data = response.json()
                    result = json_data["result"]
                    if -1 <= result <= 1:
                        print(
                            f"Le silhouette score de {result} respecte les valeurs attendues."
                        )
                    else:
                        print(
                            f"Le silhouette score de {result} ne respecte pas les valeurs attendues."
                        )
                elif "plot" in u:
                    print(u)
                    headers = response.headers
                    format_type = headers.get("content-type")
                    if format_type == "image/png":
                        print("L'API renvoie bien une image.")
                    else:
                        print("La donnée envoyée ne respecte pas le format attendu")
                else:
                    print(u)
                    print("L'URL ne renvoie ni de score ni un graphique.")
            else:
                print(u)
                print("La requête n'a pas abouti :", response.status_code)

        except Exception as e:
            print(f"Erreur suivante: {e}")


check_response(list_url)
