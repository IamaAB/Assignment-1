from abc import ABC, abstractmethod


# base class
class Product:
    def _init_(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_price(self):
        pass


# child classes inherited from base class
class PhysicalProduct(Product):
    def _init_(self, name, price, shipping_cost):
        super()._init_(name, price)
        self.shipping_cost = shipping_cost

    # define method to calculate price for physical product
    def calculate_price(self):
        return self.price + self.shipping_cost


class DigitalProduct(Product):
    def _init_(self, name, price, download_link):
        super()._init_(name, price)
        self.download_link = download_link

    # define method to calculate price for digital product
    def calculate_price(self):
        return self.price


class ShoppingCart:
    def _init_(self):
        self.products = {}

    def add_product(self, product, quantity=1):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def remove_product(self, product, quantity=1):
        if product in self.products:
            self.products[product] -= quantity
            if self.products[product] <= 0:
                del self.products[product]

    def calculate_total_price(self):
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.calculate_price() * quantity
        return total_price

    def checkout(self):
        total_price = self.calculate_total_price()
        print(f"Total price: ${total_price} .\n")
        print("Checkout complete! .\n")


available_products = {
    1: PhysicalProduct("Laptop", 800, 5),
    2: DigitalProduct("Software", 50, "download-link"),
    3: PhysicalProduct("Smartphone", 500, 0.5),
    4: DigitalProduct("E-book", 10, "ebook-link"),
    5: PhysicalProduct("Camera", 400, 2),
    6: DigitalProduct("Game", 30, "game-link"),
    7: PhysicalProduct("Headphones", 100, 0.2),
    8: DigitalProduct("Music Album", 15, "album-link"),
}

cart = ShoppingCart()

print("Available products:")
for key, product in available_products.items():
    print(f"{key}: {product.name} - Price: ${product.price}")

while True:

    print("Options:.\n")
    print("1: Add product to cart")
    print("2: Remove product from cart")
    print("3: Finish shopping")

    choice = input("Enter your choice: ")

    if choice == '3':
        break
    elif choice == '1':
        product_choice = int(input("Enter the number of the product you want to add to the cart: .\n"))
        if product_choice in available_products:
            selected_product = available_products[product_choice]
            quantity = int(input(f"Enter the quantity of {selected_product.name} you want to add: .\n"))
            cart.add_product(selected_product, quantity)
        else:
            print("Invalid product number. Please select a valid product.")
    elif choice == '2':
        product_choice = int(input("Enter the number of the product you want to remove from the cart: .\n"))
        if product_choice in available_products:
            selected_product = available_products[product_choice]
            quantity = int(input(f"Enter the quantity of {selected_product.name} you want to remove: .\n"))
            cart.remove_product(selected_product, quantity)
        else:
            print("Invalid product number. Please select a valid product.")
    else:
        print("Invalid choice. Please select a valid option.")

cart.checkout()