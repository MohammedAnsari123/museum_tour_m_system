import streamlit as st
from PIL import Image

# Load images (you must have local copies or use URLs)
msi_image = Image.open("IMG_23C5FC11-BF17-4A7B-BB46-7FF75F821C3F.jpeg")
brussels_image = Image.open("IMG_33E08E81-D2D5-43B2-99BB-31550CF9AD03.jpeg")
british_image = Image.open("IMG_DA063953-1B32-4188-9CF6-F489C6C5A3C5.jpeg")

# Page Configuration
st.set_page_config(page_title="Museum World Portal", layout="wide")

# Header Section
st.markdown("<h1 style='text-align: center; color: navy;'>🌍 Museum World</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Discover. Learn. Be Curious.</h4>", unsafe_allow_html=True)
st.markdown("---")

# Featured Exhibit Image Carousel Style Layout
col1, col2, col3 = st.columns(3)
with col1:
    st.image(msi_image, caption="Museum of Science + Industry (Chicago)", use_column_width=True)
with col2:
    st.image(brussels_image, caption="Brussels Museum", use_column_width=True)
with col3:
    st.image(british_image, caption="British Museum", use_column_width=True)

st.markdown("---")

# Quote/Tagline Section
st.markdown("<h3 style='text-align: center; color: teal;'>“Long Live Curiosity” – Where History Meets Discovery</h3>", unsafe_allow_html=True)

# Login Tabs
tab1, tab2 = st.tabs(["🔑 User Login", "🛠 Admin Login"])

with tab1:
    st.subheader("Visitor Login")
    user_username = st.text_input("Username")
    user_password = st.text_input("Password", type="password")
    if st.button("Login as User"):
        if user_username == "user" and user_password == "1234":
            st.success("Welcome, Visitor!")
            st.info("You can now explore exhibitions and plan your visit.")
        else:
            st.error("Invalid credentials.")

with tab2:
    st.subheader("Admin Login")
    admin_username = st.text_input("Admin Username")
    admin_password = st.text_input("Admin Password", type="password")
    if st.button("Login as Admin"):
        if admin_username == "admin" and admin_password == "admin123":
            st.success("Welcome, Admin!")
            st.warning("You have access to manage exhibitions and content.")
        else:
            st.error("Invalid admin credentials.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>📍 5700 S Lake Shore Dr, Chicago, IL 60637 | ✉ contact@museumworld.com</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Inspired by MSI Chicago, Brussels & British Museum</p>", unsafe_allow_html=True)