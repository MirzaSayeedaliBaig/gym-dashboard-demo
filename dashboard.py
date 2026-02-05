import streamlit as st
import pandas as pd
import numpy as np

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="FitLife Admin", layout="wide")

# --- AUTHENTICATION BLOCK (Simple Password) ---
# This creates a sidebar password box
password = st.sidebar.text_input("Enter Admin Password", type="password")

# CHANGE 'mypassword123' to whatever you want
if password != "mypassword123":
    st.info("🔒 Please enter the password to view the dashboard.")
    st.stop()  # This stops the app from loading until password is correct

st.success("✅ Login Successful!")

# --- DASHBOARD LOGIC STARTS HERE ---

# 2. GENERATE FAKE DATA
def get_data():
    dates = pd.date_range(start="2026-01-01", periods=30)
    data = pd.DataFrame({
        'Date': dates,
        'Website_Visits': np.random.randint(50, 200, size=30),
        'Signups': np.random.randint(5, 25, size=30),
        'Source': np.random.choice(['Instagram Ads', 'Google Search', 'Walk-in'], size=30)
    })
    return data

df = get_data()

# 3. DASHBOARD HEADER
st.title("📊 FitLife Gym - Owner Dashboard")
st.markdown("Welcome back! Here is how your **'30-Day Challenge'** landing page is performing.")
st.markdown("---")

# 4. KEY METRICS
total_visits = df['Website_Visits'].sum()
total_signups = df['Signups'].sum()
conversion_rate = round((total_signups / total_visits) * 100, 2)

col1, col2, col3 = st.columns(3)
col1.metric("Total Visitors", f"{total_visits}", "+12%")
col2.metric("New Leads", f"{total_signups}", "+8%")
col3.metric("Conversion Rate", f"{conversion_rate}%", "4% above target")

st.markdown("---")

# 5. CHARTS
st.subheader("📈 Traffic Trend (Last 30 Days)")
st.line_chart(df.set_index('Date')[['Website_Visits', 'Signups']])

st.subheader("🎯 Where are your customers coming from?")
source_counts = df['Source'].value_counts()
st.bar_chart(source_counts)

# 6. SIDEBAR FILTERS
st.sidebar.header("Filter Data")
st.sidebar.slider("Date Range", 1, 30, 30)