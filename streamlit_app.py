import streamlit as st
import json
import random

st.set_page_config(page_title="JEE Quiz App", layout="centered")

st.title("📘 JEE Prep: AI Quiz Master")

# Load JSON Data
@st.cache_data
def load_data():
    try:
        # Using a raw string for the path is good practice
        with open(r"C:\Users\User\Desktop\all_jee_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("❌ JSON file not found. Check the path.")
        return []

data = load_data()

if not data:
    st.stop()

# --- Session State Initialization ---
if "score" not in st.session_state:
    st.session_state.score = 0
if "q_index" not in st.session_state:
    # Use index-based tracking for better control
    st.session_state.current_q = random.choice(data)
if "answered" not in st.session_state:
    st.session_state.answered = False
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# --- Helper Functions ---
def next_question():
    st.session_state.current_q = random.choice(data)
    st.session_state.answered = False
    st.session_state.feedback = ""
    # Clear the input text by using a key (see text_input below)
    if "user_input" in st.session_state:
        st.session_state.user_input = ""

# --- UI Layout ---
st.subheader("📖 Question")
st.info(st.session_state.current_q.get("text", "No question text found."))

# If your JSON has images for math/physics diagrams:
if "image_url" in st.session_state.current_q:
    st.image(st.session_state.current_q["image_url"])

# Answer Input
user_ans = st.text_input("✍ Type your answer here:", key="user_input")

col1, col2 = st.columns([1, 4])

with col1:
    if st.button("✅ Submit"):
        if user_ans and not st.session_state.answered:
            # Assumes your JSON has a key called 'correct_answer'
            correct_ans = str(st.session_state.current_q.get("answer", "")).strip().lower()
            
            if user_ans.strip().lower() == correct_ans:
                st.session_state.score += 1
                st.session_state.feedback = "correct"
            else:
                st.session_state.feedback = "wrong"
            
            st.session_state.answered = True
        elif st.session_state.answered:
            st.warning("Already submitted!")
        else:
            st.warning("Please enter an answer.")

with col2:
    if st.button("➡ Next Question"):
        next_question()
        st.rerun()

# --- Feedback & Explanations ---
if st.session_state.feedback == "correct":
    st.success(f"🔥 Correct! The answer was: {st.session_state.current_q.get('answer')}")
elif st.session_state.feedback == "wrong":
    st.error(f"❌ Incorrect. The correct answer was: {st.session_state.current_q.get('answer')}")

# Show explanation if available in JSON
if st.session_state.answered and "explanation" in st.session_state.current_q:
    with st.expander("See Detailed Explanation"):
        st.write(st.session_state.current_q["explanation"])

st.divider()
st.write(f"### 🏆 Current Score: {st.session_state.score}")
