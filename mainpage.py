import streamlit as st

# Define the food items available for order
food_items = {
    "Pizza": 10.99,
    "Burger": 7.99,
    "Fries": 3.99,
    "Chicken Wings": 8.99
}

# Create a sidebar menu of food items
st.sidebar.header("Menu")
selected_item = st.sidebar.selectbox("Select an item", list(food_items.keys()))

# Create a quantity selector
quantity = st.sidebar.number_input("Select quantity", min_value=1, max_value=10, value=1)

# Calculate the total price based on the selected item and quantity
total_price = food_items[selected_item] * quantity

# Display the order details
st.write("## Order Details")
st.write(f"Item: {selected_item}")
st.write(f"Quantity: {quantity}")
st.write(f"Total price: ${total_price:.2f}")
