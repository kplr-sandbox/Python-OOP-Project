'''
- Nous allons a présent charger de nouvelles données,
- prenez le temps de lire ATTENTIVEMENT le contenu du nouveau fichier json_data
- En utilisant le code précédemment réalisé, générez un arbre qui en affiche le contenu
- Attention : N'afficher que les Noeuds possédant des sous-classes
- Autrement dit, il ne faut pas inclure les attributs des Produits, mais seulement les catégories de produit.
- Pour ce faire, il ne faut inclure que les noeuds qui ne sont pas terminaux
- Les noeuds sans enfants doivent être skippés.

- voici le Pseudo code pour vous aider à rédiger le code.

'''
# Import des modules nécessaires
import json
from unidecode import unidecode
from treelib import Tree
import os

''' Fonction pour charger les données JSON depuis un fichier et les convertir en dictionnaire Python
la fonction json_dict_from_file() reste inchangée.'''

# Fonction pour créer un arbre à partir d'un dictionnaire Python
def create_tree_from_dict(tree, parent_node_id, parent_dict):
    '''Créer un nouvel arbre
    Créer le noeud racine de l'arbre
    Parcourir récursivement le dictionnaire Python pour créer les noeuds de l'arbre (fonction ci dessous)
    Retourner l'arbre'''
    
                
'''            ew_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)
            
            # Créer récursivement le sous-arbre pour le dictionnaire courant
            if "subclasses" in value :
                create_tree_from_dict(tree, new_node_id, value["subclasses"])
        else:
            # Créer un nouveau noeud pour la feuille courante du dictionnaire
            leaf_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=f"{key}: {value}", identifier=leaf_node_id, parent=parent_node_id)
'''
def json_dict_from_file():
    """
    Cette fonction ouvre et charge les données JSON du fichier
    dans un dictionnaire Python.

    Returns:
        dict: le dictionnaire Python contenant les données JSON du fichier
    """
    # Get the directory path of the current Python file
    local_path = os.path.dirname(os.path.abspath(__file__))
    # Chargement des données JSON à partir du fichier dans un dictionnaire python
    json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
    
    # il est nécessaire de reconvertir le dictionnaire en chaine de caractere pour le traiter ensuite
    json_str = json.dumps(json_data)

    # Utilisation de la fonction unidecode pour enlever les accents et autres caractères spéciaux
    json_data = (unidecode(json_str))

    # Conversion de la chaine de caractere JSON à nouveau en dictionnaire Python
    # Le dictionnaire python est plus pratique à manipuler que la chaine de caractère car il est structuré
    json_dict = json.loads(json_data)

    return json_dict


#code principal main():
    '''Charger les données JSON depuis un fichier et créer la structure de l'arbre à partir du dictionnaire
    Créer l'arbre à partir du dictionnaire Python
    Afficher l'arbre de classes'''

# je crée le dictionnaire "nettoyé" à partir du Json

json_dict=json_dict_from_file()





'''Output:


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
'''