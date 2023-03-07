#2. Définissez la classe Product avec ses attributs cost, price, et marque dans la méthode init.
#3. Définissez la classe Meubles en tant que sous-classe de la classe Product, en utilisant le mot-clé "class Meubles(Product):".
#4. Définissez la méthode init de la classe Meubles en appelant la méthode init de la classe parent avec le super().init(cost, price, marque).
#5. Ajoutez les attributs spécifiques à la classe Meubles, tels que les matériaux, la couleur et les dimensions.
#6. Répétez les étapes 3 à 5 pour les classes Canape, Chaise et Table.
#7. Vous pouvez maintenant utiliser ces classes pour créer des instances de meubles spécifiques dans votre programme principal.

class Product:
    def __init__(self,cost,price,marque):
        self.cost = cost
        self.price = price
        self.marque = marque

"""class Meubles(Product):
    def __init__(self,cost,price,marque,matériaux,couleur,dimensions):
        super().__init__(cost,price,marque)
        self.matériaux = matériaux
        self.couleur = couleur
        self.dimensions = dimensions

class Canape(Product):
    def __init__(self,cost,price,marque,matériaux,couleur,dimensions):
        super().__init__(cost,price,marque)
        self.matériaux = matériaux
        self.couleur = couleur
        self.dimensions = dimensions

class Chaise(Product):
    def __init__(self,cost,price,marque,matériaux,couleur,dimensions):
        super().__init__(cost,price,marque)
        self.matériaux = matériaux
        self.couleur = couleur
        self.dimensions = dimensions"""


class Table(Product):
    def __init__(self,cost,price,marque,matériaux,couleur,dimensions):
        super().__init__(cost,price,marque)
        self.matériaux = matériaux
        self.couleur = couleur
        self.dimensions = dimensions


# On peut aussi définir les classes Canape, Chaise et Table comme sous-classe de Meubles : 
# (en rajoutant d'autres arguments spécifiques)

class Canape(Meubles):
    def __init__(self,cost,price,marque,matériaux,couleur,dimensions,nom):   #nb_places
        super().__init__(cost,price,marque,matériaux,couleur,dimensions)
        self.nom = nom   # self.nb_places = nb_places 

class Chaise(Meubles):
    def __init__(self,cost, price, marque, matériaux, couleur, dimensions, nom):  #usage
        super().__init__(cost,price,marque, matériaux, couleur, dimensions)
        self.nom = nom   # self.usage = usage

class Table(Meubles):
    def __init__(self,cost,price,marque,matériaux,couleur,dimensions):            #forme
        super().__init__(cost,price,marque,matériaux,couleur,dimensions)
                         # self.forme = forme


# - Créez les instances suivantes :
            
canape1 = Canape(1000,2000,"OKLM","Cuir","Blanc", "200x100x80","Canape")
        
canape2 = Canape(800,1600,"SIESTA","Tissu","Bleu", "150x90x70","Canape")

chaise1 = Chaise(50, 100, "PEPOUSE", "Plastique", "Rouge", "50x50x70","Chaise")

chaise2 = Chaise(75, 100, "PEPOUSE", "Métal", "Gris", "60x60x80", "Chaise")

table1 = Table(350, 700, "TEX", "Verre", "Transparent", "120x60x75")

print("\n=====")
print(canape1.cost,canape1.marque,canape1.price)
