class Product:
    def __init__(self, cost, price, mark):
        self.cost = cost
        self.price = price
        self.mark = mark

class Meubles(Product):
    def __init__(self, cost, price, mark, materiau, couleur, dimensions):
        super().__init__(cost, price, mark)
        self.materiau = materiau
        self.couleur = couleur
        self.dimensions= dimensions

class Canape(Product):
    def __init__(self, cost, price, mark, materiau, couleur, dimensions):
        super().__init__(cost, price, mark)
        self.materiau = materiau
        self.couleur = couleur
        self.dimensions= dimensions

class Chaise(Product):
    def __init__(self, cost, price, mark, materiau, couleur, dimensions):
        super().__init__(cost, price, mark)
        self.materiau = materiau
        self.couleur = couleur
        self.dimensions= dimensions

class Table(Product):
    def __init__(self, cost, price, mark, materiau, couleur, dimensions):
        super().__init__(cost, price, mark)
        self.materiau = materiau
        self.couleur = couleur
        self.dimensions= dimensions
