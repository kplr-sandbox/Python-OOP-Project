import sys
sys.path.extend(['.','..'])
from inventory.stock_manager import *
import json
from unidecode import unidecode
import generator
from classes.product_classes import *
import readline
import utils

def main():

    inventory_manager = InventoryManager()
    json_data= generator.read_json("code/data/json_data.json")
    json_data = generator.trimspaces(json_data)
    json_dict = json.loads(str(unidecode(json_data)))

    readline.set_completer_delims(' \t\n')
    readline.parse_and_bind("tab: complete")

    # Define a function to handle user input
    def auto_complete(text, list):
        matching_entry = [entry for entry in list if entry.startswith(text)]
        if len(matching_entry) == 1:
            entry_name = matching_entry[0]
            remaining_text = entry_name[len(text):]
            if remaining_text:          
                readline.insert_text(remaining_text)
                readline.redisplay()
                
    def set_autocomplete(list):
        readline.set_completer(lambda text, state: auto_complete(text,list))

    while True:
        print("""
			What would you like to do? :
			A. Add a product to stock
			R. Restock a product quantity
			S. Sell a product quantity
			D. Remove a product from stock
			L. List the products in stock
			B. Show the current balance
			Q. Quit
		""")
        
        choice = input("Enter your choice: ")
        choice = choice.upper()
        
        if choice == "A":
            
            utils.print_list
                
            class_tree = generator.generate_tree_hierarchy(json_dict)
            
            product_classes = class_tree.get_penultimate_nodes()
        
            utils.sep()

            utils.print_list(product_classes)
            set_autocomplete(product_classes)
            category = input("Enter the category of the product: ")
            
            # Get the immediate children nodes of node 'B'
            children_nodes = class_tree.get_children_nodes(category)
            utils.print_list(children_nodes)
            set_autocomplete(children_nodes)
            product_name = input("Enter your product choice: ")   
            #print(f"{name} has been added to stock with a quantity of {quantity}.")
                        
            product_entry = utils.prompt_for_instance(globals()[product_name])
            quantity = int(input("Enter quantity: "))
            inventory_manager.add_product(product_entry, quantity)

        elif choice == "R":
            name = input("Enter the name of the product: ")
            quantity = int(input("Enter the quantity to restock: "))
            product = inventory_manager.get_product(name)
            inventory_manager.restock_product(product, quantity)


        elif choice == "S":
            name = input("Enter the name of the product: ")
            quantity = int(input("Enter the quantity to sell: "))
            product = inventory_manager.get_product(name)
            inventory_manager.sell_product(product, quantity)

        elif choice == "D":
            name = input("Enter the name of the product: ")
            product = inventory_manager.get_product(name)
            if product:
                inventory_manager.remove_product(product)
                print(f"{name} has been removed from stock.")
            else:
                print(f"{name} is not in stock.")

        elif choice == "L":
            inventory_manager.list_products()

        elif choice == "B":
            print(f"Current balance: {inventory_manager.profit_tracker.balance} euros")

        elif choice == "Q":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == '__main__':
    main()
