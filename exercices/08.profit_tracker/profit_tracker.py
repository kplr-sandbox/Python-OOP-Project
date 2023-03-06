# La classe ProfitTracker est utilisée pour suivre les profits du magasin.

class ProfitTracker:

    # Le constructeur initialise la variable balance (solde)
    def __init__(self):
        # Créer une variable 'balance' et l'initialiser à 1000 euros

    #Méthode buy_product 
    """   
    La méthode buy_product est utilisée pour acheter un produit et mettre à jour le coût total et le solde.
    """     
    def buy_product(self, product: Product, quantity): 
        """
        Vérifie si le solde est suffisant pour acheter la quantité demandée de produit
            Si le solde est insuffisant:
                affiche un message d'erreur 
                retourne False pour indiquer que l'achat a échoué.
            Sinon, si le solde est suffisant:
                met à jour le solde en soustrayant le coût du produit multiplié par la quantité achetée
                retourne True pour indiquer que l'achat a réussi
        """
        
    #Méthode sell_product 
    """   
    La méthode sell_product est utilisée pour vendre un produit et mettre à jour le solde.
    """  
 
    def sell_product(self, product: Product, quantity):
        
        # Met à jour le solde en ajoutant le prix du produit multiplié par la quantité vendue


