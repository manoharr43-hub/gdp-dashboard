import streamlit as st

# Sidebar menu
menu = st.sidebar.selectbox(
    "Select Feature",
    ["Home", "JEE Subjects", "Quiz", "Performance"]
)

# ---------------- Home ----------------
if menu == "Home":
    st.title("📘 Welcome to JEE Dashboard")
    st.write("This app helps students prepare for JEE with subjects, quizzes, and performance tracking.")

# ---------------- JEE Subjects ----------------
elif menu == "JEE Subjects":
    st.title("📚 JEE Subjects")

    # Subject selection
    subject = st.selectbox("Choose Subject", ["Physics", "Chemistry", "Mathematics"])

    # Topics + Questions + Answers
    syllabus_questions = {
        "Physics": {
            "Kinematics": {
                "question": "A car accelerates uniformly from rest at 2 m/s². Find its velocity after 10 seconds.",
                "answer": "Using v = u + at → v = 0 + 2×10 = 20 m/s."
            },
            "Laws of Motion": {
                "question": "State Newton’s Second Law of Motion.",
                "answer": "It states that Force = mass × acceleration (F = ma)."
            },
            "Thermodynamics": {
                "question": "State the First Law of Thermodynamics.",
                "answer": "Energy can neither be created nor destroyed, only transformed from one form to another."
            }
        },
        "Chemistry": {
            "Atomic Structure": {
                "question": "What is the maximum number of electrons in the n=3 shell?",
                "answer": "Using 2n² → 2×3² = 18 electrons."
            },
            "Chemical Bonding": {
                "question": "What is the bond angle in methane (CH₄)?",
                "answer": "The bond angle is 109.5° due to sp³ hybridization."
            },
            "Organic Chemistry": {
                "question": "What is the functional group in alcohols?",
                "answer": "Alcohols contain the hydroxyl (-OH) group."
            }
        },
        "Mathematics": {
            "Algebra": {
                "question": "Solve for x: 2x + 5 = 15.",
                "answer": "Subtract 5 → 2x = 10 → x = 5."
            },
            "Calculus": {
                "question": "Find derivative of f(x) = x².",
                "answer": "f'(x) = 2x."
            },
            "Probability": {
                "question": "What is the probability of getting a head when a coin is tossed?",
                "answer": "Probability = 1/2."
            }
        }
    }

    # Session state for topic navigation
    if "topic_index" not in st.session_state:
        st.session_state.topic_index = 0

    # Current subject topics
    topics = list(syllabus_questions[subject].keys())
    current_topic = topics[st.session_state.topic_index]

    # Display Q&A
    st.subheader(f"{subject} → {current_topic}")
    st.write("📖 Question:")
    st.info(syllabus_questions[subject][current_topic]["question"])
    st.write("✅ AI Answer:")
    st.success(syllabus_questions[subject][current_topic]["answer"])

    # Navigation buttons
    col1, col2 = st.columns(2)
    if col1.button("⬅ Previous") and st.session_state.topic_index > 0:
        st.session_state.topic_index
