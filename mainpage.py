import streamlit as st

# Define the menu items
menu_items = {
    "Burger": 6,
    "Pizza": 10,
    "Fries": 3,
    "Soda": 2
}

# Create a dictionary to store the order
order = {}

# Define the title and subtitle of the app
st.title("Food Ordering App")
st.subheader("Welcome to our offline store!")

# Display the menu items
st.sidebar.header("Menu")
st.sidebar.write(menu_items)

# Collect the order from the user
st.header("Order")
item = st.selectbox("Select an item", list(menu_items.keys()))
quantity = st.number_input("Quantity", min_value=1, max_value=10, step=1)
add_to_order = st.button("Add to Order")

if add_to_order:
    if item in order:
        order[item] += quantity
    else:
        order[item] = quantity
    st.success(f"Added {quantity} {item}(s) to your order.")

# Display the current order
st.header("Current Order")
if not order:
    st.write("Your order is empty.")
else:
    for item, quantity in order.items():
        st.write(f"{item}: {quantity}")

# Checkout the order
checkout = st.button("Checkout")
if checkout:
    total_cost = sum([menu_items[item] * quantity for item, quantity in order.items()])
    st.success(f"Total amount is {total_cost}  INR. Thank you for your order!")

# Reset the order
reset_order = st.button("Reset Order")
if reset_order:
    order.clear()
    st.warning("Order reset.")
