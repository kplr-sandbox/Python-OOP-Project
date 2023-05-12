class InventoryProductEntry:
	def __init__(self, product:Product, quantity):
		self.product = product
		self.quantity = quantity
		self.sales = 0
		self.expenses = 0

	def sell(self, quantity):
		if self.quantity < quantity:
			print(f"Le stock du produit {self.product.name} est insuffisant.")
			return False
		else:
			self.quantity -= quantity
			self.sales += quantity * self.product.price
			return True
				
	def restock(self, quantity):
		self.quantity += quantity
		self.expenses += quantity * self.product.cost

	def __repr__(self):
		return "{} ({}): {} in stock,  price:{}".format(type(self.product).__name__, self.product.marque, self.quantity, self.product.price)
