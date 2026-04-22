import streamlit as st
import random

st.title(" TrustLayer Dashboard")

messages = random.randint(100, 200)
scams = random.randint(10, 30)

st.metric("Messages Analyzed", messages)
st.metric("High Risk Alerts", scams)

st.warning(" Investment scam detected — Risk Score: 92%")
