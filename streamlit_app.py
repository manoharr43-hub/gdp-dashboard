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

    # Topics dictionary with sample questions
    syllabus_questions = {
        "Physics": {
            "Kinematics": {
                "question": "A car accelerates uniformly from rest at 2 m/s². Find its velocity after 10 seconds.",
                "answer": "Using v = u + at → v = 0 + 2×10 = 20 m/s."
            },
            "Laws of Motion": {
                "question": "State Newton’s Second Law of Motion.",
                "answer": "It states that Force = mass × acceleration (F = ma)."
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
            }
        },
        "Mathematics": {
            "Quadratic Equations": {
                "question": "Solve x² - 5x + 6 = 0.",
                "answer": "Factorizing: (x-2)(x-3)=0 → x=2 or x=3."
            },
            "Probability": {
                "question": "What is the probability of getting a head when a coin is tossed?",
                "answer": "Probability = 1/2."
            }
        }
    }

    # Topic selection
    if subject in syllabus_questions:
        topic = st.selectbox("Choose Topic", list(syllabus_questions[subject].keys()))

        st.subheader(f"{subject} → {topic}")
        st.write("📖 Question:")
        st.info(syllabus_questions[subject][topic]["question"])

        st.write("✅ AI Answer:")
        st.success(syllabus_questions[subject][topic]["answer"])

elif menu == "Quiz":
    st.title("📝 Quiz Section")
    st.write("Here you can attempt practice quizzes for JEE.")
    st.info("Feature under development – quizzes will be added soon!")

elif menu == "Performance":
    st.title("📊 Performance Tracker")
    st.write("Track your progress across subjects and quizzes.")
    st.info("Feature under development – performance analytics will be added soon!")
