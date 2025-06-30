
import streamlit as st
from sbti_chatbot.sbti_utils import load_sbti_data
from sbti_chatbot.llm_chat import answer_query

st.set_page_config(layout="wide")
st.title("🌍 SBTi Company Explorer + Chatbot")

df = load_sbti_data()

st.subheader("📊 Companies Taking Action")
st.dataframe(df, use_container_width=True)

st.subheader("🤖 Ask about a company's climate target")
query = st.chat_input("Type your question...")

if query:
    with st.chat_message("user"):
        st.write(query)
    with st.chat_message("assistant"):
        st.write("Thinking...")
        reply = answer_query(query, df)
        st.write(reply)
