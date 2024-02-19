import streamlit as st
# import os
from synergy_result import SynergyResult
# from horizon_synergy_ai import HorizonSynergyAI
from mock_search import search_and_compare


def show_result(result: SynergyResult):
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


# PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
# OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# client = HorizonSynergyAI(pinecone_api_key=PINECONE_API_KEY, openai_api_key=OPENAI_API_KEY)

# Streamlit app main code
st.title('HorizonSynergyAI')

# Create a text input area
input_text = st.text_area("Enter your project description:")

# Create a submit button
if st.button('Submit'):
    # This is where the function gets triggered when the submit button is pressed
    with st.spinner('Searching and comparing projects...'):
        # for result in client.search_and_compare(input_text, top_k=3):
        for result in search_and_compare(input_text, top_k=3):
            show_result(result)
