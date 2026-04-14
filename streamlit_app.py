import streamlit as st
import json
import random

# పేజీ సెట్టింగ్స్
st.set_page_config(page_title="JEE Quiz App", layout="centered")
st.title("📘 JEE Quiz App (AI Powered)")

# JSON డేటాను లోడ్ చేయడం (Caching వాడితే వేగం పెరుగుతుంది)
@st.cache_data
def load_data():
    try:
        with open(r"C:\Users\User\Desktop\all_jee_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("❌ ఫైల్ దొరకలేదు. దయచేసి Path సరిచూసుకోండి.")
        return []

data = load_data()

# Session State ని సెట్ చేయడం (పేజీ రీఫ్రెష్ అయినా డేటా పోకుండా)
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(data)
if "answered" not in st.session_state:
    st.session_state.answered = False

# ప్రశ్నను చూపించడం
st.subheader("📖 ప్రశ్న:")
st.info(st.session_state.current_question.get("text", "ప్రశ్న అందుబాటులో లేదు"))

# సమాధానం ఇన్పుట్
user_ans = st.text_input("✍ మీ సమాధానాన్ని టైప్ చేయండి:", key="ans_input")

col1, col2 = st.columns(2)

with col1:
    if st.button("✅ Submit"):
        if not st.session_state.answered:
            # ఇక్కడ 'answer' అనేది మీ JSON లో ఉన్న కీ (Key) అని గమనించగలరు
            correct_answer = str(st.session_state.current_question.get("answer", "")).strip().lower()
            
            if user_ans.strip().lower() == correct_answer:
                st.success("🔥 అద్భుతం! సరైన సమాధానం.")
                st.session_state.score += 1
            else:
                st.error(f"❌ తప్పు సమాధానం. సరైన సమాధానం: {correct_answer}")
            
            st.session_state.answered = True
        else:
            st.warning("మీరు ఇప్పటికే ఈ ప్రశ్నకు సమాధానం ఇచ్చారు.")

with col2:
    if st.button("➡ Next Question"):
        st.session_state.current_question = random.choice(data)
        st.session_state.answered = False
        st.rerun() # పేజీని వెంటనే రీఫ్రెష్ చేస్తుంది

# స్కోరు ప్రదర్శన
st.divider()
st.write(f"### 🏆 మీ ప్రస్తుత స్కోరు: {st.session_state.score}")
