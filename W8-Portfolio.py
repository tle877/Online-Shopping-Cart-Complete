class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description = "none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print(str(self.item_name) + " " + str(self.item_quantity) + "@" + " $" + str(
            self.item_price) + " =$" + str(self.item_price * self.item_quantity))


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        for cart_item in self.cart_items:
            if cart_item.item_name == item_name:
                self.cart_items.remove(cart_item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modify_item):
        for cart_item in self.cart_items:
            if cart_item.item_name == modify_item.item_name:
                cart_item.item_quantity = modify_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_number = 0
        for item in self.cart_items:
            total_number += item.item_quantity
        return total_number
   

    def get_cost_of_cart(self):
        total_cost = 0
        for cart_item in self.cart_items:
            total_cost += (cart_item.item_price * cart_item.item_quantity)
        return total_cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("Number of Items: ", self.get_num_items_in_cart())
        for item in self.cart_items:
            item.print_item_cost()
        print("Total: $" + str(self.get_cost_of_cart()))

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("Item Descriptions")
        for item in self.cart_items:
            print(item.item_name + ": " + item.item_description)


def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        user_choice = input("Please choose an option or 'q' to quit: ")
        print("\n")

        if user_choice == 'a':
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(item_name, item_price, item_quantity,item_description)
            cart.add_item(item)
        elif user_choice == 'r':
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove: ")
            cart.remove_item(name)
        elif user_choice == 'c':
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name: ")
            quantity = int(input("Enter the new quantity: "))
            item = ItemToPurchase(name, 0, quantity,"none")
            cart.modify_item(item)
        elif user_choice == 'i':
            cart.print_descriptions()
        elif user_choice == 'o':
            cart.print_total()
        elif user_choice == 'q':
            break
        else:
            print("Invalid user_choice. Please try again.")


def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    print("Customer name: ", customer_name)
    print ("Today's date: ", current_date)
    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)


if __name__ == "__main__":
    main()
