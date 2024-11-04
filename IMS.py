class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


class UserManager:
    def __init__(self):
        self.users = {
            "admin": User("admin", "adminpass", "Admin"),
            "user": User("user", "userpass", "User")
        }

    def authenticate(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        return None


class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        self.stock_quantity += quantity

    def update_details(self, name=None, category=None, price=None, stock_quantity=None):
        if name:
            self.name = name
        if category:
            self.category = category
        if price:
            self.price = price
        if stock_quantity is not None:
            self.stock_quantity = stock_quantity

    def __str__(self):
        return f"ID: {self.product_id} | Name: {self.name} | Category: {self.category} | Price: {self.price} | Stock: {self.stock_quantity}"


class Inventory:
    LOW_STOCK_THRESHOLD = 5  

    def __init__(self):
        self.products = {}  
        self.next_product_id = 1

    def add_product(self, name, category, price, stock_quantity):
        product_id = self.next_product_id
        self.products[product_id] = Product(product_id, name, category, price, stock_quantity)
        self.next_product_id += 1
        print("Product added successfully.")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def edit_product(self, product_id, name=None, category=None, price=None, stock_quantity=None):
        product = self.products.get(product_id)
        if product:
            product.update_details(name, category, price, stock_quantity)
            print("Product updated successfully.")
        else:
            print("Product not found.")

    def view_products(self):
        if not self.products:
            print("No products in inventory.")
        else:
            for product in self.products.values():
                print(product)
                if product.stock_quantity < Inventory.LOW_STOCK_THRESHOLD:
                    print("Warning: Low stock!")

    def search_product(self, search_term):
        results = [p for p in self.products.values() if search_term.lower() in p.name.lower() or search_term.lower() in p.category.lower()]
        if results:
            for product in results:
                print(product)
        else:
            print("No products found matching your search.")

    def adjust_stock(self, product_id, quantity):
        product = self.products.get(product_id)
        if product:
            product.update_stock(quantity)
            print("Stock adjusted successfully.")
        else:
            print("Product not found.")


class InventorySystem:
    def __init__(self):
        self.user_manager = UserManager()
        self.inventory = Inventory()
        self.current_user = None

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = self.user_manager.authenticate(username, password)
        if user:
            self.current_user = user
            print(f"Welcome, {user.username}! You are logged in as {user.role}.")
        else:
            print("Invalid username or password.")
            return False
        return True

    def check_permission(self, required_role):
        if self.current_user and self.current_user.role == required_role:
            return True
        print("You do not have permission to perform this action.")
        return False

    def run(self):
        print("Welcome to the Inventory Management System!")
        if not self.login():
            return

        while True:
            print("\n1. View Products")
            print("2. Search Products")
            if self.current_user.role == "Admin":
                print("3. Add Product")
                print("4. Edit Product")
                print("5. Delete Product")
                print("6. Adjust Stock")
            print("0. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.inventory.view_products()
            elif choice == "2":
                search_term = input("Enter product name or category to search: ")
                self.inventory.search_product(search_term)
            elif choice == "3" and self.check_permission("Admin"):
                name = input("Enter product name: ")
                category = input("Enter product category: ")
                price = float(input("Enter product price: "))
                stock_quantity = int(input("Enter stock quantity: "))
                self.inventory.add_product(name, category, price, stock_quantity)
            elif choice == "4" and self.check_permission("Admin"):
                product_id = int(input("Enter product ID to edit: "))
                name = input("Enter new name (or press Enter to skip): ")
                category = input("Enter new category (or press Enter to skip): ")
                price = input("Enter new price (or press Enter to skip): ")
                stock_quantity = input("Enter new stock quantity (or press Enter to skip): ")
                self.inventory.edit_product(product_id, name or None, category or None, float(price) if price else None, int(stock_quantity) if stock_quantity else None)
            elif choice == "5" and self.check_permission("Admin"):
                product_id = int(input("Enter product ID to delete: "))
                self.inventory.delete_product(product_id)
            elif choice == "6" and self.check_permission("Admin"):
                product_id = int(input("Enter product ID to adjust stock: "))
                quantity = int(input("Enter quantity to adjust (positive to add, negative to reduce): "))
                self.inventory.adjust_stock(product_id, quantity)
            elif choice == "0":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = InventorySystem()
    system.run()
