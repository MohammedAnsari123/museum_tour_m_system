import streamlit as st
from PIL import Image

# Optional: Load a banner image if you have it
# st.image("assets/images/banner.jpg", use_column_width=True)

# Set page config
st.set_page_config(page_title="Museum Tour Management System", layout="wide")

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



# --- Title & Introduction ---
st.markdown("<h1 style='text-align: center; color: #004080;'>🏛️ Museum Tour Management System</h1>", unsafe_allow_html=True)
st.markdown("### A Smart, AI-Integrated Museum Experience Platform")
st.write("""
Welcome to the Museum Tour Management System! This platform is designed to provide seamless experiences for **Visitors** and powerful tools for **Admins** to manage tours, exhibits, and visitor data effectively.
""")

st.markdown("---")

# --- Project Overview Section ---
with st.expander("📌 **Project Overview**"):
    st.markdown("""
The system is divided into two main user types:

### 👨‍💼 Admin:
- Manage Exhibits and Tours
- Analyze Visitor Data and Reviews
- Use ML for Bookings and Recommendations
- Respond to Visitor Feedback
- Access Smart Dashboard with Map and Stats

### 🙋 Visitor:
- Explore Museum Exhibits
- Book and Manage Tour Visits
- Rate and Review Tours
- Get Personalized Recommendations

This project includes an interactive chatbot, ML modules, and a full analytics dashboard powered by real datasets!
""")

# --- Buttons to navigate to login pages ---
st.markdown("### 🔐 Choose User Type to Proceed:")
col1, col2 = st.columns(2)

with col1:
    if st.button("🙋 Visitor Login"):
        # st.session_state["user_type"] = "visitor"
        #st.switch_page("VisitorLogin.py")  # You must have this script
        st.switch_page("pages/1_Visitor_Login.py")  #aksjdfbmnbsakjdfh

with col2:
    if st.button("👨‍💼 Admin Login"):
        # st.session_state["user_type"] = "admin"
        #st.switch_page("AdminLogin.py")  # You must have this script in the same directory or pages folder
        st.switch_page("pages/2_Admin_Login.py")

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center;'>Built with ❤️ using Streamlit | 2025 Museum Tech Hackathon</p>", unsafe_allow_html=True)


# import streamlit as st

# st.set_page_config(page_title="🏛 Museum Management System", layout="centered")

# st.markdown("""
#     <style>
#         [data-testid="stSidebar"] {
#             display: none;
#         }
#         [data-testid="collapsedControl"] {
#             display: none;
#         }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown("<h1 style='text-align:center; color:#08fdd8;'>🏛 Welcome to the Virtual Museum</h1>", unsafe_allow_html=True)
# st.markdown("<h4 style='text-align:center;'>Explore. Experience. Evolve.</h4>", unsafe_allow_html=True)

# st.image("assets/images/banner.jpg", use_column_width=True)

# st.markdown("### Login Options:")
# col1, col2 = st.columns(2)

# with col1:
#     if st.button("👤 Visitor Login"):
#         st.switch_page("pages/1_Visitor_Login.py")

# with col2:
#     if st.button("🛠 Admin Login"):
#         st.switch_page("pages/2_Admin_Login.py")
