import streamlit as st
import os
from horizon_twin_result import HorizonTwinResult
from horizon_twin_client import HorizonTwinClient
from dotenv import load_dotenv

load_dotenv()


def show_result(result: HorizonTwinResult):
    with st.container():
        st.write(result.comparison.score, result.project.title)
        st.write(result.comparison.summary)
        with st.expander("Details"):
            st.markdown("**Similarity**")
            st.write(result.comparison.similarity)
            st.divider()
            st.markdown("**Difference**")
            st.write(result.comparison.difference)
            st.divider()
            st.markdown("**Score Reasoning**")
            st.write(result.comparison.reason)
            st.divider()
            st.markdown("**Original Objective**")
            st.write(result.project.objective)


PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
client = HorizonTwinClient(pinecone_api_key=PINECONE_API_KEY, openai_api_key=OPENAI_API_KEY)

# Streamlit app main code
st.title(":robot_face: HorizonTwinAI")

# Create a text input area
input_text = st.text_area("Enter your project description:")
col1, col2 = st.columns(2)
with col1:
    model = st.selectbox('Model', ('gpt-3.5-turbo', 'gpt-4-turbo-preview'))

with col2:
    top_k = st.number_input("Number of projects to compare", min_value=1, max_value=10, value=3, step=1)

with st.container():
    if st.button("Run", use_container_width=True):
        # This is where the function gets triggered when the submit button is pressed
        with st.spinner("Searching for simmilar projects and comparing them..."):
            # for result in client.search_and_compare(input_text, top_k=3):
            for result in client.search_and_compare(input_text, top_k=top_k, model=model):
                show_result(result=result)
