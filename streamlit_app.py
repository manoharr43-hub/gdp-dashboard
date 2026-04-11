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

    # Subject content dictionary
    subject_content = {
        "Physics": {
            "overview": "Physics is the study of matter, energy, and their interactions. It explains natural phenomena using laws and principles.",
            "topics": {
                "Kinematics": "Study of motion without considering its causes. Focus on displacement, velocity, acceleration.",
                "Laws of Motion": "Newton's three laws explain how forces affect motion.",
                "Thermodynamics": "Study of heat, energy, and work. Includes laws of energy conservation."
            }
        },
        "Chemistry": {
            "overview": "Chemistry is the study of substances, their properties, reactions, and how they combine to form new substances.",
            "topics": {
                "Atomic Structure": "Understanding protons, neutrons, electrons, and how they form atoms.",
                "Chemical Bonding": "Explains ionic, covalent, and metallic bonds between atoms.",
                "Organic Chemistry": "Study of carbon compounds, reactions, and functional groups."
            }
        },
        "Mathematics": {
            "overview": "Mathematics is the language of science. It deals with numbers, equations, functions, and geometry.",
            "topics": {
                "Algebra": "Manipulation of symbols and solving equations.",
                "Calculus": "Study of limits, derivatives, and integrals.",
                "Coordinate Geometry": "Geometry using coordinates, equations of lines, circles, and conics."
            }
        }
    }

    # Show subject overview
    st.subheader(f"{subject} Overview")
    st.write(subject_content[subject]["overview"])

    # Show topics with explanations
    st.subheader(f"{subject} Topics")
    for t, desc in subject_content[subject]["topics"].items():
        st.markdown(f"📖 **{subject} → {t}** — {desc}")

elif menu == "Quiz":
    st.title("📝 Quiz Section")
    st.write("Here you can attempt practice quizzes for JEE.")
    st.info("Feature under development – quizzes will be added soon!")

elif menu == "Performance":
    st.title("📊 Performance Tracker")
    st.write("Track your progress across subjects and quizzes.")
    st.info("Feature under development – performance analytics will be added soon!")
