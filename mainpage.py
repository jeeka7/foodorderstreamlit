import streamlit as st

# Define the menu items
menu_items = {
    "Burger": 10.99,
    "Pizza": 15.99,
    "Fries": 5.99,
    "Drink": 2.99
}

# Define the payment options
payment_options = {
    "Credit Card": "credit_card",
    "Debit Card": "debit_card",
    "PayPal": "paypal",
    "Google Pay": "google_pay"
}

# Define the order form
def order_form():
    order = {}
    for item, price in menu_items.items():
        qty = st.number_input(f"How many {item}s would you like?", min_value=0, max_value=10, step=1)
        if qty > 0:
            order[item] = {"quantity": qty, "price": price}
    return order

# Define the payment form
def payment_form():
    payment = {}
    selected_option = st.selectbox("Select a payment option", list(payment_options.keys()))
    payment["option"] = payment_options[selected_option]
    if payment["option"] == "credit_card" or payment["option"] == "debit_card":
        payment["card_number"] = st.text_input("Enter your card number")
        payment["expiry_date"] = st.date_input("Enter the expiry date")
        payment["cvv"] = st.text_input("Enter the CVV")
    elif payment["option"] == "paypal":
        payment["email"] = st.text_input("Enter your PayPal email address")
        payment["password"] = st.text_input("Enter your PayPal password", type="password")
    elif payment["option"] == "google_pay":
        payment["phone_number"] = st.text_input("Enter your phone number")
        payment["pin"] = st.text_input("Enter your PIN", type="password")
    return payment

# Define the main app
def main():
    st.title("Food Ordering App")
    order = order_form()
    st.write("Your order:")
    for item, details in order.items():
        st.write(f"{item} x {details['quantity']} - ${details['price'] * details['quantity']:.2f}")
    total_price = sum([details['price'] * details['quantity'] for details in order.values()])
    st.write(f"Total: ${total_price:.2f}")
    payment = payment_form()
    st.write("Payment details:")
    st.write(f"Option: {list(payment_options.keys())[list(payment_options.values()).index(payment['option'])]}")
    if payment["option"] == "credit_card" or payment["option"] == "debit_card":
        st.write(f"Card Number: {payment['card_number']}")
        st.write(f"Expiry Date: {payment['expiry_date']}")
        st.write(f"CVV: {payment['cvv']}")
    elif payment["option"] == "paypal":
        st.write(f"PayPal Email: {payment['email']}")
        st.write(f"PayPal Password: {len(payment['password']) * '*'}")
    elif payment["option"] == "google_pay":
        st.write(f"Phone Number: {payment['phone_number']}")
        st.write(f"PIN: {len(payment['pin']) * '*'}")

if __name__ == "__
