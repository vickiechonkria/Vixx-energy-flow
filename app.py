import streamlit as st
import datetime
import time

# --- STEP 1: APPEARANCE & BRANDING ---
st.set_page_config(page_title="Vixx Energy Flow", page_icon="✨", layout="centered")

# Custom CSS to make it look "Premium"
st.markdown("""
    <style>
    .main { background-color: #fdfdfd; }
    .stButton>button { 
        background-color: #B2D8D8; 
        color: #333; 
        border-radius: 25px; 
        border: none;
        padding: 10px 24px;
        font-weight: bold;
    }
    h1 { color: #5D3FD3; font-family: 'Helvetica Neue', sans-serif; }
    .chakra-box { 
        padding: 20px; 
        border-radius: 15px; 
        background: linear-gradient(135deg, #E6E6FA 0%, #B2D8D8 100%);
        color: #333;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- STEP 2: DATA (The Vixx Curriculum) ---
vixx_content = {
    "Root (Grounding)": {
        "affirmation": "I am safe, secure, and anchored in this moment.",
        "prompt": "What physical sensations tell me I am safe right now?",
        "color": "#FF4B4B"
    },
    "Sacral (Flow)": {
        "affirmation": "I honor my emotions and allow my creativity to flow.",
        "prompt": "What creative spark have I been suppressing lately?",
        "color": "#FFA500"
    },
    "Solar Plexus (Power)": {
        "affirmation": "I am the powerful architect of my own life.",
        "prompt": "In what area of my life do I need to reclaim my power?",
        "color": "#FFD700"
    },
    "Heart (Love)": {
        "affirmation": "I lead with compassion for myself and others.",
        "prompt": "How can I show myself more grace today?",
        "color": "#28A745"
    },
    "Throat (Truth)": {
        "affirmation": "My voice is clear, honest, and filled with light.",
        "prompt": "What truth have I been holding back?",
        "color": "#007BFF"
    },
    "Third Eye (Vision)": {
        "affirmation": "I trust my intuition and follow my soul's guidance.",
        "prompt": "What is my 'gut feeling' telling me right now?",
        "color": "#6F42C1"
    },
    "Crown (Spirit)": {
        "affirmation": "I am connected to the infinite wisdom of the universe.",
        "prompt": "How do I feel connected to something larger than myself?",
        "color": "#E6E6FA"
    }
}

# --- STEP 3: APP NAVIGATION ---
st.sidebar.title("💎 Vixx Menu")
page = st.sidebar.radio("Your Daily Flow:", ["The Spark", "Energy Journal", "Reiki Timer", "The 5 Principles"])

# --- PAGE: THE SPARK (Morning Affirmation) ---
if page == "The Spark":
    st.title("Vixx Energy Flow")
    st.write("### Today's Alignment")
    
    chakra_choice = st.selectbox("Which energy center needs movement today?", list(vixx_content.keys()))
    
    if st.button("Activate My Spark"):
        st.markdown(f"""
        <div class="chakra-box">
            <h3>Your Affirmation:</h3>
            <p style="font-size: 1.2rem;">"{vixx_content[chakra_choice]['affirmation']}"</p>
        </div>
        """, unsafe_allow_html=True)
        st.write(f"**Journaling Seed:** {vixx_content[chakra_choice]['prompt']}")
        st.balloons()

# --- PAGE: ENERGY JOURNAL ---
elif page == "Energy Journal":
    st.title("📓 Sacred Journal")
    st.write(f"Today is {datetime.date.today().strftime('%B %d, %Y')}")
    
    mood = st.select_slider("My Current Frequency:", ["Heavy", "Static", "Neutral", "Flowing", "Radiant"])
    entry = st.text_area("Pour your thoughts here...", height=300, placeholder="What is moving through you today?")
    
    if st.button("Anchor This Entry"):
        st.success("Your energy has been captured and cleared. Rest well.")

# --- PAGE: REIKI TIMER ---
elif page == "Reiki Timer":
    st.title("⏳ Healing Session")
    st.write("Set your timer and place your hands on the area needing flow.")
    
    duration = st.slider("Session length (minutes):", 1, 20, 5)
    
    if st.button("Begin Session"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(duration * 60):
            time_left = (duration * 60) - i
            mins, secs = divmod(time_left, 60)
            status_text.text(f"Remaining: {mins:02d}:{secs:02d}")
            progress_bar.progress((i + 1) / (duration * 60))
            time.sleep(1)
            
        st.success("🔔 Session Complete. Take a deep breath.")

# --- PAGE: THE 5 PRINCIPLES ---
elif page == "The 5 Principles":
    st.title("📜 The Vixx Gokai")
    st.write("Repeat these five principles to ground your energy.")
    st.markdown("""
    ---
    **Just for today:**
    1. **I will not worry.**
    2. **I will not be angry.**
    3. **I will be grateful.**
    4. **I will do my work honestly.**
    5. **I will be kind to every living thing.**
    ---
    """)
    st.info("Focusing on these daily prevents energy stagnation.")
