import agent as lch
import streamlit as st

st.title("Project name generator")

user_project_type = st.sidebar.selectbox("What type of project are you creating?",("Web App", "Content Creation", "Music"))

if user_project_type == "Web App":
    project_description = st.sidebar.text_area(label="Give a description of what your web app does.", max_chars=150)

if user_project_type == "Content Creation":
    project_description = st.sidebar.text_area(label="Give a description of what your content is.", max_chars=150)

if user_project_type == "Music":
    project_description = st.sidebar.text_area(label="Give a description of what your genre is.", max_chars=150)

if project_description:
    response = lch.generate_project_name(project_description, user_project_type)
    st.text(response['project_name'])