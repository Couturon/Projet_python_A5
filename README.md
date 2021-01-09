# Projet_python_A5
Ce git hub contient un projet permettant de déterminer si un client va passer une commande sur un site de e-commerce à l'aide de modèles de machine learning.
Pour cela, ce projet s'appuie sur le dataset Online Shoppers Purchasing Intention Dataset que vous pourrez retrouver sur ce lien : https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset.

Le fichie PDF contient un power point décrivant les tenants et aboutissant du problème et des reflexions autour du dataset.

Le fichier Python_data_projet_undersampling.ipynb contient le projet en tant que tel. Il commence par la visualisation des données afin de les comprendre, leur traitement pour pouvoir les utiliser avec des modèles de machine learning et pour finir les modèles eux-mêmes. Trois modèles différents ont été testés : 
  - Un modèle de régression logistique 
  - Un modèle random forest 
  - Un modèle XGBoost 

Pour finir le répertoire API flask contient une API fait avec flask permettant de tester les modèles random forest et XGBoost. Chacun des deux modèles ont été télécharger précédemment et mis dans le répertoire "models". Pour lancer l'API, il vous suffit de lancer le fichier app.py dans un invite de commande. Ensuite pour tester le modèle, vous pouvez exécuter le fichier request.py dans un autre invite de commande. Il prend en argument les informations d'un clients et renvoie comme réponse si celui-ci va passer une commande ou non. Pour changer le modèle utiliser dans l'API, il faut le changer dans le fichier app.py.

Merci de m'avoir lu !
