import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(page_title="RTGS Charges Calculator", layout="centered")

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"

# Demo user store
USERS = {
    "admin": {
        "password": "rtgs123",
        "name": "Administrator"
    }
}

# ---------------- FUNCTIONS ----------------
def calculate_charge(amount):
    if amount <= 100000:
        return 35.0
    elif amount >= 1000000:
        return max(amount * 0.00174694109258516, 2000)
    else:
        return amount * 0.0019960091082926


def force_login():
    """Hard stop if user is not logged in"""
    if not st.session_state.logged_in:
        st.session_state.page = "login"
        st.rerun()


def logout():
    st.session_state.logged_in = False
    st.session_state.page = "login"
    st.rerun()

# ---------------- LOGIN PAGE ----------------
def login_page():
    st.title("🏦 Bank of Bhutan")
    st.subheader("RTGS Charges Calculator – Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("
