# API

Dans le cadre de l'analyse de donnée des clients d'un centre commercial, nous utilisons les modèles de clusterisations suivants : K-Means et DBSCAN.

### Modèles utilisés

Le clustering est une méthode de Machine Learning non supervisée qui repère des similarités dans les données pour pouvoir ensuite les structurer.

** KMeans ** : Un algorithme qui permet de regrouper des individus sans a priori et d'établir une moyenne de référence parmi un jeu de données. L’idée est alors de définir un profil type qui pourra toucher le plus grand nombre.

** DBSCAN ** : Un algorithme se base sur la distance et la densité des clusters pour effectuer des sous-groupes. De son côté, le spectral clustering se base sur la similarité des données.

### Indicateur de performance

Afin que l'on puisse comparer la performance de chacun des modèles précédemment évoqués. On fait appel à la métrique *Silhouette Score* mesure à quel point les échantillons d'un même cluster sont proches les uns des autres par rapport aux échantillons des autres clusters. 
Un score de silhouette proche de 1 indique que les échantillons sont bien regroupés, -1 indique un mauvais regroupement et 0 indique un chevauchement de clusters.

### Endpoints 

**"/k-means/score"** : Ce endpoint renvoie le silhouette score du modèle KMeans dans un format .json 
**"/k-means/plot"** : Ce endpoint renvoie une image du graphique en nuage de point du modèle KMeans dans un format .png 

**"/dbscan/score"** : Ce endpoint renvoie le silhouette score du modèle DBSCAN dans un format .json 
**"/dbscan/plot"** : Ce endpoint renvoie une image du graphique en nuage de point du modèle DBSCAN dans un format .png