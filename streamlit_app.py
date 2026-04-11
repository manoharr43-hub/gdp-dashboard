import streamlit as st

# Sidebar menu
menu = st.sidebar.selectbox(
    "Select Feature",
    ["Home", "JEE Subjects", "Quiz", "Performance"]
)

if menu == "Home":
    st.title("📘 Welcome to JEE Dashboard")
    st.write("This app helps students prepare for JEE with subjects, quizzes, and performance tracking.")

elif menu == "JEE Subjects":
    st.title("📚 JEE Subjects")

    # Subject selection
    subject = st.selectbox("Choose Subject", ["Physics", "Chemistry", "Mathematics"])

    syllabus_questions = {
        "Physics": {
            "Kinematics": {
                "question": "A car accelerates uniformly from rest at 2 m/s². Find its velocity after 10 seconds.",
                "short_answer": "Velocity = 20 m/s.",
                "long_explanation": "We use v = u + at. Here u=0, a=2, t=10 → v=20 m/s."
            },
            "Laws of Motion": {
                "question": "State Newton’s Second Law of Motion.",
                "short_answer": "Force = mass × acceleration.",
                "long_explanation": "It relates force, mass, and acceleration. F = ma."
            },
            "Thermodynamics": {
                "question": "State the First Law of Thermodynamics.",
                "short_answer": "Energy can neither be created nor destroyed.",
                "long_explanation": "ΔU = Q - W. Internal energy change equals heat supplied minus work done."
            }
        },
        "Chemistry": {
            "Atomic Structure": {
                "question": "What is the maximum number of electrons in the n=3 shell?",
                "short_answer": "18 electrons.",
                "long_explanation": "Formula 2n² → 2×3² = 18."
            },
            "Chemical Bonding": {
                "question": "What is the bond angle in methane (CH₄)?",
                "short_answer": "109.5°.",
                "long_explanation": "Methane has tetrahedral geometry due to sp³ hybridization."
            }
        },
        "Mathematics": {
            "Quadratic Equations": {
                "question": "Solve x² - 5x + 6 = 0.",
                "short_answer": "x = 2 or x = 3.",
                "long_explanation": "Factorize: (x-2)(x-3)=0 → roots are 2, 3."
            },
            "Probability": {
                "question": "What is the probability of getting a head when a coin is tossed?",
                "short_answer": "1/2.",
                "long_explanation": "Two outcomes: Head/Tail. Probability = 1/2."
            }
        }
    }

    # Reset topic index when subject changes
    if "current_subject" not in st.session_state or st.session_state.current_subject != subject:
        st.session_state.current_subject = subject
        st.session_state.topic_index = 0

    topics = list(syllabus_questions[subject].keys())

    # Ensure topic_index is within bounds
    if st.session_state.topic_index >= len(topics):
        st.session_state.topic_index = 0

    current_topic = topics[st.session_state.topic_index]

    # Display Q&A
    st.subheader(f"{subject} → {current_topic}")
    st.write("📖 Question:")
    st.info(syllabus_questions[subject][current_topic]["question"])
    st.write("✅ Short Answer:")
    st.success(syllabus_questions[subject][current_topic]["short_answer"])
    st.write("📘 Detailed Explanation:")
    st.write(syllabus_questions[subject][current_topic]["long_explanation"])

    # Navigation buttons
    col1, col2 = st.columns(2)
    if col1.button("⬅ Previous"):
        if st.session_state.topic_index > 0:
            st.session_state.topic_index -= 1
    if col2.button("Next ➡"):
        if st.session_state.topic_index < len(topics) - 1:
            st.session_state.topic_index += 1
