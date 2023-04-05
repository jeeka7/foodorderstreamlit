import streamlit as st

# Set up the sidebar menu
st.sidebar.title("Menu")
menu_items = ["Burger", "Pizza", "Salad"]
selected_item = st.sidebar.selectbox("Select a menu item", menu_items)

# Set up the food order form
st.title("Food Order Form")
name = st.text_input("Name")
address = st.text_input("Address")
phone = st.text_input("Phone")
quantity = st.number_input("Quantity", min_value=1, max_value=10, step=1)
delivery = st.radio("Delivery method", ("Delivery", "Pickup"))

# Submit the order
if st.button("Place Order"):
    st.write(f"Thank you for your order, {name}!")
    st.write(f"You ordered {quantity} {selected_item}(s).")
    st.write(f"Your {delivery.lower()} address is {address}. We will call you at {phone} to confirm your order.")
