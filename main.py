import streamlit as st
import assistant as assist
import textwrap

st.title("YouTube Assistant")

with st.sidebar:
    with st.form(key="my_form"):
        youtube_url = st.sidebar.text_area(
            label="What is the YouTube video URL?",
            max_chars=50
        )
        query = st.sidebar.text_area(
            label="Ask me about the video?",
            max_chars=50,
            key="query"
        )

        submit_button = st.form_submit_button(label='Submit')

if query and youtube_url:
    db = assist.yt_vectordb(youtube_url)
    response, docs = assist.query_response(db, query)
    st.subheader("Answer:")
    st.text(textwrap.fill(response, width=80))
