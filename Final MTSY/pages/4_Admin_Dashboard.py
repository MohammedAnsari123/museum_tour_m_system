import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config("Museum_Tour_Management_System", layout="wide")

if 'tours' not in st.session_state:
    st.session_state['tours'] = pd.DataFrame(columns=['Tour ID', 'Name', 'Guide', 'Time', 'Capacity'])

if 'bookings' not in st.session_state:
    st.session_state['bookings'] = pd.DataFrame(columns=['Booking ID', 'Visitor Name', 'Tour Name', 'Status'])

if 'feedback' not in st.session_state:
    st.session_state['feedback'] = pd.DataFrame(columns=['Visitor Name', 'Message'])

if 'exhibits' not in st.session_state:
    st.session_state['exhibits'] = pd.DataFrame(columns=['Exhibit ID', 'Name', 'Description'])

st.markdown("""
    <style>
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    .card h1 {
        font-size: 28px;
        color: #2c3e50;
    }
    .card span {
        font-size: 14px;
        color: #7f8c8d;
    }
    [data-testid="stSidebar"] {
        display: none;
    }
    [data-testid="collapsedControl"] {
        display: none;
    }

    </style>
""", unsafe_allow_html=True)

menu = st.selectbox("Navigation", ["Dashboard", "Manage Exhibit", "Manage Tours", "View Analytics", "Review Feedback"])

if menu == "Dashboard":
    st.title("🏛 Admin Dashboard")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""<div class='card'><h1>{len(st.session_state['tours'])}</h1><span>Total Tours</span></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class='card'><h1>{len(st.session_state['bookings'])}</h1><span>Total Bookings</span></div>""", unsafe_allow_html=True)
    with col3:
        total_visitors = st.session_state['bookings']['Visitor Name'].nunique()
        st.markdown(f"""<div class='card'><h1>{total_visitors}</h1><span>Total Visitors</span></div>""", unsafe_allow_html=True)
    with col4:
        st.markdown(f"""<div class='card'><h1>{len(st.session_state['feedback'])}</h1><span>Feedbacks</span></div>""", unsafe_allow_html=True)

elif menu == "Manage Exhibit":
    st.title("🖼 Manage Exhibits")
    with st.form("Add Exhibit"):
        eid = st.text_input("Exhibit ID")
        name = st.text_input("Exhibit Name")
        desc = st.text_area("Description")
        submit = st.form_submit_button("Add Exhibit")
        if submit:
            new_row = {'Exhibit ID': eid, 'Name': name, 'Description': desc}
            st.session_state['exhibits'] = pd.concat([st.session_state['exhibits'], pd.DataFrame([new_row])], ignore_index=True)
            st.success("Exhibit added successfully!")
    st.subheader("Existing Exhibits")
    st.dataframe(st.session_state['exhibits'])

elif menu == "Manage Tours":
    st.title("🎫 Manage Tours")
    with st.form("Add Tour"):
        tid = st.text_input("Tour ID")
        name = st.text_input("Tour Name")
        guide = st.text_input("Guide Name")
        time = st.time_input("Tour Time")
        capacity = st.number_input("Capacity", min_value=1)
        submit = st.form_submit_button("Add Tour")
        if submit:
            new_row = {'Tour ID': tid, 'Name': name, 'Guide': guide, 'Time': time, 'Capacity': capacity}
            st.session_state['tours'] = pd.concat([st.session_state['tours'], pd.DataFrame([new_row])], ignore_index=True)
            st.success("Tour added successfully!")
    st.subheader("Existing Tours")
    st.dataframe(st.session_state['tours'])

elif menu == "View Analytics":
    st.title("📊 Booking Analytics")
    if len(st.session_state['bookings']) > 0:
        fig, ax = plt.subplots()
        st.session_state['bookings']['Tour Name'].value_counts().plot(kind='bar', ax=ax, color='#3498db')
        ax.set_xlabel("Tour Name")
        ax.set_ylabel("Number of Bookings")
        ax.set_title("Bookings per Tour")
        st.pyplot(fig)
    else:
        st.info("No booking data available to display charts.")

elif menu == "Review Feedback":
    st.title("💬 Visitor Feedback")
    st.dataframe(st.session_state['feedback'])
