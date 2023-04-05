import streamlit as st

# Define the food items and their prices
menu = {"Pizza": 10, "Burger": 5, "Hot Dog": 4, "Fries": 3}

# Create a sidebar menu with the food items
st.sidebar.title("Menu")
food_choice = st.sidebar.selectbox("Select a food item", list(menu.keys()))

# Get the quantity of the selected food item
quantity = st.sidebar.number_input("Quantity", min_value=1, max_value=10, value=1)

# Calculate the total price of the order
total_price = menu[food_choice] * quantity

# Show the total price to the user
st.write(f"Total price: ${total_price}")

# Allow the user to place the order
if st.button("Place Order"):
    st.write("Your order has been placed!")
