try:
    from supabase import create_client
except Exception as e:
    import streamlit as st
    st.error("Supabase failed to load. Check requirements.txt deployment.")
    st.stop()

import streamlit as st
from supabase import create_client
import pandas as pd

# -----------------------------
# CONFIG
# -----------------------------
SUPABASE_URL = "https://yiuxfjpemkslzmvyshce.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpdXhmanBlbWtzbHptdnlzaGNlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY4MTI2NjgsImV4cCI6MjA5MjM4ODY2OH0.wW5xGxR5sT_Qdq54eKPzYZupxsV5LHGqlabemyzqwnA"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="TrustLayer Dashboard", layout="centered")

st.title(" TrustLayer Dashboard")
st.subheader("Real-Time Fraud Intelligence System")

# -----------------------------
# FETCH DATA
# -----------------------------
data = supabase.table("message").select("*").execute()
messages = data.data if data.data else []

if not messages:
    st.warning("No data yet. Send messages via Telegram bot.")
    st.stop()

df = pd.DataFrame(messages)

# -----------------------------
# METRICS
# -----------------------------
total = len(df)
high_risk = len(df[df["risk"] >= 70])
suspicious = len(df[(df["risk"] >= 40) & (df["risk"] < 70)])
safe = len(df[df["risk"] < 40])

st.metric("Messages Analyzed", total)
st.metric("High Risk Alerts", high_risk)
st.metric("Suspicious Cases", suspicious)
st.metric("Safe Messages", safe)

# -----------------------------
# RISK DISTRIBUTION (VISUAL)
# -----------------------------
st.markdown("###  Risk Distribution")

chart_data = pd.DataFrame({
    "Category": ["Safe", "Suspicious", "Scam"],
    "Count": [safe, suspicious, high_risk]
})

st.bar_chart(chart_data.set_index("Category"))

# -----------------------------
# RECENT MESSAGES
# -----------------------------
st.markdown("### 📩 Recent Activity")

for m in df.tail(10).iloc[::-1].to_dict("records"):
    text = m.get("text", "")
    risk = m.get("risk", 0)

    if risk >= 70:
        st.error(f" {text} (Risk: {risk})")
    elif risk >= 40:
        st.warning(f" {text} (Risk: {risk})")
    else:
        st.success(f" {text} (Risk: {risk})")
