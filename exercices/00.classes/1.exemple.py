class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, nb_portes):
        super().__init__(marque, modele, annee)
        self.nb_portes = nb_portes

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, nb_roues,cylindree):
        super().__init__(marque, modele, annee)
        self.nb_roues = nb_roues
        self.cylindree = cylindree

"""
Dans cet exemple, la classe 'Vehicule' est la classe mère qui définit les attributs de base pour tous les véhicules, 
à savoir la marque, le modèle et l'année. 

Les classes 'Voiture' et 'Moto' sont des classes enfant qui héritent de ces attributs de base, 
mais qui ont également leurs propres attributs spécifiques (nb_portes pour la classe Voiture et nb_roues pour la classe Moto).

Les constructeurs des classes enfants appellent la méthode super().__init__() pour appeler le constructeur de la classe mère 
et initialiser les attributs hérités. 

Ensuite, ils initialisent leurs propres attributs spécifiques.
"""

""""
Par exemple, pour créer une instance de la classe Voiture, vous pouvez utiliser la syntaxe suivante :
"""

voiture1 = Voiture("Renault", "Clio", 2018, 5)

"""
Ceci crée une instance de la classe Voiture avec les attributs suivants :

marque = "Renault"
modele = "Clio"
annee = 2018
nb_portes = 5
De même, pour créer une instance de la classe Moto, vous pouvez utiliser la syntaxe suivante :

"""

moto1 = Moto("Yamaha", "MT-07", 2020, 2,300)

"""
Ceci crée une instance de la classe Moto avec les attributs suivants :

marque = "Yamaha"
modele = "MT-07"
annee = 2020
nb_roues = 2
cylindree = 300
"""


