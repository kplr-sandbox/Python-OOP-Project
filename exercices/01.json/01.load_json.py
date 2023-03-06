# Import des modules nécessaires
import json
from unidecode import unidecode
import re

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

"""
Le code ci-dessus charge des données JSON à partir d'un fichier, les convertit en un dictionnaire Python, puis effectue des manipulations sur ce dictionnaire.
Voici les étapes détaillées :
1.	Le module json est importé pour manipuler des données JSON. Les modules re et unidecode sont importés pour la suppression des caractères spéciaux.
2.	Les données JSON sont chargées à partir du fichier "_exercices/01.json/json_data.json" dans un dictionnaire Python à l'aide de la fonction json.load().
3.	Le dictionnaire Python est converti en une chaîne de caractères JSON à l'aide de la fonction json.dumps().
4.	La fonction unidecode() est utilisée pour enlever les accents et autres caractères spéciaux de la chaîne de caractères JSON.
5.	La chaîne de caractères JSON est à nouveau convertie en un dictionnaire Python à l'aide de la fonction json.loads().
6.	Le dictionnaire Python résultant peut ensuite être manipulé et utilisé dans le code.
En résumé, ce code permet de charger des données JSON à partir d'un fichier, de les convertir en dictionnaire Python et de les nettoyer de certains caractères spéciaux avant de pouvoir les manipuler plus facilement dans le reste du programme.
."""

"""
imprimons a présent le dictionnaire
"""
print(json.dumps(json_dict, indent=4))
