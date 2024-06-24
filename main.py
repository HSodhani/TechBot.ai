import streamlit as st
from openai import OpenAI
import re

def main():
    st.title("💬 ChatBot.ai")

    # Load API key from Streamlit's secrets
    openai_api_key = st.secrets["OPENAI_API_KEY"]

    # Initialize OpenAI client
    client = OpenAI(api_key=openai_api_key)

    # Initialize session state for conversations and the current conversation
    if 'conversations' not in st.session_state:
        st.session_state.conversations = {}
    if 'current_conversation' not in st.session_state:
        st.session_state['current_conversation'] = []

    def detect_special_command(user_input):
        match = re.search(r"generate a step by step guide on (.+)", user_input.lower())
        if match:
            topic = match.group(1)
            return "generate_report", topic
        return None, None

    # Add a function to process general queries
    def handle_general_query(query):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a professional support assistant. Use chain of thought reasoning to provide clear, step-by-step, and informative answers to user queries. Aim to provide solutions or insights as a knowledgeable support agent."},
                    {"role": "user", "content": query}
                ]
            )
            if response.choices:
                first_choice = response.choices[0]
                return first_choice.message.content
            else:
                return "No response was generated."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    # Update the function to detect the type of query and route it accordingly
    def process_input(user_input):
        # Check for the special command to generate a report
        command, topic = detect_special_command(user_input)
        if command == "generate_report" and topic:
            prompt = f"Generate a step by step guide on {topic}"
            report = handle_general_query(prompt)
            return report, 'report'
        # Fallback for other types of queries
        general_response = handle_general_query(user_input)
        return general_response, 'general'

    # Streamlit UI handling logic
    st.subheader("Ask me anything:")

    # Form for user input to avoid continuous reruns
    with st.form(key='user_input_form'):
        user_input = st.text_area("Enter your request here:", key='user_input')
        submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        # Process the user input
        response, response_type = process_input(user_input)
        
        # Update current conversation with the new Q&A pair
        st.session_state['current_conversation'].append((user_input, response))
        
        # Clear the input box by resetting the form
        st.experimental_rerun()

    # Display conversation history in reverse order
    if st.session_state['current_conversation']:
        st.write("Conversation History:")
        for i, (q, a) in enumerate(reversed(st.session_state['current_conversation']), start=1):
            st.write(f"**Q{i}:** {q}")
            st.write(f"**A{i}:** {a}")
            st.write("---")

    # Sidebar for conversation management
    st.sidebar.header("Conversations Management:")
    conversation_name = st.sidebar.text_input("Conversation Name:", key="conversation_name")

    if st.sidebar.button("Save Conversation"):
        if conversation_name:  # Ensure the conversation name is not empty
            st.session_state['conversations'][conversation_name] = st.session_state['current_conversation'].copy()
            st.sidebar.success("Conversation Saved!")

    selected_conversation = st.sidebar.selectbox("Select a Conversation", options=list(st.session_state['conversations'].keys()))

    if st.sidebar.button("Delete Conversation"):
        if selected_conversation in st.session_state['conversations']:
            del st.session_state['conversations'][selected_conversation]
            st.sidebar.success("Conversation Deleted!")
            st.experimental_rerun()

    if st.sidebar.button("Load Conversation"):
        if selected_conversation in st.session_state['conversations']:
            st.session_state['current_conversation'] = st.session_state['conversations'][selected_conversation].copy()
            st.session_state['loaded_conversation'] = True
            st.experimental_rerun()

    if st.sidebar.button("Start New Conversation"):
        st.session_state['current_conversation'] = []
        st.session_state['loaded_conversation'] = False
        st.experimental_rerun()

    # Sidebar Instructions
    st.sidebar.header("Instructions:")
    st.sidebar.markdown("""
    - To ask a general question, type your query in the input box and click 'Send'.
    - To generate a step by step guide, type: "generate a a step by step guide on [topic]" and click 'Send'.
    """)

    # About ChatBot.ai
    st.sidebar.header("About ChatBot.ai")
    st.sidebar.info("""
    ChatBot.ai uses advanced AI techniques to generate insights and provide information based on user queries.
    """)

if __name__ == "__main__":
    main()
