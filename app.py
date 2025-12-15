import streamlit as st

USERNAME = "admin"
PASSWORD = "rtgs123"

st.title("Bank of Bhutan RTGS Charges Calculator")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if username == USERNAME and password == PASSWORD:
    st.success("Login successful")

    amount = st.number_input("Enter Amount", min_value=0.0)

    def calculate_charge(amount):
        if amount <= 100000:
            return 35.0
        elif amount >= 1000000:
            return max(amount * 0.00174694109258516, 2000)
        else:
            return amount * 0.0019960091082926

    if st.button("Calculate"):
        st.success(f"Charge: Nu. {calculate_charge(amount):.2f}")

else:
    st.warning("Please enter valid credentials")
st.markdown("""
---
**RTGS Charges Calculator**  
Developed by **Prakash Giri(KASH-BRO)**  
© 2025
""")


