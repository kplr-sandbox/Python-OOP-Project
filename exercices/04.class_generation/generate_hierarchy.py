from generator.generate_class_def import generate_class_def 
import os
import json
from unidecode import unidecode
import re

def generate_class_hierarchy(json_dict :dict, superclass_name:str=None,superclass_args:list=[]):
    class_defs = ""

    for class_name, class_attrs in json_dict.items():

        class_def = generate_class_def(class_name, class_attrs, superclass_name,superclass_args)
        class_defs += class_def

        if "subclasses" in class_attrs:
            super_attr = (list(class_attrs.keys())+superclass_args)
            super_attr.remove("subclasses")
            subclass_defs = generate_class_hierarchy(class_attrs["subclasses"], class_name, super_attr)
            class_defs += subclass_defs

    return class_defs

# Charger des données JSON à partir du fichier dans un dictionnaire python
local_path = os.path.dirname(os.path.abspath(__file__))
json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))

# Reconvertir le dictionnaire en chaine de caractere pour le traiter ensuite
json_str = json.dumps(json_data)

# Utilisation de la fonction unidecode pour enlever les accents et autres caractères spéciaux
json_data = (unidecode(json_str))

# Conversion de la chaine de caractere JSON à nouveau en dictionnaire Python
# Le dictionnaire python est plus pratique à manipuler que la chaine de caractère car il est structuré
json_dict = json.loads(json_data)

# Appeler la méthode generate_class_hierarchy pour générer le code des classes automatiquement en se basant sur le dictionnaire json_dict
generate_class_hierarchy (json_dict)
# Stocker le résultat de la classe dans une variable

class_defs=generate_class_hierarchy(json_dict)
print(class_defs)