import streamlit as st

# Define menu items and their prices
menu = {
    "Burger": 10.0,
    "Pizza": 20.0,
    "Sandwich": 5.0,
    "Fries": 3.0
}

# Define a function to calculate the total cost of the order
def calculate_total(order):
    total = 0.0
    for item, quantity in order.items():
        total += menu[item] * quantity
    return total

# Define the main function
def main():
    st.title("Food Ordering and Payment System")

    # Display the menu
    st.write("## Menu")
    for item, price in menu.items():
        st.write(f"{item}: ${price:.2f}")

    # Get the user's order
    st.write("## Order")
    order = {}
    for item in menu.keys():
        quantity = st.number_input(f"How many {item}s do you want?", min_value=0, value=0)
        if quantity > 0:
            order[item] = quantity

    # Calculate the total cost
    total = calculate_total(order)

    # Display the total cost
    st.write("## Total")
    st.write(f"Total cost: ${total:.2f}")

    # Get the user's UPI ID
    st.write("## Payment")
    upi_id = st.text_input("Enter your UPI ID")

    # Allow the user to confirm the order and pay
    if st.button("Confirm order and pay"):
        # TODO: Implement the UPI payment functionality here
        st.write(f"Your order has been confirmed and paid for. Thank you for ordering!")

# Run the main function
if __name__ == "__main__":
    main()
