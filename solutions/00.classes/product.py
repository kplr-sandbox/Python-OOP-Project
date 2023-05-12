class Product:
    def __init__(self, cost, price, brand):
        self.cost = cost
        self.price = price
        self.brand = brand

    def screen_attributs(self):
        print("Attributs pour le produit :")
        print("- Coût : ", self.cost)
        print("- Prix : ", self.price)
        print("- Marque : ", self.brand)

class Meubles(Product):
    def __init__(self, cost, price, brand, color, materials, dimension, name):
        super().__init__(cost, price, brand)
        self.color = color
        self.materials = materials
        self.dimension = dimension
        self.name = name
    
    def screen_attributs(self):
        super().screen_attributs()
        print("- Couleur :", self.color)
        print("- Materiaux :", self.materials)
        print("- Dimensions :", self.dimension)
        print("- Nom du meuble :", self.name)

class Canape(Meubles):
    def __init__(self, cost, price, brand, color, materials, dimension, name):
        super().__init__(cost, price, brand, color, materials, dimension, name)

    def screen_attributs(self):
        super().screen_attributs()

class Chaise(Meubles):
    def __init__(self, cost, price, brand, color, materials, dimension, name):
        super().__init__(cost, price, brand, color, materials, dimension, name)

    def screen_attributs(self):
        super().screen_attributs()

class Table(Meubles):
    def __init__(self, cost, price, brand, color, materials, dimension, name):
        super().__init__(cost, price, brand, color, materials, dimension, name)

    def screen_attributs(self):
        super().screen_attributs()


Canape1 = Canape(1000, 2000, "OKLM", "Blanc", "Cuir", "200 x 100 x 80", "Canapé")
Canape2 = Canape(800, 1600, "SIESTA", "Bleu", "Tissu", "150 x 90 x 70", "Canapé")
Chaise1 = Chaise(50, 100, "PEPOUSE", "Rouge", "Plastique", "50 x 50 x 70", "Chaise")
Chaise2 = Chaise(75, 150, "PEPOUSE", "Gris", "Métal", "60 x 60 x 80", "Chaise")
Table2 = Table(250, 500, "TEX", "Chêne", "Chêne", "150 x 80 x 75", "Table")
Table1 = Table(350, 700, "TEX", "Transparent", "Verre", "120 x 60 x 75", "Table")