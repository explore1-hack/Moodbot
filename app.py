# app.py

# app.py

import streamlit as st
from prompt import emotion_templates, generate_prompt
from llm_response import generate_response_llama

st.set_page_config(page_title="🧠 MoodBot", layout="centered")

st.title("🧠 MoodBot: Chat with an Emotion!")
st.write("Choose your mood/personality and start chatting.")

# Emotion dropdown
emotion = st.selectbox("Select Emotion:", list(emotion_templates.keys()))

# Chat input
user_input = st.chat_input("Type your message...")

# Initialize history (list of dicts)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# On user message
if user_input:
    # Add user message to history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Generate prompt using emotion tone
    prompt = generate_prompt(emotion, user_input)
    bot_response = generate_response_llama(prompt)

    # Add bot response to history
    st.session_state.chat_history.append({"role": "assistant", "content": bot_response})

# Display entire chat
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"👤 **You:** {msg['content']}")
    else:
        st.markdown(f"🤖 **MoodBot:** {msg['content']}")
