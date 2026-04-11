import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
import json
from datetime import datetime

st.set_page_config(page_title="🔥 TG JEE + AI Trading App", layout="wide")

# =============================
# LOAD QUIZ DATA
# =============================
def load_quiz():
    try:
        with open("quiz_data.json", "r") as f:
            return json.load(f)
    except:
        return []

quiz_data = load_quiz()

# =============================
# SIDEBAR
# =============================
menu = st.sidebar.selectbox(
    "Select Feature",
    ["🏠 Home", "📚 JEE Subjects", "📝 Quiz", "📊 Performance", "📈 AI Trading"]
)

# =============================
# HOME
# =============================
if menu == "🏠 Home":
    st.title("🔥 TG JEE + AI Trading App")
    st.write("JEE Preparation + Stock Market AI System 🚀")

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

    st.subheader(f"{subject} Topics")
    for t in topics[subject]:
        st.write(f"👉 {t}")

# =============================
# QUIZ
# =============================
elif menu == "📝 Quiz":
    st.title("📝 JEE Quiz")

    if quiz_data:
        q = quiz_data[0]
        answer = st.radio(q["question"], q["options"])

        if st.button("Submit"):
            if answer == q["answer"]:
                st.success("Correct ✅")
                st.session_state["score"] = st.session_state.get("score", 0) + 1
            else:
                st.error("Wrong ❌")
    else:
        st.warning("No quiz data found")

# =============================
# PERFORMANCE
# =============================
elif menu == "📊 Performance":
    st.title("📊 Your Performance")

    score = st.session_state.get("score", 0)
    st.metric("Score", score)

# =============================
# AI TRADING
# =============================
elif menu == "📈 AI Trading":
    st.title("📈 AI Stock Analyzer")

    stock = st.text_input("Enter Stock Symbol", "RELIANCE.NS")

    if st.button("Analyze"):
        try:
            df = yf.download(stock, period="3mo")

            if df.empty:
                st.error("No data found ❌")
            else:
                # Moving Average
                df["MA20"] = df["Close"].rolling(20).mean()
                df["MA50"] = df["Close"].rolling(50).mean()

                last = df.iloc[-1]

                # Trend Logic
                if last["MA20"] > last["MA50"]:
                    signal = "BUY 📈"
                else:
                    signal = "SELL 📉"

                st.success(f"Signal: {signal}")

                # Chart
                fig = go.Figure()
                fig.add_trace(go.Scatter(y=df["Close"], name="Close"))
                fig.add_trace(go.Scatter(y=df["MA20"], name="MA20"))
                fig.add_trace(go.Scatter(y=df["MA50"], name="MA50"))

                st.plotly_chart(fig)

                st.dataframe(df.tail())

        except Exception as e:
            st.error(f"Error: {e}")
