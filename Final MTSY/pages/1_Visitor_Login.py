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

st.title("👤 Visitor Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "guest" and password == "123":
        st.success("Login successful!")
        st.switch_page("pages/3_Visitor_Dashboard.py")
    else:
        st.error("Invalid credentials.")
