# import streamlit as st
# from PIL import Image

# banner1 = Image.open("i1")  # Dark theme
# banner2 = Image.open("i2")  # Yellow-modern
# banner3 = Image.open("i3")  # Elegant black

# st.set_page_config(page_title="My Museum", layout="wide")

# st.markdown("<h1 style='text-align: center; color: navy;'>🏛 Welcome to Our Museum</h1>", unsafe_allow_html=True)
# st.markdown("<h4 style='text-align: center; font-weight: normal;'>Explore. Experience. Evolve.</h4>", unsafe_allow_html=True)
# st.markdown("---")

# # ---- IMAGE GALLERY SECTION ----
# st.image(banner1, use_column_width=True)
# st.markdown("<h3 style='color: white; background-color: #003366; padding: 10px;'>Elusive. Powerful. Preserved. Visit Our Deep Sea Exhibit</h3>", unsafe_allow_html=True)

# # ---- GRID IMAGE SECTION ----
# col1, col2 = st.columns(2)
# with col1:
#     st.image(banner2, use_column_width=True)
#     st.markdown("<h5 style='color: black;'>Discover over 100 unique exhibits blending culture, history, and innovation.</h5>", unsafe_allow_html=True)
# with col2:
#     st.image(banner3, use_column_width=True)
#     st.markdown("<h5 style='color: #444;'>Experience two million years of heritage, brought to life in our special galleries.</h5>", unsafe_allow_html=True)

# st.markdown("---")

# # ---- LOGIN SECTION ----
# st.markdown("<h2 style='text-align: center;'>🔐 Login</h2>", unsafe_allow_html=True)
# login_tab1, login_tab2 = st.tabs(["👤 Visitor", "🛠 Admin"])

# with login_tab1:
#     username = st.text_input("Enter Visitor Username")
#     password = st.text_input("Enter Visitor Password", type="password")
#     if st.button("Login as Visitor"):
#         if username == "guest" and password == "123":
#             st.success("Welcome! Enjoy exploring our exhibitions.")
#         else:
#             st.error("Incorrect visitor credentials.")

# with login_tab2:
#     admin_user = st.text_input("Enter Admin Username")
#     admin_pass = st.text_input("Enter Admin Password", type="password")
#     if st.button("Login as Admin"):
#         if admin_user == "admin" and admin_pass == "admin123":
#             st.success("Admin access granted.")
#         else:
#             st.error("Invalid admin credentials.")

# # ---- FOOTER ----
# st.markdown("---")
# st.markdown("<p style='text-align: center;'>📍 Museum Address: 123 Museum Avenue, Your City</p>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center; color: gray;'>Design inspired by world-class museums</p>", unsafe_allow_html=True)
# import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd

# st.set_page_config(page_title="Visitor Dashboard", layout="wide")

# st.markdown("<h1 style='text-align:center; color: teal;'>🎫 Visitor Dashboard</h1>", unsafe_allow_html=True)
# st.markdown("---")

# # Sidebar Navigation
# menu = st.sidebar.radio("📂 Navigation", ["Analytics", "Manage Booked Tours", "Browse Exhibitions & Tours", "Recommendations"])

# # ---- SECTION 1: Analytics ----
# if menu == "Analytics":
#     st.subheader("📊 Visitor Analysis")

#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown("#### Indian vs Foreign Visitors")
#         visitor_data = {"Indian": 620, "Foreign": 380}
#         fig1, ax1 = plt.subplots()
#         ax1.pie(visitor_data.values(), labels=visitor_data.keys(), autopct='%1.1f%%', startangle=90)
#         ax1.axis('equal')
#         st.pyplot(fig1)

#     with col2:
#         st.markdown("#### Most Visited Museums")
#         museum_data = {"History Museum": 300, "Art Gallery": 240, "Science Museum": 400, "Heritage Hall": 180}
#         fig2, ax2 = plt.subplots()
#         ax2.bar(museum_data.keys(), museum_data.values(), color='orange')
#         plt.xticks(rotation=15)
#         st.pyplot(fig2)

