- Nous allons a présent charger de nouvelles données,
- prenez le temps de lire ATTENTIVEMENT le contenu du nouveau fichier json_data
- En utilisant le code précédemment réalisé, générez un arbre qui en affiche le contenu
- Attention : N'afficher que les Noeuds possédant des sous-classes
- Autrement dit, il ne faut pas inclure les attributs des Produits, mais seulement les catégories de produit.
- Pour ce faire, il ne faut inclure que les noeuds qui ne sont pas terminaux
- Les noeuds sans enfants doivent être skippés.

- voici le Pseudo code pour vous aider à rédiger le code.

```
# Import des modules nécessaires
import json
from unidecode import unidecode
from treelib import Tree

# Fonction pour charger les données JSON depuis un fichier et les convertir en dictionnaire Python
la fonction json_dict_from_file() reste inchangée.

# Fonction pour créer un arbre à partir d'un dictionnaire Python
def create_tree_from_dict(json_dict):
    Créer un nouvel arbre
    Créer le noeud racine de l'arbre
    Parcourir récursivement le dictionnaire Python pour créer les noeuds de l'arbre (fonction ci dessous)
    Retourner l'arbre

# Fonction récursive pour parcourir un dictionnaire Python et créer des noeuds dans un arbre
def recusive_tree_from_json(json_dict, parent_node_id):

    Pour chaque clé (class_name) et valeur (class_attrs) dans le dictionnaire :
        Créer un nouveau noeud pour la clé courante du dictionnaire (nom de la classe)
        Ajouter le nouveau noeud en tant que fils du noeud parent

        Si "subclasses" est dans les attributs de la classe en cours (soit : valeur(class_attrs))
            Appeler récursivement la fonction pour créer les sous-noeuds de ce dictionnaire

# Fonction principale
def main():
    Charger les données JSON depuis un fichier et créer la structure de l'arbre à partir du dictionnaire
    Créer l'arbre à partir du dictionnaire Python
    Afficher l'arbre de classes

# Code principal
if __name__ == '__main__':
    Appeler la fonction principale

```

Output:

```
Product Classes Hierarchy
└── Product
    └── Biens Consommation
        ├── Articles Menagers
        │   ├── Appareils Electromenagers
        │   │   ├── Lave-linge
        │   │   ├── Lave-vaisselle
        │   │   └── Refrigerateur
        │   ├── Meubles
        │   │   ├── Canape
        │   │   ├── Chaise
        │   │   └── Table
        │   └── Ustensiles Cuisine
        │       ├── Batterie Cuisine
        │       └── Casserole
        └── Habillement
            ├── Casquette
            ├── Chaussures
            └── Vetements
                ├── Haut
                ├── Pantalon
                └── Robe
```
