class InventoryManager:
	def __init__(self):
		self.inventory : Dict[str, InventoryProductEntry] = {}

	def product_exists(self,product:Product):
		for inventory_product_entry_key in self.inventory:
			if (inventory_product_entry_key == product.name):
				return True
		return False
		
	def add_product(self, product:Product, quantity):
		#if product exists inventory, increase quantity 
		if self.product_exists(product):
			print("Ce produit existe déja. (Une seule référence par produit)")
			pass
		else:
			inventory_product_entry = InventoryProductEntry(product, quantity)
			self.inventory[product.name]=inventory_product_entry
			
	def remove_product(self, product:Product):
		if self.product_exists(product):
				self.inventory.pop(product.name)

	def sell_product(self, product:Product, quantity):
		for inventory_product_entry_key in self.inventory:
			if inventory_product_entry_key == product.name:
				self.inventory[inventory_product_entry_key].sell(quantity)
				return
		print(f"product {product.name} not found")

	def restock_product(self, product:Product, quantity):		
		if self.product_exists(product):
			self.inventory[product.name].restock(quantity)
		else:
			self.add_product(product,0)
			self.restock_product(product,quantity)

	def get_product(self, name):
		for inventory_product_entry_key in self.inventory:
			if inventory_product_entry_key == name:
				return self.inventory[inventory_product_entry_key].product
		print(f"product {name} not found")

	def list_products(self):
		for inventory_product_entry_key in self.inventory:
			print(self.inventory[inventory_product_entry_key])
		return self.inventory

