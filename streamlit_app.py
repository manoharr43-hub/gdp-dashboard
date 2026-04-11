import streamlit as st

# Sidebar menu
menu = st.sidebar.selectbox(
    "Select Feature",
    ["Home", "JEE Subjects", "Quiz", "Performance"]
)

# Home Page
if menu == "Home":
    st.title("📘 Welcome to JEE Dashboard")
    st.write("This app helps students prepare for JEE with subjects, quizzes, and performance tracking.")

# JEE Subjects Page
elif menu == "JEE Subjects":
    st.title("📚 JEE Subjects")

    # Subject selection
    subject = st.selectbox("Choose Subject", ["Physics", "Chemistry", "Mathematics"])

    # Topics with explanations
    topics = {
        "Physics": {
            "Kinematics": "Study of motion without considering its causes. Focus on displacement, velocity, acceleration.",
            "Laws of Motion": "Newton's three laws explain how forces affect motion.",
            "Thermodynamics": "Study of heat, energy, and work. Includes laws of energy conservation."
        },
        "Chemistry": {
            "Atomic Structure": "Understanding protons, neutrons, electrons, and how they form atoms.",
            "Chemical Bonding": "Explains ionic, covalent, and metallic bonds between atoms.",
            "Organic Chemistry": "Study of carbon compounds, reactions, and functional groups."
        },
        "Mathematics": {
            "Algebra": "Manipulation of symbols and solving equations.",
            "Calculus": "Study of limits, derivatives, and integrals.",
            "Coordinate Geometry": "Geometry using coordinates, equations of lines, circles, and conics."
        }
    }

    st.subheader(f"{subject} Topics")
    for t, desc in topics[subject].items():
        st.markdown(f"📖 **{t}** — {desc}")

# Quiz Page
elif menu == "Quiz":
    st.title("📝 Quiz Section")
    st.write("Here you can attempt practice quizzes for JEE.")
    st.info("Feature under development – quizzes will be added soon!")

# Performance Page
elif menu == "Performance":
    st.title("📊 Performance Tracker")
    st.write("Track your progress across subjects and quizzes.")
    st.info("Feature under development – performance analytics will be added soon!")
