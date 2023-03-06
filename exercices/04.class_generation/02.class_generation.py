def generate_class_def(nom_classe: str, attributs: dict, nom_superclasse: str, args_superclasse: list = []) -> str:
    # Cette fonction génère une définition de classe Python à partir des paramètres passés et retourne une chaîne de caractères représentant la définition de classe générée.
    """
    `nom_classe`: une chaîne de caractères représentant le nom de la classe à générer.
    `attributs`: un dictionnaire représentant les attributs de la classe, où les clés sont les noms des attributs et les valeurs sont les types des attributs.
    `nom_superclasse`: une chaîne de caractères représentant le nom de la superclasse éventuelle. Si la classe n'a pas de superclasse, on peut passer une chaîne vide en argument.
    `args_superclasse`: une liste de chaînes de caractères représentant les arguments à passer au constructeur de la superclasse éventuelle. Si la classe n'a pas de superclasse, on peut passer une liste vide en argument.

    La fonction retourne une chaîne de caractères représentant le code source de la classe.
    """

    # Initialisation des variables
    """
    On commence par initialiser plusieurs variables utiles pour la suite de la fonction :

    `args_constructeur`: une liste des noms des arguments à passer au constructeur de la classe.
    `definition_constructeur`: une chaîne de caractères représentant la définition du constructeur de la classe, à remplir au fur et à mesure qu'on parcourt les attributs.
    `has_attributs`: un booléen qui permet de savoir si la classe a des attributs ou non.

    """
    args_constructeur = [] # une liste qui stocke les noms des attributs qui seront utilisés pour créer le constructeur
    definition_constructeur = "" # une chaîne de caractères qui stocke le code qui sera utilisé pour initialiser les attributs de la classe
    has_attributs = False # un booléen qui vérifie si la classe a des attributs ou non
    modele_classe = f"class {nom_classe}" # une chaîne de caractères qui stocke la définition de base de la classe

    """
    Si la classe a une superclasse, celle-ci est spécifiée dans la définition. 
    La chaîne de caractères est stockée dans la variable modele_classe.
    """
    # Gestion de la superclasse
    if nom_superclasse: # si la classe a une superclasse
        modele_classe += f"({nom_superclasse})" # ajouter la superclasse à la définition de la classe

    modele_classe += ":\n" # ajouter une nouvelle ligne à la définition de la classe
    """
    Ensuite, la fonction parcourt les attributs de la classe. 
    Pour chaque attribut, elle ajoute le nom de l'attribut à la liste args_constructeur et construit 
    une ligne de code de la forme `self.nom_attribut = nom_attribut` pour la définition du constructeur.     
    """
    # Gestion des attributs
    for nom_attribut in attributs.keys(): # pour chaque attribut dans le dictionnaire d'attributs
        if nom_attribut != "subclasses": # si l'attribut n'est pas une sous-classe
            has_attributs = True # la classe a des attributs
            args_constructeur.append(nom_attribut) # ajouter le nom de l'attribut à la liste des arguments du constructeur
            definition_constructeur += f"\n\t\tself.{nom_attribut} = {nom_attribut}" # ajouter une ligne au code de définition du constructeur pour initialiser l'attribut

    """
    Si l'attribut est `name` et que la classe est une classe `Product`, 
    la fonction ajoute également une ligne de code pour initialiser `self.name` avec le nom de la classe. 
    """
    # Gestion du nom de la classe si c'est une classe Product
    if nom_classe == "Product": # si la classe est de type Product
        definition_constructeur += "\n\t\tself.name=type(self).__name__" # ajouter une ligne au code de définition du constructeur pour initialiser le nom de la classe

    """
    Si la classe a des attributs:
    la fonction construit une chaîne de caractères représentant le constructeur de la classe en utilisant les arguments fournis. 
    La chaîne de caractères est stockée dans la variable `modele_constructeur`.
    """
    # Gestion du constructeur
    if has_attributs: # la classe a des attributs
        modele_constructeur = f"\tdef __init__(self, {', '.join(args_constructeur + args_superclasse)}):" # créer la signature du constructeur en incluant les arguments des attributs et les arguments de la superclasse

        if len(args_superclasse) > 0: # si la superclasse a des arguments
            modele_constructeur += f"\n\t\tsuper().__init__({', '.join(args_superclasse)})" # ajouter une ligne pour initialiser la superclasse

        modele_constructeur += definition_constructeur # ajouter le code d'initialisation des attributs à la définition du constructeur
   
        """
        Si la classe n'a pas d'attributs:
        la fonction construit une chaîne de caractères représentant le constructeur de la classe 
        en utilisant uniquement les arguments de la superclasse (s'il y en a). 
        La chaîne de caractères est stockée dans la variable modele_constructeur.
        """
    else: # la classe n'a pas d'attributs
        if len(args_superclasse) > 0: # si la superclasse a des arguments
            modele_constructeur = f"\tdef __init__(self, {', '.join(args_superclasse)}):" # créer la signature du constructeur en incluant les arguments de la superclasse
            modele_constructeur += f"\n\t\tsuper().__init__({', '.join(args_superclasse)})"
      
        else:    
            modele_constructeur = "\tpass"
    
    """
    On retourne une chaîne de caractères qui représente le code source complet de la classe, 
    en utilisant les chaînes de caractères stockées précédemment dans modele_classe et `modele_constructeur`.
    """
    return modele_classe + modele_constructeur + "\n\n"

"""
Code de Test / Exemple d'utilisation :
Ce code génère la définition de la classe Voiture, qui hérite de la classe Vehicule et possède deux attributs, moteur et . 
Le constructeur de la classe prend en argument moteur, nbportes, marque et modele, ainsi que les arguments de la superclasse Vehicule. 
La variable code_classe contient le code source généré par la fonction generate_class_def
"""
def test_fonction():
    
    attributs = {
    "moteur": "str",
    "nbportes": "int"
    }

    code_classe = generate_class_def("Voiture", attributs, "Vehicule", ["marque", "modele"])
    print(code_classe)

if __name__ == '__main__':
    # Appeler la fonction principale
    test_fonction()