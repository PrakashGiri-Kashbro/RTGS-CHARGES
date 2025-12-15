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
# --- 3. REGISTRATION PAGE (For New Users) ---

def register_page():
    """Handles the sign-up process, including CIC number and Payment."""
    st.title("New User Registration")

    # Step 1: Initialize session state for payment status
    if 'payment_status' not in st.session_state:
        st.session_state['payment_status'] = 'PENDING_DETAILS'
    
    # --- A. Collect User Details ---
    if st.session_state['payment_status'] == 'PENDING_DETAILS':
        with st.form("register_details_form"):
            st.subheader("Step 1: Account Details (Nu. 100 Fee)")
            st.info("A one-time registration fee of **Nu. 100** is required.")
            
            # Form Inputs
            new_name = st.text_input("Full Name")
            new_username = st.text_input("Choose Username")
            new_password = st.text_input("Choose Password", type='password')
            cic_number = st.text_input("Citizen Identity Card Number", max_chars=12)
            
            register_button = st.form_submit_button("Proceed to Payment (Nu. 100)")

        if register_button:
            if not (new_name and new_username and new_password and cic_number):
                st.error("All fields are required.")
            else:
                # ⚠️ YOUR SECURE BACKEND API CALL GOES HERE!
                # 1. Send data to backend (Backend checks uniqueness of CIC, username)
                # 2. Backend stores data temporarily as 'unpaid user'.
                
                # Store data in session state for next step (in a real app, this is unsafe)
                st.session_state['temp_user_data'] = {
                    'name': new_name,
                    'username': new_username,
                    'password': new_password, # Should be a hash here!
                    'cic': cic_number
                }
                st.session_state['payment_status'] = 'PENDING_PAYMENT'
                st.experimental_rerun()
                
    # --- B. Handle Payment ---
    elif st.session_state['payment_status'] == 'PENDING_PAYMENT':
        st.subheader("Step 2: Complete Registration Payment")
        st.warning(f"Registration Fee: **Nu. 100.00**")
        
        # ⚠️ This is where you would integrate the payment gateway API
        # Example: Generate a payment link from your backend and show it here.
        payment_link = "http://your-secure-backend/pay/Nu100?user_temp_id=XYZ"
        
        st.markdown(f"""
        1. Click the link below to securely pay the Nu. 100 fee.
        2. **Do not close this window.** Once payment is confirmed, your account will be activated.
        
        [**Click Here to Pay Nu. 100**]({payment_link})
        """)
        
        # --- Mock Payment Completion Check ---
        # In a real app, this button is replaced by a check against your backend database.
        if st.button("I have Completed Payment"):
            # ⚠️ BACKEND CHECK REQUIRED:
            # Your code needs to ping the backend to confirm the webhook was received.
            st.session_state['payment_status'] = 'CONFIRMED'
            st.experimental_rerun()
            
        if st.button("<< Back to Details"):
            st.session_state['payment_status'] = 'PENDING_DETAILS'
            st.experimental_rerun()

    # --- C. Final Confirmation ---
    elif st.session_state['payment_status'] == 'CONFIRMED':
        # ⚠️ BACKEND ACTION REQUIRED HERE:
        # Finalize the user's account in the secure database.
        # Encrypt CIC, Hash Password, and mark the user as 'Active'.
        
        st.success("✅ Payment Confirmed! Your account is now active.")
        st.balloons()
        
        # Reset state to redirect to the login screen
        st.session_state['show_register'] = False
        st.session_state['payment_status'] = 'PENDING_DETAILS'
        st.experimental_rerun()

# --- MAIN APPLICATION FLOW CALL ---
# Ensure your main flow calls this updated register_page() function
# when st.session_state['show_register'] is True.

