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

    # Topics dictionary
    topics = {
        "Physics": ["Kinematics", "Laws of Motion", "Thermodynamics"],
        "Chemistry": ["Atomic Structure", "Chemical Bonding", "Organic Chemistry"],
        "Mathematics": ["Algebra", "Calculus", "Coordinate Geometry"]
    }

    st.subheader(f"{subject} Topics")
    for t in topics[subject]:
        st.markdown(f"📖 {t}")

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
