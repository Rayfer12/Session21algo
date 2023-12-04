from se21 import Foodinnit

def create_object_list():
    object_list = []

    num_items = 0
    while num_items <= 0:
        try:
            num_items = int(input("Enter the amount you want to buy: "))
            if num_items <= 0:
                print("Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    for _ in range(num_items):
        item_name = input("Enter the name of the item: ")

        amount_ordered = 0
        while amount_ordered <= 0:
            try:
                amount_ordered = float(input(f"Enter the amount of {item_name} in pounds: "))
                if amount_ordered <= 0:
                    print("Please enter a valid amount.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        food_order_object = Foodinnit(item_name, amount_ordered)
        object_list.append(food_order_object)

    return object_list

def display_order_list(order_list):
    for order in order_list:
        order.cost_of_ordered_food()

        print(f"Item: {order._item_name}")
        print(f"Amount Ordered: {order._amount_ordered} pounds")
        print(f"Standard Price per Pound: ${order._standard_price_per_pound:.2f}")
        print(f"Calculated Price: ${order._calculated_price:.2f}")
        print("-" * 30)

def calculate_total_cost(order_list):
    total_cost = 0
    for order in order_list:
        order.cost_of_ordered_food()
        total_cost += order._calculated_price
    return total_cost

def main():
    order_list = create_object_list()
    display_order_list(order_list)
    total_cost = calculate_total_cost(order_list)
    print(f"Total Cost of All Items: ${total_cost:.2f}")

if __name__ == "__main__":
    main()