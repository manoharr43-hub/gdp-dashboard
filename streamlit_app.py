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

    # Topics + Questions + Answers + Explanations (based on NTA JEE Main syllabus)
    syllabus_questions = {
        "Physics": {
            "Kinematics": {
                "question": "A car accelerates uniformly from rest at 2 m/s². Find its velocity after 10 seconds.",
                "short_answer": "Velocity = 20 m/s.",
                "long_explanation": "We use the first equation of motion: v = u + at. Here u=0, a=2 m/s², t=10s. Substituting values: v = 0 + 2×10 = 20 m/s. This shows how velocity increases linearly with time under constant acceleration."
            },
            "Laws of Motion": {
                "question": "State Newton’s Second Law of Motion.",
                "short_answer": "Force = mass × acceleration (F = ma).",
                "long_explanation": "Newton’s Second Law explains the relationship between force, mass, and acceleration. It states that the net force acting on a body is equal to the product of its mass and acceleration. This law forms the foundation of dynamics and helps calculate motion under applied forces."
            },
            "Thermodynamics": {
                "question": "State the First Law of Thermodynamics.",
                "short_answer": "Energy can neither be created nor destroyed.",
                "long_explanation": "The First Law of Thermodynamics is essentially the law of conservation of energy. It states that the change in internal energy of a system is equal to the heat supplied minus the work done by the system. This principle governs all energy transformations in physics."
            }
        },
        "Chemistry": {
            "Atomic Structure": {
                "question": "What is the maximum number of electrons in the n=3 shell?",
                "short_answer": "18 electrons.",
                "long_explanation": "The formula for maximum electrons in a shell is 2n². For n=3, 2×3² = 18. This means the third shell can accommodate up to 18 electrons, distributed across s, p, and d orbitals."
            },
            "Chemical Bonding": {
                "question": "What is the bond angle in methane (CH₄)?",
                "short_answer": "109.5°.",
                "long_explanation": "Methane has a tetrahedral geometry due to sp³ hybridization of carbon. The bond angle between H–C–H is 109.5°, which minimizes electron pair repulsion according to VSEPR theory."
            }
        },
        "Mathematics": {
            "Quadratic Equations": {
                "question": "Solve x² - 5x + 6 = 0.",
                "short_answer": "x = 2 or x = 3.",
                "long_explanation": "Factorizing: x² - 5x + 6 = (x-2)(x-3). Setting each factor equal to zero gives x=2 or x=3. These are the roots of the quadratic equation."
            },
            "Probability": {
                "question": "What is the probability of getting a head when a coin is tossed?",
                "short_answer": "1/2.",
                "long_explanation": "A fair coin has two equally likely outcomes: Head or Tail. Probability = (favorable outcomes)/(total outcomes) = 1/2. This is a fundamental concept in probability theory."
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
    st.write("✅ Short Answer:")
    st.success(syllabus_questions[subject][current_topic]["short_answer"])
    st.write("📘 Detailed Explanation:")
    st.write(syllabus_questions[subject][current_topic]["long_explanation"])

    # Navigation buttons
    col1, col2 = st.columns(2)
    if col1.button("⬅ Previous") and st.session_state.topic_index > 0:
        st.session_state.topic_index -= 1
    if col2.button("Next ➡") and st.session_state.topic_index < len(topics) - 1:
        st.session_state.topic_index += 1

# ---------------- Quiz ----------------
elif menu == "Quiz":
    st.title("📝 Quiz Section")
    st.write("Here you can attempt practice quizzes for JEE.")
    st.info("Feature under development – quizzes will be added soon!")

# ---------------- Performance ----------------
elif menu == "Performance":
    st.title("📊 Performance Tracker")
    st.write("Track your progress across subjects and quizzes.")
    st.info("Feature under development – performance analytics will be added soon!")
