import streamlit as st
from PIL import Image
import base64
from pathlib import Path

# Set page config
st.set_page_config(page_title="Museum Tour Management System", layout="wide")

# Hide sidebar elements
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
        .scroll-container {
            display: flex;
            overflow-x: auto;
            gap: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 10px;
            margin: 20px 0;
        }
        .scroll-container img {
            height: 180px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }
        .scroll-container img:hover {
            transform: scale(1.05);
        }
        .exhibit-title {
            font-size: 1.4rem;
            font-weight: bold;
            color: #2c3e50;
            margin-top: 30px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title & Introduction ---
st.markdown("<h1 style='text-align: center; color: #004080;'>🏛️ Museum Tour Management System</h1>", unsafe_allow_html=True)
st.markdown("### A Smart, AI-Integrated Museum Experience Platform")
st.write("""
Welcome to the Museum Tour Management System! This platform is designed to provide seamless experiences for **Visitors** and powerful tools for **Admins** to manage tours, exhibits, and visitor data effectively.
""")

# --- Featured Exhibits Section with Horizontal Scroll ---
st.markdown('<div class="exhibit-title">🌟 Featured Exhibits</div>', unsafe_allow_html=True)

def encode_image(img_path):
    with open(img_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
        return f"data:image/png;base64,{encoded}"

# Sample exhibit categories (replace with your actual images)
exhibit_categories = {
    "Modern Art": ["assets/images/Art1.jpg","assets/images/Art2.jpg","assets/images/Art3.jpg","assets/images/Art4.jpg","assets/images/Art5.jpg","assets/images/Art6.jpg"],
    "Cultural Heritage": ["assets/images/culture1.jpg","assets/images/culture2.jpg","assets/images/culture3.jpg","assets/images/culture4.jpg","assets/images/culture5.jpg"],
    "History": ["assets/images/History1.jpg","assets/images/History2.jpg","assets/images/History3.jpg","assets/images/History4.jpg","assets/images/History5.jpg","assets/images/History6.jpg"],
    "Scientific Discoveries": ["assets/images/Science1.jpg","assets/images/Science2.jpg","assets/images/Science3.jpg","assets/images/Science4.jpg","assets/images/Science5.jpg","assets/images/Science6.jpg","assets/images/Science7.jpg","assets/images/Science8.jpg","assets/images/Science9.jpg","assets/images/Science10.jpg","assets/images/Science11.jpg"]
}

for category, images in exhibit_categories.items():
    st.markdown(f'<div class="exhibit-title">{category}</div>', unsafe_allow_html=True)
    
    scroll_html = '<div class="scroll-container">'
    for img_path in images:
        try:
            if Path(img_path).exists():
                img_data_url = encode_image(img_path)
                scroll_html += f'<img src="{img_data_url}" title="{Path(img_path).stem}">'
            else:
                scroll_html += f'<div style="width: 200px; height: 180px; display: flex; align-items: center; justify-content: center; background: #eee; border-radius: 8px;">Sample Exhibit</div>'
        except Exception as e:
            scroll_html += f'<div style="color:red;">Error loading image</div>'
    scroll_html += '</div>'
    
    st.markdown(scroll_html, unsafe_allow_html=True)

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
        st.switch_page("pages/1_Visitor_Login.py")

with col2:
    if st.button("👨‍💼 Admin Login"):
        st.switch_page("pages/2_Admin_Login.py")

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center;'>Built with ❤️ using Streamlit | 2025 Museum Tech Hackathon</p>", unsafe_allow_html=True)








# import streamlit as st
# from PIL import Image

# # Optional: Load a banner image if you have it
# # st.image("assets/images/banner.jpg", use_column_width=True)

# # Set page config
# st.set_page_config(page_title="Museum Tour Management System", layout="wide")

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



# # --- Title & Introduction ---
# st.markdown("<h1 style='text-align: center; color: #004080;'>🏛️ Museum Tour Management System</h1>", unsafe_allow_html=True)
# st.markdown("### A Smart, AI-Integrated Museum Experience Platform")
# st.write("""
# Welcome to the Museum Tour Management System! This platform is designed to provide seamless experiences for **Visitors** and powerful tools for **Admins** to manage tours, exhibits, and visitor data effectively.
# """)

# st.markdown("---")

# # --- Project Overview Section ---
# with st.expander("📌 **Project Overview**"):
#     st.markdown("""
# The system is divided into two main user types:

# ### 👨‍💼 Admin:
# - Manage Exhibits and Tours
# - Analyze Visitor Data and Reviews
# - Use ML for Bookings and Recommendations
# - Respond to Visitor Feedback
# - Access Smart Dashboard with Map and Stats

# ### 🙋 Visitor:
# - Explore Museum Exhibits
# - Book and Manage Tour Visits
# - Rate and Review Tours
# - Get Personalized Recommendations

# This project includes an interactive chatbot, ML modules, and a full analytics dashboard powered by real datasets!
# """)

# # --- Buttons to navigate to login pages ---
# st.markdown("### 🔐 Choose User Type to Proceed:")
# col1, col2 = st.columns(2)

# with col1:
#     if st.button("🙋 Visitor Login"):
#         # st.session_state["user_type"] = "visitor"
#         #st.switch_page("VisitorLogin.py")  # You must have this script
#         st.switch_page("pages/1_Visitor_Login.py")  #aksjdfbmnbsakjdfh

# with col2:
#     if st.button("👨‍💼 Admin Login"):
#         # st.session_state["user_type"] = "admin"
#         #st.switch_page("AdminLogin.py")  # You must have this script in the same directory or pages folder
#         st.switch_page("pages/2_Admin_Login.py")

# # --- Footer ---
# st.markdown("---")
# st.markdown("<p style='text-align: center;'>Built with ❤️ using Streamlit | 2025 Museum Tech Hackathon</p>", unsafe_allow_html=True)


# # import streamlit as st

# # st.set_page_config(page_title="🏛 Museum Management System", layout="centered")

# # st.markdown("""
# #     <style>
# #         [data-testid="stSidebar"] {
# #             display: none;
# #         }
# #         [data-testid="collapsedControl"] {
# #             display: none;
# #         }
# #     </style>
# # """, unsafe_allow_html=True)

# # st.markdown("<h1 style='text-align:center; color:#08fdd8;'>🏛 Welcome to the Virtual Museum</h1>", unsafe_allow_html=True)
# # st.markdown("<h4 style='text-align:center;'>Explore. Experience. Evolve.</h4>", unsafe_allow_html=True)

# # st.image("assets/images/banner.jpg", use_column_width=True)

# # st.markdown("### Login Options:")
# # col1, col2 = st.columns(2)

# # with col1:
# #     if st.button("👤 Visitor Login"):
# #         st.switch_page("pages/1_Visitor_Login.py")

# # with col2:
# #     if st.button("🛠 Admin Login"):
# #         st.switch_page("pages/2_Admin_Login.py")
