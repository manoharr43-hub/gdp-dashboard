import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px

st.set_page_config(page_title="🔥 TG JEE + Trading App", layout="wide")

# =============================
# SIDEBAR MENU
# =============================
menu = st.sidebar.selectbox(
    "Select Feature",
    ["🏠 Home", "📚 JEE Subjects", "📝 Quiz", "📈 Stock Viewer"]
)

# =============================
# HOME
# =============================
if menu == "🏠 Home":
    st.title("🔥 TG JEE + Trading App")
    st.write("All-in-One Learning + Stock Analysis Platform 🚀")

# =============================
# JEE SUBJECTS
# =============================
elif menu == "📚 JEE Subjects":
    st.title("📚 JEE Subjects")

    subject = st.selectbox("Choose Subject", ["Physics", "Chemistry", "Maths"])

    topics = {
        "Physics": ["Kinematics", "Laws of Motion", "Thermodynamics"],
        "Chemistry": ["Organic", "Inorganic", "Physical"],
        "Maths": ["Algebra", "Calculus", "Trigonometry"]
    }

    if subject:
        st.subheader(f"{subject} Topics")
        for t in topics[subject]:
            st.write(f"👉 {t}")

# =============================
# QUIZ SECTION
# =============================
elif menu == "📝 Quiz":
    st.title("📝 JEE Quiz")

    question = "What is 2 + 2?"
    options = ["3", "4", "5"]

    answer = st.radio(question, options)

    if st.button("Submit"):
        if answer == "4":
            st.success("Correct ✅")
        else:
            st.error("Wrong ❌")

# =============================
# STOCK VIEWER
# =============================
elif menu == "📈 Stock Viewer":
    st.title("📈 Live Stock Viewer")

    stock = st.text_input("Enter Stock Symbol (e.g. RELIANCE.NS)", "RELIANCE.NS")

    if st.button("Fetch Data"):
        try:
            data = yf.download(stock, period="1mo")

            if data.empty:
                st.error("No data found ❌")
            else:
                st.success("Data Loaded ✅")

                st.dataframe(data.tail())

                fig = px.line(data, y="Close", title=f"{stock} Price")
                st.plotly_chart(fig)

        except Exception as e:
            st.error(f"Error: {e}")
