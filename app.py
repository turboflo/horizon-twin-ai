# Import necessary libraries and modules
import streamlit as st
import os
from horizon_twin_ai.result import Result
from horizon_twin_ai.client import Client
from horizon_twin_ai.mock_search import mock_search_and_compare
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve API keys from environment variables
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
DEV_MODE = os.environ.get("DEV_MODE", "False").lower() in ["true", "1"]

# Initialize the HorizonTwinClient with API keys
client = Client(pinecone_api_key=PINECONE_API_KEY,
                openai_api_key=OPENAI_API_KEY)


def show_result(result: Result):
    """
    Display the result of a comparison between projects in a Streamlit application.

    Args:
    result (HorizonTwinResult): An object containing the comparison data between two projects.
    """
    # Container to display comparison results
    with st.container():
        # Display the comparison score and project title
        st.write(result.comparison.score, result.project.title)
        # Display a summary of the comparison
        st.write(result.comparison.summary)
        # Provide an expander for detailed comparison information
        with st.expander("Details"):
            st.markdown("**Similarity**")
            st.write(result.comparison.similarity)
            st.divider()  # Visual divider
            st.markdown("**Difference**")
            st.write(result.comparison.difference)
            st.divider()  # Visual divider
            st.markdown("**Score Reasoning**")
            st.write(result.comparison.reason)
            st.divider()
            st.markdown("**Vector Similarity**")
            st.write(result.project.score)
            st.divider()  # Visual divider
            st.markdown("**Original Objective**")
            st.write(result.project.objective)


# Set the title of the Streamlit application
st.title(":robot_face: HorizonTwinAI")

# Toggle to use mock api request for testing purposes
if DEV_MODE:
    use_mock = st.toggle("Use Mock API request", False)
else:
    use_mock = False

# Input area for users to enter their project description
input_text = st.text_area("Enter your project description:")

# Create two columns for layout purposes
col1, col2 = st.columns(2)
with col1:
    # Dropdown for selecting the model
    model = st.selectbox('Model', ('gpt-3.5-turbo', 'gpt-4-turbo-preview'))

with col2:
    # Input for selecting the number of projects to compare (between 1 and 10)
    top_k = st.number_input("Number of projects to compare",
                            min_value=1, max_value=10, value=3, step=1)

# Container for the run button and results display
with st.container():
    # Button to trigger the comparison process
    if st.button("Run", use_container_width=True):
        # Show a spinner while processing
        with st.spinner("Searching for similar projects and comparing them..."):
            # Iterate through the results and display each
            results = []
            if use_mock:
                results = mock_search_and_compare(
                    input_text, top_k=top_k)
            else:
                results = client.search_and_compare(
                    input_text, top_k=top_k, model=model)

            for result in results:
                show_result(result=result)
