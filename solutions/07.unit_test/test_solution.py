import sys
sys.path.extend(['.','..'])
from classes.product_classes import Chaise, Pantalon
from inventory.stock_manager import InventoryManager, ProfitTracker

import unittest

class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        self.inventory_manager = InventoryManager()
        self.chaise = Chaise("materiau2", "couleur2", "dimension2", 50, 100, "Ikea")
        self.pantalon = Pantalon("M", "noir", "jeans", 150, 200,"Zara")

    def test_add_product(self):
        self.inventory_manager.add_product(self.chaise, 5)
        self.assertIn(self.chaise.name, self.inventory_manager.inventory)

    def test_remove_product(self):
        self.inventory_manager.add_product(self.pantalon, 5)
        self.inventory_manager.remove_product(self.pantalon)
        self.assertNotIn(self.pantalon.name, self.inventory_manager.inventory)

    def test_sell_product(self):
        self.inventory_manager.add_product(self.pantalon, 5)
        self.inventory_manager.sell_product(self.pantalon, 2)
        self.assertEqual(self.inventory_manager.inventory[self.pantalon.name].quantity, 3)

    def test_restock_product(self):
        self.inventory_manager.add_product(self.chaise, 10)
        self.inventory_manager.restock_product(self.chaise, 5)
        self.assertEqual(self.inventory_manager.inventory[self.chaise.name].quantity, 15)

    def test_get_product(self):
        self.inventory_manager.add_product(self.chaise, 5)
        product = self.inventory_manager.get_product(self.chaise.name)
        self.assertEqual(product, self.chaise)

    def test_list_products(self):
        self.inventory_manager.add_product(self.chaise, 5)
        self.inventory_manager.add_product(self.pantalon, 10)
        list_product=self.inventory_manager.list_products()
        expected_output = "Chaise (Ikea): 5 in stock,  price:100"
        self.assertEqual(str(list_product['Chaise']), expected_output)


# class TestProfitTracker(unittest.TestCase):

#     def setUp(self):
#         self.profit_tracker = ProfitTracker()
#         self.chaise = Chaise("materiau2", "couleur2", "dimension2", 50, 100, "Ikea")
#         self.pantalon = Pantalon("M", "noir", "jeans", 150, 200,"Zara")

#     def test_buy_product(self):
#         self.assertTrue(self.profit_tracker.buy_product(self.chaise, 5))
#         self.assertFalse(self.profit_tracker.buy_product(self.pantalon, 1000))

#     def test_sell_product(self):
#         self.profit_tracker.sell_product(self.chaise, 2)
#         self.assertEqual(self.profit_tracker.balance, 1200)

#     def test_calcul_profit(self):
#         self.profit_tracker.buy_product(self.pantalon, 2)
#         self.profit_tracker.sell_product(self.pantalon, 5)
#         self.assertEqual(self.profit_tracker.calcul_profit(), 1700)


if __name__ == '__main__':
    unittest.main()
