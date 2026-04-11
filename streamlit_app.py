import streamlit as st
import json

st.title("📘 JEE Quiz App")

# Load JSON
with open(r"C:\Users\User\Desktop\all_jee_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Filter only questions
questions = [item for item in data if "?" in item["text"]]

if len(questions) == 0:
    st.error("No questions found in JSON")
else:
    q_index = st.number_input("Select Question", 0, len(questions)-1, 0)

    st.write("### Question:")
    st.info(questions[q_index]["text"])
