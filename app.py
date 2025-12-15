import streamlit as st

st.set_page_config(page_title="Bank of Bhutan RTGS Charge Calculator", layout="centered")

st.title("Bank of Bhutan RTGS Charge Calculator")

amount = st.number_input("Enter Amount", min_value=0.0, step=1000.0)

def calculate_charge(amount):
    if amount <= 100000:
        return 35.0
    elif amount >= 1000000:
        return max(amount * 0.00174694109258516, 2000)
    else:
        return amount * 0.0019960091082926

if st.button("Calculate"):
    charge = calculate_charge(amount)
    st.success(f"Calculated Charge: Nu. {charge:.2f}")
st.markdown("""
---
**RTGS Charges Calculator**  
Developed by **Prakash Giri KASH BRO**  
© 2025
""")
