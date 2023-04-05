import streamlit as st

# Define food items and prices
menu = {
    "Burger": 10,
    "Pizza": 12,
    "Salad": 8,
    "Fries": 4
}

# Initialize cart
cart = {}

# Display menu and accept user input
st.title("Food Ordering App")
st.write("Welcome to our menu!")
for item, price in menu.items():
    st.write(f"{item}: {price} INR")
    quantity = st.number_input(f"Enter quantity for {item}", min_value=0, max_value=10)
    if quantity > 0:
        cart[item] = quantity

# Display cart and total
st.write("Your Cart:")
for item, quantity in cart.items():
    st.write(f"{item} x {quantity}")
total = sum([menu[item]*quantity for item, quantity in cart.items()])
st.write(f"Total: {total} INR")

# Place order
if st.button("Place Order"):
    st.write("Thank you for your order!")
    cart.clear()
