import streamlit as st

st.set_page_config(page_title="TrustLayer AI", layout="centered")

st.title(" TrustLayer")
st.subheader("Real-Time Financial Fraud Intelligence System")

st.write("""
TrustLayer detects scams, suspicious transactions, and financial fraud patterns using AI + community intelligence.
""")

# Demo dashboard (replace later with real data if needed)
st.metric("Messages Analyzed", "128")
st.metric("High Risk Alerts", "14")

st.markdown("###  Live System Output")

st.warning(" Investment scam detected — Risk Score: 92%")
st.error(" Urgent money request flagged as HIGH RISK")
st.success(" Normal conversation detected — Safe")

st.markdown("###  Community Intelligence")
st.info("3 users reported similar scam pattern in the last 24h")
