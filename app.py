import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(page_title="RTGS Charges Calculator", layout="centered")

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"

# Demo user store (for Streamlit Cloud)
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


def logout():
    st.session_state.logged_in = False
    st.session_state.page = "login"
    st.experimental_rerun()


# ---------------- LOGIN PAGE ----------------
def login_page():
    st.title("🏦 Bank of Bhutan")
    st.subheader("RTGS Charges Calculator – Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            if username in USERS and USERS[username]["password"] == password:
                st.session_state.logged_in = True
                st.session_state.page = "app"
                st.success("Login successful")
                st.experimental_rerun()
            else:
                st.error("Invalid username or password")

    with col2:
        if st.button("New User Registration"):
            st.session_state.page = "register"
            st.experimental_rerun()


# ---------------- REGISTRATION PAGE ----------------
def register_page():
    st.title("📝 New User Registration")
    st.info("One-time registration fee: **Nu. 100**")

    with st.form("register_form"):
        name = st.text_input("Full Name")
        username = st.text_input("Choose Username")
        password = st.text_input("Choose Password", type="password")
        cic = st.text_input("Citizen Identity Card (CIC) Number", max_chars=12)

        submit = st.form_submit_button("Register")

    if submit:
        if not all([name, username, password, cic]):
            st.error("All fields are required")
        elif username in USERS:
            st.error("Username already exists")
        else:
            # DEMO ONLY (No DB, no payment gateway)
            USERS[username] = {
                "password": password,
                "name": name
            }
            st.success("Registration successful (Demo)")
            st.info("Please login to continue")
            st.session_state.page = "login"
            st.experimental_rerun()

    if st.button("⬅ Back to Login"):
        st.session_state.page = "login"
        st.experimental_rerun()


# ---------------- MAIN APP ----------------
def app_page():
    st.title("RTGS Charges Calculator")

    with st.sidebar:
        st.success(f"Logged in as: **{list(USERS.keys())[0]}**")
        if st.button("Logout"):
            logout()

    amount = st.number_input("Enter Amount", min_value=0.0, step=1000.0)

    if st.button("Calculate"):
        charge = calculate_charge(amount)
        st.success(f"Charge: **Nu. {charge:.2f}**")

    st.markdown("""
    ---
    **RTGS Charges Calculator**  
    Developed by **Prakash Giri (KASH-BRO)**  
    © 2025
    """)


# ---------------- ROUTER ----------------
if st.session_state.page == "login":
    login_page()

elif st.session_state.page == "register":
    register_page()

elif st.session_state.page == "app" and st.session_state.logged_in:
    app_page()

else:
    st.session_state.page = "login"
    st.experimental_rerun()
