import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="Espresso Assistant", page_icon="☕", layout="centered")

st.markdown("""
<style>
    .stTextInput input, .stSelectbox select, .stNumberInput input { border-radius: 6px; }
    .stButton button { background-color: #2b2b2b; color: white; border-radius: 6px; border: 1px solid #444; padding: 0.5rem 1rem; }
    .img-container { display: flex; justify-content: center; margin: 10px 0; }
    .img-container img { max-height: 160px !important; max-width: 250px !important; border-radius: 8px; border: 1px solid #444; object-fit: cover; }
</style>
""", unsafe_allow_html=True)

if not api_key:
    st.error("❌ GEMINI_API_KEY is not set in the .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

st.title("☕ Espresso Extraction & Recipe Assistant")
st.caption("Input parameters and upload your extraction/puck photo for AI vision diagnosis.")
st.markdown("---")

st.subheader("📸 Visual Diagnosis (Optional)")
uploaded_file = st.file_uploader("Upload extraction or puck photo", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.markdown('<div class="img-container">', unsafe_allow_html=True)
    st.image(image, width=220)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.subheader("🎛️ Extraction Parameters")

col1, col2 = st.columns(2)
with col1:
    bean_name = st.text_input("Coffee Bean Name", placeholder="e.g., Seabright Blend")
with col2:
    roast_level = st.selectbox("Roast Level", ["Medium", "Light", "Dark", "Omni"])

col3, col4, col5 = st.columns(3)
with col3:
    dose_in = st.number_input("Dose In (g)", 10.0, 30.0, 18.0, 0.5)
with col4:
    yield_out = st.number_input("Yield Out (g)", 10.0, 100.0, 36.0, 1.0)
with col5:
    extract_time = st.number_input("Extraction Time (s)", 5, 120, 28, 1)

grind_setting = st.text_input("Grind Setting", placeholder="e.g., 14 clicks")
issues = st.multiselect("Main Issues", ["Sour & Thin", "Bitter & Astringent", "Channeling", "Fast Flow", "Slow Flow", "Weak Body"])

if st.button("✨ Diagnose Shot with AI", use_container_width=True):
    prompt = f"""
    Analyze espresso: Bean: {bean_name}, Roast: {roast_level}, Dose: {dose_in}g, Yield: {yield_out}g, Time: {extract_time}s, Grind: {grind_setting}, Issues: {issues}.
    Provide: 1. Root Cause Analysis, 2. Action Plan (Grind, Puck Prep, Target Recipe) concisely in English.
    """
    with st.spinner("Analyzing..."):
        contents = [image, prompt] if uploaded_file else prompt
        res = client.models.generate_content(model='gemini-3.8-flash', contents=contents)
        st.markdown(res.text)