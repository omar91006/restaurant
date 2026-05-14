from abc import ABC, abstractmethod

# Abstract Base Class
class MenuItem(ABC):

    def __init__(self, item_id, name, price):

        self.item_id = item_id
        self.name = name
        self.__price = 0
        self.set_price(price)
        self.__available = True
    def get_price(self):
        return self.__price

    def is_available(self):
        return self.__available

    def set_price(self, price):

        if price > 0:
            self.__price = price
        else:
            print("Invalid price.")

    def set_availability(self, status):

        if isinstance(status, bool):
            self.__available = status
        else:
            print("Availability must be True or False.")

    @abstractmethod
    def calculate_final_price(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

# Food Class
class Food(MenuItem):

    def __init__(self, item_id, name, price, prep_time):

        super().__init__(item_id, name, price)

        self.prep_time = prep_time

    def calculate_final_price(self):
        # 15% service fee
        return self.get_price() * 1.15

    def display_info(self):

        print(
            f"[{self.item_id}] "
            f"{self.name} - "
            f"${self.get_price():.2f} "
            f"(Prep Time: {self.prep_time} mins)"
        )

# Beverage Class
class Beverage(MenuItem):

    def __init__(self, item_id, name, price, size):

        super().__init__(item_id, name, price)

        self.size = size

    def calculate_final_price(self):

        # 50% Happy Hour discount
        discounted = self.get_price() * 0.5

        # 10% sugar tax
        final = discounted * 1.10

        return final

    def display_info(self):

        print(
            f"[{self.item_id}] "
            f"{self.name} - "
            f"${self.get_price():.2f} "
            f"(Size: {self.size})"
        )

# Customer Order Class
class CustomerOrder:

    def __init__(self):

        self.items = []

    def add_item(self, item):

        self.items.append(item)

        print(f"{item.name} added successfully.")

    def view_order(self):

        if not self.items:
            print("Order is empty.")
            return

        print("\n======= CURRENT ORDER =======")

        for item in self.items:

            print(
                f"{item.name} - "
                f"${item.get_price():.2f}"
            )

    def print_receipt(self):

        if not self.items:
            print("Order is empty.")
            return

        print("\n")
        print("=" * 40)
        print("       RESTAURANT RECEIPT")
        print("=" * 40)

        total = 0

        for item in self.items:

            final_price = item.calculate_final_price()

            print(
                f"{item.name:<20}"
                f"${final_price:.2f}"
            )

            total += final_price

        print("-" * 40)

        print(f"{'TOTAL':<20}${total:.2f}")

        print("=" * 40)

menu = [

    Food(1, "Burger", 120, 15),
    Food(2, "Pizza", 200, 20),

    Beverage(3, "Cola", 50, "Medium"),
    Beverage(4, "Coffee", 80, "Large")
]

order = CustomerOrder()

def display_menu():

    print("\n======= MENU =======")

    for item in menu:

        item.display_info()

def find_item(user_input):

    for item in menu:

        if (
            str(item.item_id) == user_input
            or item.name.lower() == user_input.lower()
        ):

            return item

    return None

while True:

    print("\n")
    print("1. View Menu")
    print("2. Add Item")
    print("3. View Current Order")
    print("4. Print Receipt")
    print("5. Exit")

    choice = input("Choose option: ")

    try:

        if choice == "1":

            display_menu()

        elif choice == "2":

            user_input = input(
                "Enter item ID or name: "
            )

            item = find_item(user_input)

            if item:
                order.add_item(item)
            else:
                print("Item not found.")

        elif choice == "3":

            order.view_order()

        elif choice == "4":

            order.print_receipt()

        elif choice == "5":

            print("Exiting system...")
            break

        else:

            print("Invalid option.")

    except Exception as e:

        print("An error occurred:", e)