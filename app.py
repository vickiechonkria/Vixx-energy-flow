import streamlit as st
import datetime
import time

# 1. SETUP
st.set_page_config(page_title="Vixx Energy Flow", page_icon="💜", layout="centered")

# 2. THE COLORS (Violet & Green Theme)
st.markdown("""
    <style>
    .stApp { background-color: #F0F9F6 !important; }
    h1, h2, h3 { color: #6D28D9 !important; font-family: 'Helvetica', sans-serif; }
    p, span, label { color: #4B5563 !important; }
    .stButton>button {
        background-color: #7C3AED !important;
        color: white !important;
        border-radius: 30px !important;
        border: none !important;
        font-weight: bold !important;
    }
    .stExpander {
        background-color: white !important;
        border-radius: 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LOGO
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.write("✨ **VIXX ENERGY FLOW** ✨")

# 4. NEW: ABOUT THE APP SECTION
with st.expander("ℹ️ About Vixx Energy Flow & How it Helps"):
    st.write("""
    **Vixx Energy Flow** is your digital sanctuary for spiritual alignment. This app is designed to help you:
    * **Shift Your Frequency:** Use color therapy (Violet for Spirit, Green for Healing) to calm the nervous system.
    * **Reprogram the Subconscious:** Daily affirmations targeted at specific chakras help break old patterns.
    * **Deepen Meditation:** The built-in Reiki timer and frequency music allow you to hold space for healing without distractions.
    * **Self-Reflect:** Journaling seeds prompt you to dive deeper into your inner wisdom.
    """)

st.title("Vixx Energy Flow")
st.write(f"✨ *Aligning your vibration for {datetime.date.today().strftime('%B %d, %Y')}*")

# 5. ALIGNMENT DATA
alignment_data = {
    "Root (Grounding)": {"affirmation": "I am safe and anchored.", "seed": "What makes you feel secure right now?"},
    "Sacral (Creativity)": {"affirmation": "I flow with creative grace.", "seed": "How can you honor your joy today?"},
    "Solar Plexus (Power)": {"affirmation": "I am strong and capable.", "seed": "Where are you reclaiming your power?"},
    "Heart (Love)": {"affirmation": "I am worthy of infinite love.", "seed": "Who can you send a breath of love to?"},
    "Throat (Truth)": {"affirmation": "I speak my truth with love.", "seed": "What truth is ready to be heard?"},
    "Third Eye (Intuition)": {"affirmation": "I trust my inner vision.", "seed": "What is your intuition showing you?"},
    "Crown (Spirit)": {"affirmation": "I am one with the divine.", "seed": "How do you feel the universe's support?"}
}

st.divider()
st.subheader("🧘 Today's Alignment")
chakra = st.selectbox("Select the energy center to focus on:", list(alignment_data.keys()))

if st.button("Activate My Spark"):
    st.snow()
    st.success(f"**Your Affirmation:** {alignment_data[chakra]['affirmation']}")
    st.info(f"**Journaling Seed:** {alignment_data[chakra]['seed']}")

# 6. HEALING MUSIC & TIMER
st.divider()
st.subheader("🎵 Ambient Frequency")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3") 

st.subheader("⏲️ Reiki Timer")
duration = st.slider("Set session minutes:", 1, 30, 5)

if st.button("Start Session"):
    bar = st.progress(0, text="Energy is flowing... breathe deep.")
    for i in range(100):
        time.sleep((duration * 60) / 100)
        bar.progress(i + 1)
    st.balloons()
    st.success("Session Complete. Stay in this peace. ✨")
