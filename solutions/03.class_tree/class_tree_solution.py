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

def create_tree_from_dict(json_dict):
    # define the tree
    global tree 
    tree = Tree()

    # define the root node
    root_node_id = "root"
    root_node_name = "Product Classes Hierarchy"
    tree.create_node(root_node_name, root_node_id)

    #traverse json data and creathe other node
    recusive_tree_from_json(json_dict, root_node_id)

    return tree

def recusive_tree_from_json(json_dict, parent_node_id):
    for class_name, class_attrs in json_dict.items():            
            class_node_id = class_name
            class_node_name = class_name

            # Add the class node to the tree
            tree.create_node(class_node_name, class_node_id, parent=parent_node_id)

            # Traverse any subclasses
            if "subclasses" in class_attrs:
                recusive_tree_from_json(class_attrs["subclasses"], class_node_id)

def main():
    
    # Charger les données JSON depuis un fichier et créer la structure de l'arbre à partir du dictionnaire
    json_dict = json_dict_from_file()
    my_tree = create_tree_from_dict(json_dict)

    # Afficher l'arbre
    my_tree.show()

if __name__ == '__main__':
    # Appeler la fonction principale
    main()
