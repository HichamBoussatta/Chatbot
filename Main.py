import streamlit as st 
import google.generativeai as genai
from PIL import Image

# API Configuration using Streamlit Secrets
api_key = st.secrets["API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Functions
def generate_text(prompt):
    return model.generate_content(prompt).text

def text_summarization(text):
    return model.generate_content(f"Summarize this: {text}").text

def question_answering(context, question):
    return model.generate_content(f"Question: {question} Context: {context}").text

def sentiment_analysis(text):
    return model.generate_content(f"Analyze the sentiment of this text: {text}").text

def text_translation(text, target_language):
    return model.generate_content(f"Translate this text to {target_language}: {text}").text

def analyze_image(uploaded_image):
    image = Image.open(uploaded_image)
    response = model.generate_content(["Describe this image in detail:", image])
    return response.text

# Streamlit UI
st.title("🧠 HBAi")

option = st.sidebar.radio("Choose a function:", [
    "1. Text Generation",
    "2. Text Summarization",
    "3. Question Answering",
    "4. Sentiment Analysis",
    "5. Text Translation",
    "6. Image Analysis"
])

if option == "1. Text Generation":
    prompt = st.text_area("Prompt:", "")
    if st.button("Generate"):
        output = generate_text(prompt)
        st.success(output)

elif option == "2. Text Summarization":
    text = st.text_area("Text to summarize:", "")
    if st.button("Summarize"):
        output = text_summarization(text)
        st.success(output)

elif option == "3. Question Answering":
    context = st.text_area("Context:", "")
    question = st.text_input("Question:", "")
    if st.button("Answer"):
        output = question_answering(context, question)
        st.success(output)

elif option == "4. Sentiment Analysis":
    text = st.text_area("Text to analyze:", "")
    if st.button("Analyze"):
        output = sentiment_analysis(text)
        st.success(output)

elif option == "5. Text Translation":
    text = st.text_area("Text to translate:", "")
    lang = st.text_input("Target language (e.g., fr, es, ar, de):", "fr")
    if st.button("Translate"):
        output = text_translation(text, lang)
        st.success(output)

elif option == "6. Image Analysis":
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        if st.button("Analyze Image"):
            output = analyze_image(uploaded_image)
            st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)
            st.success(output)
