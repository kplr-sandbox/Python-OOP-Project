"""
A présent rajoutons une méthode afficher attributs dans chaque classe
"""

class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    
    def afficher_attributs(self):
        print("Attributs pour le véhicule :")
        print("- Marque :", self.marque)
        print("- Modèle :", self.modele)
        print("- Année :", self.annee)

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, nb_portes):
        super().__init__(marque, modele, annee)
        self.nb_portes = nb_portes
    
    def afficher_attributs(self):
        super().afficher_attributs()
        print("- Nombre de portes :", self.nb_portes)

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, nb_roues):
        super().__init__(marque, modele, annee)
        self.nb_roues = nb_roues
    
    def afficher_attributs(self):
        super().afficher_attributs()
        print("- Nombre de roues :", self.nb_roues)

# Création d'une instance de chaque classe
voiture1 = Voiture("Renault", "Clio", 2018, 5)
moto1 = Moto("Yamaha", "MT-07", 2020, 2)

# Appel de la méthode afficher_attributs pour chaque instance
voiture1.afficher_attributs()


moto1.afficher_attributs()

"""
Dans cet exemple, la méthode afficher_attributs est incluse dans la classe Vehicule. 
Elle affiche les attributs communs (marque, modele et annee) pour chaque instance de la classe.

Les méthodes afficher_attributs dans les classes Moto et Voiture redéfinissent la méthode de la classe mère 
et appellent la méthode afficher_attributs de la classe mère à l'aide de la fonction super() pour afficher les attributs communs. 

Ensuite, elles affichent les attributs spécifiques de chaque classe fille (nb_portes pour la classe Voiture et nb_roues pour la classe Moto).
Enfin, on crée une instance de chaque classe (voiture1 et moto1) et on appelle la méthode afficher_attributs pour afficher les attributs et leurs valeurs pour chaque instance. 
Notez que l'appel de la méthode est identique pour chaque classe (voiture1.afficher_attributs() et moto1.afficher_attributs()), 
car la méthode est maintenant définie dans la classe mère."""