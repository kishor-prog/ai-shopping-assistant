from pathlib import Path
import sys
import asyncio

import streamlit as st

# --------------------------------------------------
# Add project root to Python path
# --------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from ai_assistant.chat_service import ChatService

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="AI Shopping Assistant",
    page_icon="🛒",
    layout="wide",
)

st.title("🛒 AI Shopping Assistant")
st.caption("Powered by Gemini + MCP + FastAPI + PostgreSQL")

# --------------------------------------------------
# Initialize Chat Service
# --------------------------------------------------
if "chat_service" not in st.session_state:
    st.session_state.chat_service = ChatService()

service = st.session_state.chat_service

# --------------------------------------------------
# Chat History
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# Chat Input
# --------------------------------------------------
prompt = st.chat_input(
    "Ask me about products, categories, or users..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = asyncio.run(
                service.chat(prompt)
            )

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )