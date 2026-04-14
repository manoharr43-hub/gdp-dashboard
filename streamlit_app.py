import streamlit as st
import json
import random

# పేజీ సెట్టింగ్స్
st.set_page_config(page_title="JEE Quiz App", layout="centered")

st.title("📘 JEE Quiz App (AI Powered)")

# JSON డేటాను లోడ్ చేయడం
@st.cache_data
def load_data():
    try:
        # GitHubలో ఫైల్ ఒకే ఫోల్డర్‌లో ఉంటే కేవలం పేరు ఇస్తే సరిపోతుంది
        with open("all_jee_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("❌ JSON ఫైల్ దొరకలేదు! దయచేసి GitHubలో ఫైల్ పేరు సరిగ్గా ఉందో లేదో చూడండి.")
        return []
    except Exception as e:
        st.error(f"❌ ఎర్రర్ వచ్చింది: {e}")
        return []

data = load_data()

# డేటా ఖాళీగా ఉంటే యాప్‌ను ఆపివేయడం
if not data:
    st.info("💡 సూచన: మీ GitHub రిపోజిటరీలో 'all_jee_data.json' ఫైల్‌ను అప్‌లోడ్ చేశారో లేదో ఒకసారి చెక్ చేయండి.")
    st.stop()

# --- Session State ని సెట్ చేయడం ---
if "score" not in st.session_state:
    st.session_state.score = 0

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(data)

if "answered" not in st.session_state:
    st.session_state.answered = False

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# --- Helper Functions ---
def next_question():
    st.session_state.current_question = random.choice(data)
    st.session_state.answered = False
    st.session_state.feedback = ""
    if "user_input_key" in st.session_state:
        st.session_state.user_input_key = ""

# --- UI ప్రదర్శన ---
st.write("---")
st.subheader("📖 ప్రశ్న:")
# JSON లో ప్రశ్న 'text' అనే కీ (key) తో ఉందని భావిస్తున్నాను
st.info(st.session_state.current_question.get("text", "ప్రశ్న లోడ్ కాలేదు."))

# సమాధానం ఇన్పుట్
user_ans = st.text_input("✍ మీ సమాధానాన్ని ఇక్కడ టైప్ చేయండి:", key="user_input_key")

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("✅ Submit"):
        if user_ans and not st.session_state.answered:
            # మీ JSON లో 'answer' అనే కీ ఉంటే దాన్ని చెక్ చేస్తుంది
            correct_ans = str(st.session_state.current_question.get("answer", "")).strip().lower()
            
            if user_ans.strip().lower() == correct_ans:
                st.session_state.score += 1
                st.session_state.feedback = "correct"
            else:
                st.session_state.feedback = "wrong"
            
            st.session_state.answered = True
        elif st.session_state.answered:
            st.warning("మీరు ఇప్పటికే సమాధానం ఇచ్చారు!")
        else:
            st.warning("ముందుగా సమాధానం టైప్ చేయండి.")

with col2:
    if st.button("➡ Next Question"):
        next_question()
        st.rerun()

# --- రిజల్ట్ మరియు వివరణ ---
if st.session_state.feedback == "correct":
    st.success(f"🔥 అద్భుతం! సరైన సమాధానం: {st.session_state.current_question.get('answer')}")
elif st.session_state.feedback == "wrong":
    st.error(f"❌ తప్పు! సరైన సమాధానం: {st.session_state.current_question.get('answer')}")

# వివరణ ఉంటే చూపిస్తుంది
if st.session_state.answered and "explanation" in st.session_state.current_question:
    with st.expander("వివరణ (Solution) చూడండి"):
        st.write(st.session_state.current_question["explanation"])

# స్కోరు ప్రదర్శన
st.divider()
st.write(f"### 🏆 మీ ప్రస్తుత స్కోరు: {st.session_state.score}")
