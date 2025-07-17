import streamlit as st

st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🛠 Admin Login")

username = st.text_input("Admin Username")
password = st.text_input("Admin Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "admin123":
        st.success("Login successful!")
        st.switch_page("pages/4_Admin_Dashboard.py")
    else:
        st.error("Invalid admin credentials.")
