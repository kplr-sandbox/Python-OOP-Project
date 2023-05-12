class Product:
def __init__(self, cost, price, marque):

    self.cost = cost
    self.price = price

        self.marque = marque

# Setter

    def set_cost(self,cost):

        self.cost=cost

    def set_price(self,price):

        self.price=price

    def set_marque(self,marque):

        self.marque=marque

# Getter

    def get_cost(self):

        return self.cost

    def get_price(self):

        return self.price

    def get_marque(self):

        return self.marque

   

# Fonctions génériques

    def __str__(self):

        return f"au prix de {self.get_price()} pour un cout de fabrication {self.get_cost()} de la marque {str(self.get_marque())}"





class Meubles(Product):

    def __init__(self, cost, price, marque,materiaux,couleur,hauteur,largeur,longueur):

        super().__init__(cost, price, marque)

        self.materiaux=materiaux

        self.couleur=couleur

        self.hauteur=hauteur

        self.largeur=largeur

        self.longueur=longueur

# Setter

    def set_materiaux(self,materiaux):

        self.materiaux=materiaux

    def set_couleur(self,couleur):

        self.couleur=couleur

    def set_hauteur(self,hauteur):

        self.hauteur=hauteur

    def set_largeur(self,largeur):

        self.largeur=largeur

    def set_longueur(self,longueur):

        self.longueur=longueur

# Getter

    def get_materiaux(self):

        return self.materiaux

    def get_couleur(self):

        return self.couleur

    def get_hauteur(self):

        return self.hauteur

    def get_largeur(self):

        return self.largeur

    def get_longueur(self):

        return self.longueur

# Fonctions génériques

    def __str__(self):

        return f"{super().__str__()} de dimension {self.get_hauteur()}x{self.get_largeur()}x{self.get_longueur()} de couleur {self.get_couleur()} fabriqué avec {self.get_materiaux()}"




class Canape(Meubles):

# Fonctions génériques

    def __str__(self):

        return f"c'est un canapé {super().__str__()}"

   

class Table(Meubles):

# Fonctions génériques

    def __str__(self):

        return f"c'est une table {super().__str__()}"




class Chaise(Meubles):

# Fonctions génériques

    def __str__(self):

        return f"c'est une chaise {super().__str__()}"




def main():

    mobilier=[Canape(1000,2000,"OKLM","Cuir","Blanc",200,100,80),

              Canape(800,1600,"SIESTA","Tissu","Bleu",150,90,70),

              Chaise(50,100,"PEPOUSE","Plastique","Rouge",50,50,70),

              Chaise(75,150,"PEPOUSE","Métal","Gris",60,60,80),

              Table(250,500,"TEX","Bois","Chêne",150,80,75),

              Table(350,700,"TEX","Verre","Transparent",120,60,75)]




# Parcours du mobilier

    for meuble in mobilier:

        print(meuble)





main()