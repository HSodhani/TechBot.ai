# ChatBot.ai
ChatBot.ai is a responsive and interactive AI-driven chat interface built with Streamlit and powered by OpenAI's GPT-3.5 Turbo model. It offers users the capability to engage in a dynamic conversation, manage conversation history, and execute special commands to generate detailed step-by-step guides on specified topics.

## Key Features
- **Interactive Chat Interface**: Allows users to interact through a simple text input to receive detailed and context-aware responses.
- **Session State Management**: Tracks and manages user conversations within the session, enabling features like saving and reloading conversations.
- **Special Command Detection**: Detects and processes specific commands to generate structured content such as step-by-step guides on user-requested topics.
- **Conversation Management**: Provides tools to save, load, and delete conversations, giving users control over their chat histories.

## System Requirements
- Python 3.x
- Streamlit
- OpenAI Python Client
- Regular Expressions (re)

## Installation

### To set up ChatBot.ai, follow these steps:

- Clone the repository:
  
```git clone https://github.com/HSodhani/ChatBot.ai```

- Install the required dependencies:

```pip install streamlit openai```

## Usage
To run ChatBot.ai, navigate to the project directory and run the following command in your terminal:


```streamlit run main.py```

## How to Interact with the ChatBot
- Starting a New Conversation: Simply type your question or command in the provided text area and hit 'Send'.
- Managing Conversations: Use the sidebar to save, load, or delete conversations. Conversations can be named for easy retrieval.
- Generating Guides: To generate a step-by-step guide, type your request in the format: "generate a step by step guide on _[topic]_".

## Development
Developers can extend this project by adding more specialized commands, improving the AI's response accuracy, or integrating additional AI models.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests with your enhancements.

## About ChatBot.ai
ChatBot.ai leverages advanced AI techniques to provide insightful and actionable responses, aiming to enhance user experience through technology. It's a versatile tool for anyone looking to explore AI capabilities in conversation management.
