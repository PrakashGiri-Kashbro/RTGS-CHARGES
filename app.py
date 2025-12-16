import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="RTGS Charges Calculator",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"

# ---------------- USERS (DEMO) ----------------
USERS = {
    "admin": {
        "password": "rtgs123",
        "name": "Administrator"
    }
}

# ---------------- LOGIC ----------------
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
    st.rerun()


def require_login():
    if not st.session_state.logged_in:
        st.session_state.page = "login"
        st.rerun()
        

        st.markdown(
            """
            **RTGS Charges Calculator**  
            Developed by **Prakash Giri (KASH-BRO)**  
            © 2025
            """
        )
# ---------------- LOGIN PAGE ----------------
def login_page():
    st.title("🏦 Bank of Bhutan")
    st.subheader("RTGS Charges Calculator")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            if username in USERS and USERS[username]["password"] == password:
                st.session_state.logged_in = True
                st.session_state.page = "app"
                st.rerun()
            else:
                st.error("Invalid username or password")

    with col2:
        if st.button("New User Registration"):
            st.session_state.page = "register"
            st.rerun()

# ---------------- REGISTRATION PAGE ----------------
def register_page():
    st.title("📝 New User Registration")
    st.info("One-time registration fee: **Nu. 100**")

    with st.form("register_form"):
        name = st.text_input("Full Name")
        username = st.text_input("Choose Username")
        password = st.text_input("Choose Password", type="password")
        cic = st.text_input("Citizen Identity Card Number", max_chars=12)
        submit = st.form_submit_button("Register")

    if submit:
        if not name or not username or not password or not cic:
            st.error("All fields are required")
        elif username in USERS:
            st.error("Username already exists")
        else:
            USERS[username] = {
                "password": password,
                "name": name
            }
            st.success("Registration successful (Demo)")
            st.session_state.page = "login"
            st.rerun()

    if st.button("Back to Login"):
        st.session_state.page = "login"
        st.rerun()

# ---------------- APP PAGE (PROTECTED) ----------------
def app_page():
    require_login()

    st.title("RTGS Charges Calculator")

    # ✅ SINGLE SIDEBAR (ONLY HERE)
    with st.sidebar:
        st.success("Logged in")
        if st.button("Logout", key="logout_btn"):
            logout()

        st.markdown("---")
        st.markdown(
            """
            **RTGS Charges Calculator**  
            Developed by **Prakash Giri (KASH-BRO)**  
            © 2025
            """
        )

    amount = st.number_input(
        "Enter Amount",
        min_value=0.0,
        step=1000.0
    )

    if st.button("Calculate", key="calc_btn"):
        charge = calculate_charge(amount)
        st.success(f"Charge: Nu. {charge:.2f}")

# ---------------- ROUTER ----------------
if st.session_state.page == "login":
    login_page()

elif st.session_state.page == "register":
    register_page()

elif st.session_state.page == "app":
    app_page()

else:
    st.session_state.page = "login"
    st.rerun()
