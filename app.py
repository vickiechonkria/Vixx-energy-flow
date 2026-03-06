import streamlit as st
import datetime
import time

# 1. SETUP (Must be first)
st.set_page_config(page_title="Vixx Energy Flow", layout="centered")

# 2. THE COLOR THEME (Parchment & Gold)
st.markdown("""
    <style>
    /* This forces the background to Parchment */
    .stApp {
        background-color: #FFF9F1 !important;
    }
    /* This forces text to Dark Brown */
    h1, h2, h3, p, span, label {
        color: #4A3728 !important;
    }
    /* This forces buttons to Gold */
    .stButton>button {
        background-color: #D4AF37 !important;
        color: white !important;
        border-radius: 25px !important;
        border: none !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LOGO
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.write("✨")

# 4. CONTENT
st.title("Vixx Energy Flow")
st.write(f"**Date:** {datetime.date.today().strftime('%B %d, %Y')}")

st.subheader("Today's Alignment")
chakra = st.selectbox("Choose your energy center:", 
    ["Root", "Sacral", "Solar Plexus", "Heart", "Throat", "Third Eye", "Crown"])

if st.button("Activate My Spark"):
    st.snow()
    st.success("Energy Flowing... ✨")

# 5. REIKI TIMER
st.divider()
st.subheader("🧘 Reiki Timer")
duration = st.slider("Minutes:", 1, 30, 5)
if st.button("Start Session"):
    bar = st.progress(0)
    for i in range(100):
        time.sleep((duration * 60) / 100)
        bar.progress(i + 1)
    st.success("Session Complete. Drink water and ground yourself. ✨")
