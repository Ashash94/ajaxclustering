# SIMPLON DEV IA | Brief 15

## AJAX Clustering

### Contexte

Pour ce brief, je dois :<br>
    - Développer un back-end avec les modèles proprement dits, et plusieurs modalités de clustering<br>
    - Spécifier la façon par laquelle mon programme peut interagir avec ce back<br>
    - Développer un front-end permettant de changer les paramètres en utilisant AJAX<br>

### Data

[Lien vers les données à utiliser](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

### Structure du projet

```bash
project/
│
├── .github/
│   └── workflows/
│       └── deploy.yml    # Github action workflow when pushed on main branch
│
├── backend/
│   ├── data/
│   │   └── mall_customers.csv    # Emplacement des données
│   ├── pkl/    # Dossier généré après génération des .pkl (pkl_gen.py)
│   │   ├── dbscan.pkl
│   │   └── kmeans.pkl
│   ├── .dockerignore
│   ├── config.py    # Config pour le backend (emplacement des données, etc.)
│   ├── Dockerfile
│   ├── main.py    # API
│   ├── pkl_gen.py    # Script à exécuter pour générer les modèles .pkl
│   ├── plotting.py    # Fonctions de génération des plots pour chaque modèle
│   ├── processing.py    # Fonction de processing des données
│   ├── scoring.py    # Fonctions de scoring (silhouette score) pour chaque modèle
│   ├── requirements.txt
│   ├── spec.md    # Spécifications de l'API
│   └── testing.py    # Fonctions de test avant déploiement
│
├── frontend/
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── .gitignore
├── deploy-aci.yaml    # Configuration de l'instance de conteneurs Azure (utilisé par le workflow)
└── README.md
```

### Prérequis en local

1 / Avant de démarrer le projet, il est nécessaire d'installer certaines dépendances sur l'environnement de travail. Pour effectuer ces installations, vous pouvez éxécuter la commande suivante :

```bash
pip install -r backend/requirements.txt
```

2 / Depuis le terminal, placez-vous dans le dossier backend/, générez les modèles .pkl en exécutant le script :
```bash
python pkl_gen.py
```

3 / Depuis le terminal, lancer l'API en se plaçant dans le dossier backend/ et en exécutant :
```bash
python main.py
```
Penser à changer l'API_PATH dans le script.js, en local il devrait s'agir de :

const API_PATH = "http://localhost:8002"

4 / Depuis le terminal, se placer dans le dossier *frontend/* et exécuter cette ligne de commande :
```bash
python -m http.server 8001
```

5 / Se rendre à l'adresse http://localhost:8001 pour consulter la page et communiquer avec l'API.

### Procédure de déploiement sur Azure