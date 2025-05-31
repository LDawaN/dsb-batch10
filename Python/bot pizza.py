MENU  = {
    "Hawaiian Deluxe"	: {"Small": 120, "Medium":250, "Large":350},
    "Pepperoni Cheese Lover"	: {"Small": 150, "Medium":280, "Large":380},
    "Classic Margherita	Medium"	: {"Small": 100, "Medium":220, "Large":320},
    "Seafood Extreme"	: {"Small": 180, "Medium":320, "Large":450},
    "Spinach and Mushroom"	: {"Small": 130, "Medium":260, "Large":360},
    "BBQ Chicken"	: {"Small": 140, "Medium":270, "Large":370}
}
order_price_total = 0
current_order = {}

def View_menu():
  print("Pizza Manu")
  if not MENU:
    print("Sorry, we're out of pizza.")
    return
  for item, sizes in MENU.items():
    print(f"- {item} :")
    for size, price in sizes.items():
      print(f"- {size} and {price:.2f}")


def add():
  global order_price_total

  View_menu()

  while True:
    cp = input(f"Enter the name pizza that you want to order (or 'done' to finish): ").strip()
    if cp == "done":
      break
    if cp in MENU:
      while True:
        sp = input(f"{cp}: Small, Median or Large").strip().capitalize()
        if sp in MENU[cp]:
          while True:
            quantity = int(input(f"How many {cp} {sp} would you like?"))
            if quantity > 0:
              price = MENU[cp][sp]
              order_item = (cp,sp)
              current_order[order_item] = current_order.get(order_item,0) + quantity
              order_price_total += price*quantity
              print(f"{quantity} x {cp} {sp} added to your order.")
              break
            else:
              print("Please specify the quantity you want.")
        break
      else:
        print("Invalid size. Please choose from Small, Medium, or Large.")

      another = input("Add another pizza? (yes/no): ").strip().lower()
      if another != 'yes':
          break
    else:
      print("Sorry, that pizza is not on the menu. Please choose from the list or type 'done' to finish.")

def View_order():
  if not current_order:
    print("your order is currently empty.")
  else:
    for (cp, sp), quantity in current_order.items():
      item_price = MENU[cp][sp]
      print(f"- {quantity} x {cp} ({sp}): ${item_price:.2f} each = ${quantity * item_price:.2f}")
    print("------------------------")
    print(f"Total Amount: ${order_price_total:.2f}")


def payment():
  if not current_order:
    print("Your order is currently empty. Nothing to pay for.")
    return

  View_order()
  print(f"\n Your total is ${order_price_total:.2f}")


def main():
  print("welcome to pizza company")

  while True:
    print("\nWhat would you like to do?")
    print("1. View Menu")
    print("2. Add to Order")
    print("3. View Your Order")
    print("4. Proceed to Payment")
    print("5. Exit")

    c = input("Enter your choice (1-5):")

    if c == "1":
      View_menu()
    elif c == "2":
      add()
    elif c == "3":
      View_order()
    elif c == "4":
      payment()
    elif c == "5":
      print("Thank you Pizza Company is pleased to serve you.")
      break
    else:
      print("The number you selected is incorrect. Please select again.")

if __name__ == "__main__":
    # This ensures the main function runs only when the script is executed directly
    main()