# # ---- SECTION 2: Manage Booked Tours ----
# elif menu == "Manage Booked Tours":
#     st.subheader("🗓 Manage Your Booked Tours")

#     option = st.selectbox("Choose Action", ["View My Bookings", "Reschedule Tour", "Cancel Tour"])

#     if option == "View My Bookings":
#         st.info("🔎 Booking ID: #A12345\n\nTour: Art & Sculpture\nDate: 20th July\nTime: 11:00 AM\nPeople: 2")

#     elif option == "Reschedule Tour":
#         st.date_input("Select New Date")
#         st.time_input("Select New Time")
#         if st.button("Reschedule"):
#             st.success("Tour rescheduled successfully!")

#     elif option == "Cancel Tour":
#         st.text_input("Enter Booking ID to Cancel")
#         if st.button("Cancel"):
#             st.warning("Tour has been canceled.")

# # ---- SECTION 3: Browse Exhibitions & Tours ----
# elif menu == "Browse Exhibitions & Tours":
#     st.subheader("🖼 Browse Exhibitions & Book Tours")

#     browse_option = st.radio("Explore Options", ["View Exhibit Details", "Book a Tour"])

#     if browse_option == "View Exhibit Details":
#         st.image("https://upload.wikimedia.org/wikipedia/commons/6/69/Louvre_Museum_Wikimedia_Commons.jpg", caption="Featured Exhibit: Ancient Arts")
#         st.write("This exhibit displays ancient artifacts from different civilizations with audio guides and interactive screens.")

#     elif browse_option == "Book a Tour":
#         date = st.date_input("Choose Date")
#         time = st.time_input("Choose Time")
#         people = st.number_input("Number of People", min_value=1, step=1)
#         if st.button("Confirm Booking"):
#             st.success("🎉 Booking Confirmed!")
#             st.balloons()
#         if st.button("Rate & Review Tour"):
#             st.text_area("Write your review here...")
#             st.success("Thank you for your feedback!")

# # ---- SECTION 4: Recommendations ----
# elif menu == "Recommendations":
#     st.subheader("🤖 ML-Driven Recommendations")

#     st.markdown("### 🎯 Personalized Museum Suggestions")
#     st.write("- Heritage Trail Tour")
#     st.write("- Time Capsule Exhibit")
#     st.write("- Sculpture Walk")

#     st.markdown("### 🔥 Popular Exhibits")
#     st.write("- Space Science Dome")
#     st.write("- Ancient Egypt Mummies")
#     st.write("- AI & Robotics Lab")

#     st.markdown("### 📍 Nearby Museums (via API)")
#     st.info("📍 City Museum - 2.1 km\n📍 Innovation Gallery - 3.7 km\n📍 Craft & Culture Museum - 5.4 km")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="🎫 Virtual Museum Dashboard", layout="wide")

