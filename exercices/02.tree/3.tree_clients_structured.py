# A présent organisons un peu le code. 
# Nous allons utiliser des méthodes et fonctions pour isolers les modules

"""Ce code est un exemple d'utilisation de fonctions et de méthodes pour organiser le code et le rendre plus lisible. 
- Il utilise les modules json, unidecode et treelib.

- La fonction `json_dict_from_file()` est utilisée pour charger les données JSON à partir d'un fichier et les convertir en un dictionnaire Python structuré. 
Cette fonction utilise les modules json et unidecode pour effectuer cette conversion. La fonction retourne le dictionnaire Python.

- La fonction `create_tree_from_dict()` est utilisée pour créer un arbre treelib à partir d'un dictionnaire Python. 
Cette fonction prend en entrée l'arbre treelib, l'identifiant du noeud parent et le dictionnaire Python à partir duquel l'arbre doit être créé. Cette fonction utilise une approche récursive pour parcourir le dictionnaire et ajouter chaque élément en tant que noeud dans l'arbre treelib.

- La méthode `main()` est utilisée pour appeler les fonctions json_dict_from_file() et create_tree_from_dict() 
et afficher l'arbre treelib résultant.

- La condition if __name__ == '__main__': est utilisée pour s'assurer que le script est exécuté en tant que programme principal, 
et non importé en tant que module dans un autre script Python.

En résumé, ce code 
     - charge des données JSON à partir d'un fichier, 
     - les convertit en un dictionnaire Python structuré, 
     - crée un arbre treelib à partir de ce dictionnaire 
     - et affiche l'arbre dans la console.
"""
# Import des modules nécessaires
import json
from unidecode import unidecode
from treelib import Tree
import os

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

def create_tree_from_dict(tree, parent_node_id, parent_dict):
    """
    Cette fonction crée un arbre à partir d'un dictionnaire.
    Elle est appelée récursivement pour chaque sous-dictionnaire.

    Args:
        tree (Tree): un objet Tree de la bibliothèque treelib pour représenter l'arbre
        parent_node_id (str): l'identifiant du noeud parent dans l'arbre
        parent_dict (dict): le dictionnaire Python contenant les données à insérer dans l'arbre
    """
    for key, value in parent_dict.items():
        if isinstance(value, dict):
            # Créer un nouveau noeud pour la clé courante du dictionnaire
            new_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)
            
            # Créer récursivement le sous-arbre pour le dictionnaire courant
            create_tree_from_dict(tree, new_node_id, value)
        else:
            # Créer un nouveau noeud pour la feuille courante du dictionnaire
            leaf_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=f"{key}: {value}", identifier=leaf_node_id, parent=parent_node_id)

def main():
    """
    Cette fonction est la fonction principale qui orchestre toutes les autres.
    Elle charge les données JSON depuis un fichier, crée un objet Tree de la bibliothèque treelib,
    et crée un arbre à partir des données JSON.

    Elle affiche ensuite l'arbre créé.
    """
    my_tree = Tree()
    # Créer le noeud racine pour l'arbre
    my_tree.create_node(tag="Racine", identifier="racine")

    # Charger les données JSON depuis un fichier et créer la structure de l'arbre à partir du dictionnaire
    json_dict = json_dict_from_file()
    create_tree_from_dict(my_tree, "racine", json_dict)

    # Afficher l'arbre
    my_tree.show()

if __name__ == '__main__':
    # Appeler la fonction principale
    main()
