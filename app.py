import streamlit as st
import datetime
import time

# 1. SETUP
st.set_page_config(page_title="Vixx Energy Flow", page_icon="✨", layout="centered")

# 2. THE COLOR THEME (Parchment & Gold)
st.markdown("""
    <style>
    .stApp { background-color: #FFF9F1 !important; }
    h1, h2, h3, p, span, label { color: #4A3728 !important; }
    .stButton>button {
        background-color: #D4AF37 !important;
        color: white !important;
        border-radius: 25px !important;
        border: none !important;
        font-weight: bold !important;
    }
    .stAlert {
        background-color: rgba(212, 175, 55, 0.1) !important;
        border: 1px solid #D4AF37 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LOGO
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.write("✨ **Vixx Energy Flow** ✨")

st.title("Vixx Energy Flow")

# 4. PERMANENT MUSIC PLAYER (Ambient 432Hz Style)
st.write("### 🎵 Ambient Healing Frequencies")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3") 
st.caption("Play this for background peace while you explore.")

# 5. DATA (Affirmations & Seeds)
alignment_data = {
    "Root (Grounding)": {"affirmation": "I am safe and anchored.", "seed": "What makes you feel safe?"},
    "Sacral (Creativity)": {"affirmation": "I flow with creativity.", "seed": "How can you create today?"},
    "Solar Plexus (Power)": {"affirmation": "I am powerful.", "seed": "Where is your strength?"},
    "Heart (Love)": {"affirmation": "I lead with love.", "seed": "Who needs your love today?"},
    "Throat (Truth)": {"affirmation": "I speak my truth.", "seed": "What needs to be said?"},
    "Third Eye (Intuition)": {"affirmation": "I trust my vision.", "seed": "What is your gut saying?"},
    "Crown (Spirit)": {"affirmation": "I am connected.", "seed": "How do you feel the divine?"}
}

# 6. ALIGNMENT SECTION
st.divider()
chakra = st.selectbox("Which energy center needs movement?", list(alignment_data.keys()))

if st.button("Activate My Spark"):
    st.snow()
    st.success(f"**Affirmation:** {alignment_data[chakra]['affirmation']}")
    st.info(f"**Journaling Seed:** {alignment_data[chakra]['seed']}")

# 7. REIKI TIMER WITH TRIGGERED SOUND
st.divider()
st.subheader("🧘 Reiki Session Timer")
duration = st.slider("Minutes:", 1, 30, 5)

if st.button("Start Timer"):
    # Trigger a chime sound to start
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")
    
    progress_text = "Session active... focus on your breath."
    my_bar = st.progress(0, text=progress_text)
    for i in range(100):
        time.sleep((duration * 60) / 100)
        my_bar.progress(i + 1, text=progress_text)
    
    st.balloons()
    st.success("Session Complete. ✨")
