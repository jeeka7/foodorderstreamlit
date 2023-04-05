import streamlit as st

# Define the menu items and their prices
menu_items = {
    "Burger": 10,
    "Pizza": 15,
    "Fries": 5,
    "Salad": 8,
}

# Define the initial order
order = []

# Define the sidebar for adding items to the order
st.sidebar.title("Menu")
for item, price in menu_items.items():
    quantity = st.sidebar.number_input(f"{item} (${price})", value=0)
    if quantity > 0:
        order.append({"item": item, "price": price, "quantity": quantity})

# Define the main section for displaying the order
st.title("Your Order")
if len(order) == 0:
    st.write("No items in your order")
else:
    total = sum(item["price"] * item["quantity"] for item in order)
    st.write(f"Total: ${total}")
    st.write("Items:")
    for item in order:
        st.write(f"- {item['quantity']} x {item['item']} (${item['price']}) = ${item['quantity'] * item['price']}")
def place_order(order):
    # Here you would add code to process the order, e.g. sending it to a restaurant or delivery service.
    # For this example, we'll just print the order to the console.
    print("Order placed:")
    for item in order:
        print(f"- {item['quantity']} x {item['item']} (${item['price']}) = ${item['quantity'] * item['price']}")
    total = sum(item["price"] * item["quantity"] for item in order)
    print(f"Total: ${total}")
