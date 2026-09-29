import streamlit as st
from dotenv import load_dotenv
import os
from google import genai
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b, #312e81);
    color: white;
}

.block-container {
    max-width: 850px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}


h1 {
    text-align: center;
    font-size: 42px !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    margin-bottom: 5px;
}


.stApp p {
    color: #cbd5e1;
}

.stTextArea textarea {
    background-color: #1e293b !important;
    color: white !important;
    border: 2px solid #6366f1 !important;
    border-radius: 15px !important;
    font-size: 16px !important;
    padding: 15px !important;
}


.stTextArea textarea:focus {
    border: 2px solid #a78bfa !important;
    box-shadow: 0 0 15px rgba(139, 92, 246, 0.5) !important;
}


.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 15px;
    border: none;
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    font-size: 18px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.3s ease;
}


.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(139, 92, 246, 0.5);
}


.response-box {
    background: rgba(30, 41, 59, 0.9);
    border-left: 5px solid #8b5cf6;
    padding: 20px;
    margin-top: 20px;
    border-radius: 12px;
    color: #f8fafc;
    line-height: 1.7;
    box-shadow: 0 5px 20px rgba(0,0,0,0.25);
}


.stAlert {
    border-radius: 12px !important;
}

.stSuccess {
    border-radius: 12px !important;
}


.footer {
    text-align: center;
    margin-top: 40px;
    color: #94a3b8;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)



st.title("🤖 Gemini AI Chatbot")

st.markdown(
    "<p style='text-align:center; font-size:18px;'>"
    "Ask Gemini anything and get an AI-powered response."
    "</p>",
    unsafe_allow_html=True
)

st.write("")

prompt = st.text_area(
    "💬 Enter your prompt:",
    placeholder="Example: Explain Artificial Intelligence in simple words...",
    height=180
)

st.write("")

if st.button("✨ Generate Response"):

    if prompt.strip():

        with st.spinner("🤖 Gemini is thinking..."):

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

        st.success("✅ Response generated!")

        st.markdown(
            f"""
            <div class="response-box">
                <h3>🤖 Gemini Response</h3>
                <p>{response.text}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.warning("⚠️ Please enter a prompt.")


st.markdown(
    "<div class='footer'>Powered by Google Gemini • Built with Streamlit</div>",
    unsafe_allow_html=True
)