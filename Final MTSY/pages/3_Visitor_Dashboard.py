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
            
    [data-testid="stSidebar"] {
        display: none;
    }
    [data-testid="collapsedControl"] {
        display: none;
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
