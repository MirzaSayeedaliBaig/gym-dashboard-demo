import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Novanode Client Dashboard",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------------------------
# 2. AUTHENTICATION (The Lock)
# ---------------------------------------------------------
# This creates a sidebar password box.
# For the demo, the password is: admin123
password = st.sidebar.text_input("Enter Admin Password", type="password")

if password != "admin123":
    st.info("🔒 Please enter the password to access the Novanode Dashboard.")
    st.stop()  # Stops the app here if password is wrong

st.sidebar.success("✅ Access Granted")

# ---------------------------------------------------------
# 3. HELPER FUNCTIONS (The Brains)
# ---------------------------------------------------------

# Function to generate fake Marketing Data
def get_marketing_data():
    dates = pd.date_range(start="2026-01-01", periods=30)
    data = pd.DataFrame({
        'Date': dates,
        'Website_Visits': np.random.randint(50, 200, size=30),
        'Signups': np.random.randint(5, 25, size=30),
        'Source': np.random.choice(['Instagram Ads', 'Google Search', 'Walk-in'], size=30)
    })
    return data

# Function to write the "AI Summary" paragraph
def generate_smart_summary(df):
    total_visits = df['Website_Visits'].sum()
    total_signups = df['Signups'].sum()
    conversion_rate = round((total_signups / total_visits) * 100, 2)
    target_rate = 5.0 
    
    summary = f"**Executive Summary:**\n\n"
    summary += f"This month, the landing page received **{total_visits} visitors**. "
    
    if conversion_rate >= target_rate:
        summary += f"You are converting at **{conversion_rate}%**, which is excellent! "
        summary += "Recommendation: **Scale up your ad budget**."
    else:
        summary += f"However, your conversion rate is **{conversion_rate}%** (Target: 5%). "
        summary += "Recommendation: **Review pricing or page headlines**."

    top_source = df['Source'].mode()[0]
    summary += f"\n\n**Top Channel:** Most customers are coming from **{top_source}**."
    return summary

# ---------------------------------------------------------
# 4. MAIN APP LAYOUT
# ---------------------------------------------------------

st.title("🚀 Novanode Analytics | Client Portal")
st.markdown("### FitLife Gym - Hyderabad")

# Create the Two Main Tabs
tab1, tab2 = st.tabs(["📈 Marketing Intelligence", "💰 Financial HQ"])

# =========================================================
# TAB 1: MARKETING
# =========================================================
with tab1:
    st.header("Marketing Performance")
    
    # Load Data
    df_marketing = get_marketing_data()
    
    # 1. Key Metrics Row
    total_visits = df_marketing['Website_Visits'].sum()
    total_signups = df_marketing['Signups'].sum()
    conv_rate = round((total_signups / total_visits) * 100, 2)

    m_col1, m_col2, m_col3 = st.columns(3)
    m_col1.metric("Total Visitors", f"{total_visits}", "+12%")
    m_col2.metric("New Leads", f"{total_signups}", "+8%")
    m_col3.metric("Conversion Rate", f"{conv_rate}%", "4% above target")

    st.divider()

    # 2. Charts
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.subheader("Traffic vs Leads")
        st.line_chart(df_marketing.set_index('Date')[['Website_Visits', 'Signups']])
        
    with col_chart2:
        st.subheader("Traffic Sources")
        st.bar_chart(df_marketing['Source'].value_counts())

    # 3. AI Insights Box
    st.subheader("🤖 Novanode Analyst Insights")
    st.info(generate_smart_summary(df_marketing))


# =========================================================
# TAB 2: FINANCE (For You & Your Friend)
# =========================================================
with tab2:
    st.header("Financial Command Center")
    
    # 1. Transaction Input Form
    with st.expander("➕ Add New Expense / Income", expanded=False):
        with st.form("finance_form"):
            f_col1, f_col2, f_col3 = st.columns(3)
            date = f_col1.date_input("Date")
            t_type = f_col2.selectbox("Type", ["Expense", "Income"])
            category = f_col3.selectbox("Category", ["Rent", "Salaries", "Ads", "Utilities", "Sales", "Consulting"])
            
            amount = st.number_input("Amount (₹)", min_value=0, step=100)
            note = st.text_input("Description / Notes")
            
            submitted = st.form_submit_button("Save Transaction")
            if submitted:
                st.success(f"✅ Saved: ₹{amount} for {category} ({t_type})")
                # NOTE: This connects to Google Sheets in the live version
    
    st.divider()

    # 2. Fake Finance Data (Demo Mode)
    # We create dummy data to show the client what it LOOKS like
    fin_data = pd.DataFrame({
        'Category': ['Rent', 'Salaries', 'Ads', 'Gym Memberships', 'Personal Training', 'Utilities'],
        'Type': ['Expense', 'Expense', 'Expense', 'Income', 'Income', 'Expense'],
        'Amount': [15000, 25000, 5000, 55000, 30000, 2000]
    })
    
    # 3. Financial Logic
    total_income = fin_data[fin_data['Type'] == 'Income']['Amount'].sum()
    total_expense = fin_data[fin_data['Type'] == 'Expense']['Amount'].sum()
    net_profit = total_income - total_expense
    
    # 4. Financial Metrics
    f_metric1, f_metric2, f_metric3 = st.columns(3)
    f_metric1.metric("Total Revenue", f"₹{total_income}", "High Season")
    f_metric2.metric("Total
