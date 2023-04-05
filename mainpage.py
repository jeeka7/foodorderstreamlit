import streamlit as st

menu = {
    'Burger': 10,
    'Pizza': 15,
    'Fries': 5,
    'Drink': 2
}

st.sidebar.title('Menu')

for item in menu:
    st.sidebar.write(f'{item}: ${menu[item]}')
st.title('Food Order Form')

with st.form('order_form'):
    for item in menu:
        quantity = st.number_input(f'{item} quantity', min_value=0, max_value=10, key=item)
    
    submit_button = st.form_submit_button(label='Place Order')
if submit_button:
    total_price = 0
    for item in menu:
        quantity = order_form[item]
        total_price += quantity * menu[item]
        
    st.write(f'Total Price: ${total_price}')