# ---------- CSS Styling ----------
st.markdown("""
    <style>
    .title {
        font-size: 45px;
        text-align: center;
        color: #08fdd8;
        margin-bottom: 0px;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #a78bfa;
        margin-bottom: 40px;
    }
    .card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;
    }
    .section-title {
        font-size: 28px;
        color: #f3f4f6;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("<div class='title'>🖼 Virtual Museum Visitor Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Explore. Experience. Evolve.</div>", unsafe_allow_html=True)

# ---------- Tabs ----------
tab1, tab2, tab3, tab4 = st.tabs(["📊 Analytics", "🗓 Bookings", "🖼 Exhibitions", "🤖 Recommendations"])

# ---------- Tab 1: Analytics ----------
with tab1:
    st.markdown("<div class='section-title'>📈 Visitor Statistics</div>", unsafe_allow_html=True)
    with st.container():
        col1, col2, col3 = st.columns(3)
        col1.metric("👥 Total Visitors", "1,200", "+7%")
        col2.metric("🇮🇳 Indian Visitors", "820", "+5%")
        col3.metric("🌍 Foreign Visitors", "380", "+12%")

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 🌐 Visitor Distribution")
            fig1, ax = plt.subplots()
            ax.pie([820, 380], labels=["Indian", "Foreign"], autopct="%1.1f%%", startangle=140)
            ax.axis("equal")
            st.pyplot(fig1)

        with col2:
            st.markdown("#### 🏛 Top Museums")
            data = pd.DataFrame({
                "Museum": ["Art Gallery", "Science Hall", "Ancient India"],
                "Visitors": [450, 600, 300]
            })
            fig2 = px.bar(data, x="Museum", y="Visitors", color="Museum",
                          color_discrete_sequence=px.colors.sequential.Rainbow)
            st.plotly_chart(fig2)

# ---------- Tab 2: Bookings ----------
with tab2:
    st.markdown("<div class='section-title'>🗓 Manage Booked Tours</div>", unsafe_allow_html=True)

    action = st.selectbox("Choose Action", ["📄 View My Bookings", "🔁 Reschedule Tour", "❌ Cancel Tour"])

    if action == "📄 View My Bookings":
        with st.container():
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.success("🎫 Booking ID: A1234\n\n📍 Exhibit: Sculpture Gallery\n📅 Date: July 22\n⏰ Time: 3:00 PM\n👥 Visitors: 2")
            st.markdown("</div>", unsafe_allow_html=True)

    elif action == "🔁 Reschedule Tour":
        with st.container():
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            new_date = st.date_input("📅 Select New Date")
            new_time = st.time_input("⏰ Select New Time")
            if st.button("✅ Confirm Reschedule"):
                st.success(f"Tour rescheduled to {new_date} at {new_time}")
            st.markdown("</div>", unsafe_allow_html=True)

    elif action == "❌ Cancel Tour":
        with st.container():
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            cancel_id = st.text_input("🔐 Enter Booking ID")
            if st.button("⚠ Cancel Tour"):
                st.warning("Booking canceled.")
            st.markdown("</div>", unsafe_allow_html=True)

# ---------- Tab 3: Exhibitions ----------
with tab3:
    st.markdown("<div class='section-title'>🖼 Browse Exhibitions & Book Tours</div>", unsafe_allow_html=True)
    exhibit_tab = st.radio("Select an Option", ["🎨 View Exhibits", "📅 Book a Tour"])

    if exhibit_tab == "🎨 View Exhibits":
        with st.container():
            st.image("https://upload.wikimedia.org/wikipedia/commons/6/69/Louvre_Museum_Wikimedia_Commons.jpg",
                     caption="✨ Ancient Artifacts", use_column_width=True)
            st.info("🧾 Discover ancient tools, stories, and scrolls from lost civilizations.")

    elif exhibit_tab == "📅 Book a Tour":
        with st.container():
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.date_input("📅 Choose Date")
            st.time_input("⏰ Choose Time")
            st.slider("👥 Number of Visitors", 1, 10)
            if st.button("🎫 Confirm Booking"):
                st.success("Tour booked successfully!")
            if st.button("⭐ Rate Exhibit"):
                st.text_area("Your Feedback")
                st.success("Thanks for your review!")
            st.markdown("</div>", unsafe_allow_html=True)

# ---------- Tab 4: Recommendations ----------
with tab4:
    st.markdown("<div class='section-title'>🤖 AI-Based Recommendations</div>", unsafe_allow_html=True)
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("#### 🎯 Personalized")
            st.success("• Robotics Lab\n• Temple Trail\n• VR Time Travel")

        with col2:
            st.markdown("#### 🔥 Trending")
            st.info("• Submarine Journey\n• Cultural Kaleidoscope\n• Quantum Playground")

        with col3:
            st.markdown("#### 📍 Nearby Museums")
            st.warning("• Science World – 1.8 km\n• Craft Hub – 3.2 km\n• Kids Art House – 5.1 km")