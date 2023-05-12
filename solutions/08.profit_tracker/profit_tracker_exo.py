class ProfitTracker:

	def __init__(self):		

		self.total_cost = 0
		self.balance= 1000

	def buy_product(self, product:Product,quantity):
		if self.balance < product.cost * quantity:
			print(f"Vous avez {self.balance} euros. Pour restocker {quantity} {product.name}, vous avez besoin de {product.cost * quantity} euros")
			return False
		else:
			self.balance= self.balance - (product.cost * quantity)
			print(f"balance après achat du produit {product.name} : {self.balance} euros")
			return True
	
	def sell_product(self, product:Product,quantity):
		self.balance= self.balance + (product.price * quantity)
		print(f"balance après vente du produit {product.name}  : {self.balance} euros")
