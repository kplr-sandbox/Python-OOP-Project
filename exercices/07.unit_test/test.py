#Importer les bibliothèques nécessaires
import sys
import unittest
sys.path.extend(['.','..'])

#Import des classes à tester
from classes.product_classes import Chaise, Pantalon
from inventory.stock_manager import InventoryManager

#Définition de la classe de test
class TestInventoryManager(unittest.TestCase):
    """
    Méthode setUp est une méthode spéciale dans le module unittest de Python.
    Elle est appelée avant chaque méthode de test définie dans une classe de test et sert à mettre en place l'état initial pour les tests.
    Elle est utilisée pour initialiser des objets que les méthodes de test vont utiliser.
    """
    def setUp(self):
        # Instanciation de l'objet InventoryManager
        self.inventory_manager = InventoryManager()
        # Instanciation d'objets Chaise et Pantalon pour les tests
        self.chaise = Chaise("materiau2", "couleur2", "dimension2", 50, 100, "Ikea")
        self.pantalon = Pantalon("M", "noir", "jeans", 150, 200,"Zara")

    # Test de la méthode add_product de la classe InventoryManager
    def test_add_product(self):
        
         """
         -Ajout de 5 chaises à l'inventaire en utilisant la méthode add_product
         -Vérification que la chaise a bien été ajoutée à l'inventaire avec la méthode assertIn ( assertIn(argument1, argument2) )
         -assertIn est une méthode fournie par le module unittest de Python qui vérifie si le premier argument est contenu dans le second argument.
        """

    # Test de la méthode remove_product de la classe InventoryManager
    def test_remove_product(self):
        
         """
         -Ajout de 5 pantalons à l'inventaire en utilisant la méthode add_product
         -Suppression le pantalon de l'inventaire en utilisant la méthode remove_product
         -Vérification que le pantalon a bien été supprimé de l'inventaire avec la méthode assertNotIn ( assertNotIn(argument1, argument2) )
         -assertNotIn est une méthode qui permet de vérifier si un élément n'est pas présent dans une séquence
        """
    # Test de la méthode sell_product de la classe InventoryManager
    def test_sell_product(self):
        """
         -Ajout de 5 pantalons à l'inventaire
         -Vente de 2 pantalons en utilisant la méthode sell_product
         -Vérification que le nombre de pantalons en stock a bien été mis à jour avec la méthode assertEqual
         - La méthode assertEqual prend deux arguments, les valeurs attendue et observée, et vérifie si les deux sont égaux. 
           Si les deux valeurs sont égales, le test réussit. Sinon, il échoue et affiche un message d'erreur indiquant les valeurs attendue et observée.
        """  
        
        
    # Test de la méthode restock_product de la classe InventoryManager
    def test_restock_product(self):
         """
         -Ajout de 10 chaises à l'inventaire
         -Réapprovisionnement (restocker) de 5 chaises en utilisant la méthode restock_product
         -Vérification que le nombre de chaises en stock a bien été mis à jour avec la méthode assertEqual
        """
        
    # Test de la méthode get_product de la classe InventoryManager
    def test_get_product(self):
        
         """
         -Ajout de 5 chaises à l'inventaire
         -Récupération de la chaise ajoutée précédemment en utilisant la méthode get_product
         -Vérification que la chaise récupérée est bien celle ajoutée précédemment avec la méthode assertEqual
         """
    # Test de la méthode list_products de la classe InventoryManager
    def test_list_products(self):
        """ 
        - Ajout de 5 chaises et de 10 pantalons à l'inventaire
        - Lister les produits existants dans l'inventaire en utilisant la méthode list_products et stocker le résultat dans une variable
        - Définir une variable qui contient la sortie attendue qui sera  "Chaise (Ikea): 5 in stock,  price:100"
        - Vérification que le premier résultat de la méthode list_products égal à la sortie attendue
        """
        
# Exécuter le code     
if __name__ == '__main__':
    unittest.main()

        
