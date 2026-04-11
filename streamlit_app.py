import streamlit as st
import json
import random

st.set_page_config(page_title="JEE Quiz App", layout="centered")

st.title("📘 JEE Quiz App (AI Powered)")

# Load JSON
with open(r"C:\Users\User\Desktop\all_jee_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Check data
if len(data) == 0:
    st.error("❌ No data found in JSON")
    st.stop()

# Session state
if "score" not in st.session_state:
    st.session_state.score = 0

if "question" not in st.session_state:
    st.session_state.question = random.choice(data)

if "answered" not in st.session_state:
    st.session_state.answered = False

# Show Question
st.write("### 📖 Question:")
st.info(st.session_state.question["text"])

# Answer input
user_ans = st.text_input("✍ Enter your answer:")

# Submit
if st.button("✅ Submit Answer") and not st.session_state.answered:
    st.session_state.answered = True

    # Simple check (basic match)
    if user_ans.strip().lower() in st.session_state.question["text"].lower():
        st.success("✅ Correct (approx match)")
        st.session_state.score += 1
    else:
        st.error("❌ Answer submitted (manual check needed)")

# Next Question
if st.button("➡ Next Question"):
    st.session_state.question = random.choice(data)
    st.session_state.answered = False

# Score display
st.write(f"### 🏆 Score: {st.session_state.score}")
