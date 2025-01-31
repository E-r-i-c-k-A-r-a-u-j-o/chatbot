%%writefile chatbot.py
import streamlit as st
import openai

openai.api_key = "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"

st.title("Chatbot de Voz 🎙️")

pregunta = st.text_input("Haz una pregunta:")

if st.button("Responder"):
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": pregunta}]
    )["choices"][0]["message"]["content"]

    st.write(f"🤖 Chatbot: {respuesta}")
 
