import streamlit as st
from zexparemental.auth import authenticate

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    role = authenticate(username, password)
    if role:
        st.success(f"Logged in as {role}")
        # redirect to AdminPage() or VisitorPage()
    else:
        st.error("Invalid username or password")
