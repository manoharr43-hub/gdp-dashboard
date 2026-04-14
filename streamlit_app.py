import streamlit as st
import json
import random

# పేజీ టైటిల్
st.set_page_config(page_title="JEE Quiz App", layout="centered")
st.title("📘 JEE Quiz App (AI Powered)")

# JSON డేటాను లోడ్ చేయడం
@st.cache_data
def load_data():
    try:
        # మీరు GitHubలో పెట్టిన ఫైల్ పేరు ఇక్కడ ఉంది
        with open("all_jee_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("❌ 'all_jee_data.json' ఫైల్ దొరకలేదు.")
        return []
    except Exception as e:
        st.error(f"❌ ఎర్రర్: {e}")
        return []

data = load_data()

if not data:
    st.stop()

# --- Session State ---
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_q" not in st.session_state:
    st.session_state.current_q = random.choice(data)
if "answered" not in st.session_state:
    st.session_state.answered = False

# --- ప్రశ్నను చూపించడం ---
st.write("---")
st.subheader("📖 ప్రశ్న:")
st.info(st.session_state.current_q.get("text", "ప్రశ్న లోడ్ కాలేదు"))

# ఆన్సర్ ఇన్పుట్
user_ans = st.text_input("✍ మీ సమాధానాన్ని టైప్ చేయండి:", key="user_input")

col1, col2 = st.columns(2)

with col1:
    if st.button("✅ Submit"):
        if user_ans and not st.session_state.answered:
            # ఇక్కడ 'answer' అనేది మీ JSON లో ఉన్న కీ పేరు అని గమనించండి
            correct = str(st.session_state.current_q.get("answer", "")).strip().lower()
            if user_ans.strip().lower() == correct:
                st.success("🔥 సరైన సమాధానం!")
                st.session_state.score += 1
            else:
                st.error(f"❌ తప్పు! సరైన సమాధానం: {correct}")
            st.session_state.answered = True
        elif st.session_state.answered:
            st.warning("ఇప్పటికే సమాధానం ఇచ్చారు.")

with col2:
    if st.button("➡ Next Question"):
        st.session_state.current_q = random.choice(data)
        st.session_state.answered = False
        st.rerun()

# వివరణ (ఉంటే చూపిస్తుంది)
if st.session_state.answered and "explanation" in st.session_state.current_q:
    with st.expander("Solution వివరణ చూడండి"):
        st.write(st.session_state.current_q["explanation"])

st.divider()
st.write(f"### 🏆 స్కోరు: {st.session_state.score}")
