import streamlit as st

# Sample user database (username: password)
users = {
    "admin": "admin123",
    "john": "johnpass",
    "jane": "janepass"
}

def login(username, password):
    """Check if username and password match."""
    return users.get(username) == password

def main():
    st.set_page_config(page_title="Login Page", page_icon="🔐")

    st.title("🔐 User Login Page")

    # Login form
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            if login(username, password):
                st.success(f"Welcome, {username}!")
                st.balloons()
            else:
                st.error("Invalid username or password.")

if __name__ == "__main__":
    main()

