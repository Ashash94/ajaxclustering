# SIMPLON DEV IA | Brief 15

## AJAX Clustering

### Contexte

En tant que développeur IA, je veux :<br>
    - Développer un back-end avec les modèles proprement dits, et plusieurs modalités de clustering<br>
    - Spécifier la façon par laquelle mon programme peut interagir avec ce back<br>
    - Développer un front-end permettant de changer les paramètres en utilisant AJAX<br>

### Data

[Lien vers les données à utiliser](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

### Structure du projet

```bash
project/
│
├── backend/
│   ├── data/
│   │   └── mall_customers.csv    # Emplacement des données (à télécharger)
│   ├── config.py    # Config pour le backend (emplacement des données, etc.)
│   ├── main.py    # API
│   ├── models.py    # Fonctions des modèles de clustering
│   ├── plots.py    # Fonctions de plotting des différents modèles
│   ├── processing.py    # Fonction de processing des données
│   ├── requirements.txt
│   └── spec.md    # Spécifications de l'API
│
├── frontend/
│   ├── assets/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── .gitignore
└── README.md
```

### Prérequis

Avant de démarrer le projet, il est nécessaire d'installer certaines dépendances sur l'environnement de travail. Pour effectuer ces installations, vous pouvez éxécuter la commande suivante :
```bash
pip install -r backend/requirements.txt
```
Vous devrez aussi télécharger les données (voir partie *Data*) et placer le .csv obtenu dans un dossier data/, dans le backend du projet (voir partie *Structure du projet*).

### Procédure

1 / Depuis le terminal, se placer dans le dossier frontend/ et exécuter cette ligne de commande :
```bash
python -m http.server 8001
```
2 / Depuis le terminal, lancer l'API en se plaçant dans le dossier backend/ et en exécutant :
```bash
python main.py
```
Par défaut, le port 8000 sera utilisé pour l'API, penser à changer l'API_PATH dans le script.js dans le cas contraire.<br><br>
3 / Se rendre à l'adresse http://localhost:8001 pour consulter la page et communiquer avec l'API.
