import streamlit as st
from sarvamai import SarvamAI
from dotenv import load_dotenv
import os
import requests
import time

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="💖 Sweatable - Your AI Girlfriend",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CHARACTER DATA ====================
CHARACTER_DATA = {
    "Romantic GF": {"emoji": "💕", "desc": "Sweet & Loving"},
    "Caring GF": {"emoji": "🤗", "desc": "Nurturing & Kind"},
    "Flirty GF": {"emoji": "😘", "desc": "Playful & Charming"},
    "Supportive GF": {"emoji": "🤝", "desc": "Always There"},
    "Coder GF": {"emoji": "👩‍💻", "desc": "Tech Savvy Love"},
    "Spiritual GF": {"emoji": "🧘‍♀️", "desc": "Peaceful Soul"},
    "Normal GF": {"emoji": "😊", "desc": "Just Perfect"},
    "Shy GF": {"emoji": "😳", "desc": "Adorably Timid"},
    "Angry GF": {"emoji": "😤", "desc": "Fiery Passion"},
    "Moody GF": {"emoji": "🌙", "desc": "Mysterious Vibes"},
    "GenZ GF": {"emoji": "😎", "desc": "Cool & Trendy"},
    "Indian GF": {"emoji": "🌺", "desc": "I am Indian Queen"},
    "American GF": {"emoji": "🗽", "desc": "Western Charm"},
    "Abhijit The GenZ Casanova": {"emoji": "😈", "desc": "Smooth Talker"},
    "Rajeeb The Cyber Sage": {"emoji": "🧙‍♂️", "desc": "Tech Wizard"},
    "OAM the Tense Techie": {"emoji": "😅", "desc": "Stressed Genius"},
    "Rahul The Ghoster": {"emoji": "👻", "desc": "Ghoster King"},
    "Ramakanta The Gentle Guy": {"emoji": "🕊️", "desc": "Pure Heart"},
    "Gamer Boy Saroj": {"emoji": "🎮", "desc": "Gaming Pro"},
    "Krishna The Random Guy": {"emoji": "🕺", "desc": "Expert at affairs/Love Snatcher"},
    "Dreamer Boy": {"emoji": "💭", "desc": "Lost in Dreams"},
    "Gym Bro": {"emoji": "💪", "desc": "Fitness King"},
    "The Meme Lord": {"emoji": "😂", "desc": "Comedy Gold"},
    "Tech Nerd": {"emoji": "🤓", "desc": "Code Master"},
    "Red Flag": {"emoji": "🚩", "desc": "Drama King"},
    "Green Flag King": {"emoji": "💚", "desc": "Perfect Gentleman"},
}

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global Styles */
    .stApp {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
        min-height: 100vh;
    }
    
    /* Main container */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 900px;
    }
    
    /* Header Styles */
    .header-container {
        text-align: center;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(25px);
        border-radius: 25px;
        padding: 2.5rem 2rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    }
    
    .main-title {
        font-family: 'Poppins', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(45deg, #ff6b6b, #feca57, #48dbfb, #ff9ff3);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientShift 4s ease-in-out infinite;
        margin-bottom: 0.5rem;
        text-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .subtitle {
        color: rgba(255, 255, 255, 0.95);
        font-size: 1.3rem;
        font-weight: 300;
        margin-bottom: 1rem;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    
    /* Character Selector */
    .character-selector {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 20px rgba(31, 38, 135, 0.2);
        
    }
    
    .selector-title {
        color: white;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1rem;
        text-align: center;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* Language Selector */
    .language-selector {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 20px rgba(31, 38, 135, 0.2);
    }
    
    .language-title {
        color: white;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1rem;
        text-align: center;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* Chat Header */
    .chat-header {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.1));
        backdrop-filter: blur(25px);
        border-radius: 20px 20px 0 0;
        padding: 1.5rem 2rem;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-bottom: none;
        text-align: center;
        box-shadow: 0 4px 20px rgba(31, 38, 135, 0.2);
    }
    
    .chat-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.4rem;
        font-weight: 600;
        color: white;
        margin: 0;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        letter-spacing: 0.5px;
    }
    
    /* Chat Messages */
    .chat-container {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border-radius: 0 0 20px 20px;
        padding: 2rem 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-top: none;
        min-height: 450px;
        max-height: 650px;
        overflow-y: auto;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.2);
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 1.2rem 1.8rem;
        border-radius: 25px 25px 8px 25px;
        margin: 1rem 0 1rem 2rem;
        max-width: 85%;
        float: right;
        clear: both;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        animation: slideInRight 0.4s ease-out;
        position: relative;
        word-wrap: break-word;
    }
    
    .assistant-message {
        background: rgba(255, 255, 255, 0.18);
        color: white;
        padding: 1.2rem 1.8rem;
        border-radius: 25px 25px 25px 8px;
        margin: 1rem 2rem 1rem 0;
        max-width: 85%;
        float: left;
        clear: both;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
        animation: slideInLeft 0.4s ease-out;
        position: relative;
        word-wrap: break-word;
    }
    
    @keyframes slideInRight {
        from { transform: translateX(100%) scale(0.8); opacity: 0; }
        to { transform: translateX(0) scale(1); opacity: 1; }
    }
    
    @keyframes slideInLeft {
        from { transform: translateX(-100%) scale(0.8); opacity: 0; }
        to { transform: translateX(0) scale(1); opacity: 1; }
    }
    
    .message-label {
        font-weight: 600;
        font-size: 0.85rem;
        opacity: 0.9;
        margin-bottom: 0.6rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .user-label {
        color: rgba(255, 255, 255, 0.95);
    }
    
    .assistant-label {
        color: #ff9ff3;
    }
    
    /* Input Area */
    .input-container {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(25px);
        border-radius: 25px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.3);
        position: sticky;
        bottom: 0;
        z-index: 100;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.3);
    }
    
    /* Style Streamlit input */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.15);
        border: 2px solid rgba(255, 255, 255, 0.4);
        border-radius: 0px;
        color: white;
        padding: 0.2rem 1rem;
        font-size: 1.1rem;
        backdrop-filter: blur(15px);
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.7);
        font-weight: 400;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #ff6b6b;
        box-shadow: 0 0 25px rgba(255, 107, 107, 0.4);
        background: rgba(255, 255, 255, 0.2);
        transform: scale(1.02);
    }
    
    /* Style buttons */
    .stButton > button {
        background: linear-gradient(45deg, #ff6b6b, #feca57);
        border: none;
        border-radius: 30px;
        color: white;
        font-weight: 600;
        padding: 1rem 2.5rem;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        width: 100%;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 10px 30px rgba(255, 107, 107, 0.5);
        background: linear-gradient(45deg, #ff5252, #ffc107);
    }
    
    /* Selection buttons */
    .selection-buttons .stButton > button {
        background: rgba(255, 255, 255, 0.12);
        border: 2px solid rgba(255, 255, 255, 0.3);
        padding: 0.8rem 1.2rem;
        font-size: 0.95rem;
        min-width: 120px;
        transition: all 0.3s ease;
    }
    
    .selection-buttons .stButton > button:hover {
        background: rgba(255, 255, 255, 0.2);
        border-color: rgba(255, 255, 255, 0.5);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 255, 255, 0.2);
    }
    
    /* Welcome message */
    .welcome-message {
        text-align: center;
        color: rgba(255, 255, 255, 0.9);
        padding: 3rem 2rem;
        font-size: 1.2rem;
        line-height: 1.7;
    }
    
    .welcome-emoji {
        font-size: 4rem;
        margin-bottom: 1.5rem;
        display: block;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    
    /* Loading indicator */
    .typing-indicator {
        background: rgba(255, 255, 255, 0.18);
        border-radius: 25px 25px 25px 8px;
        padding: 1.2rem 1.8rem;
        margin: 1rem 2rem 1rem 0;
        max-width: 120px;
        float: left;
        clear: both;
        animation: pulse 1.8s infinite;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 0.6; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.02); }
    }
    
    /* Error messages */
    .stAlert {
        background: rgba(255, 107, 107, 0.25);
        border: 1px solid rgba(255, 107, 107, 0.5);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        color: white;
    }
    
    /* Scrollbar */
    .chat-container::-webkit-scrollbar {
        width: 8px;
    }
    
    .chat-container::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    .chat-container::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.4);
        border-radius: 10px;
        transition: background 0.3s ease;
    }
    
    .chat-container::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.6);
    }
    
    /* Mobile responsive */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.5rem;
        }
        
        .chat-title {
            font-size: 1.1rem;
        }
        
        .user-message, .assistant-message {
            max-width: 90%;
            margin-left: 0.5rem;
            margin-right: 0.5rem;
            padding: 1rem 1.3rem;
        }
        
        .selection-buttons .stButton > button {
            min-width: 90px;
            font-size: 0.85rem;
            padding: 0.6rem 1rem;
        }
        
        .input-container {
            padding: 1.5rem;
        }
        
        .chat-container {
            min-height: 400px;
            max-height: 500px;
        }
    }
    
    .stSelectbox > div > div { 
    background: rgba(255, 255, 255, 0.2) !important;
    color: white !important;
    border-radius: 15px !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# ==================== INITIALIZATION ====================
load_dotenv()
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

if not SARVAM_API_KEY:
    st.error("⚠️ Missing SARVAM_API_KEY. Please check your .env file.")
    st.stop()

try:
    client = SarvamAI(api_subscription_key=SARVAM_API_KEY)
except Exception as e:
    st.error(f"⚠️ Failed to initialize SarvamAI client: {e}")
    st.stop()

# ==================== SUPPORTED LANGUAGES ====================
LANGUAGES = {
    "🇺🇸 English": "en-IN",
    "🇮🇳 हिंदी": "hi-IN", 
    "🇧🇩 বাংলা": "bn-IN",
    "🇮🇳 ગુજરાતી": "gu-IN",
    "🇮🇳 ಕನ್ನಡ": "kn-IN",
    "🇮🇳 ଓଡ଼ିଆ": "od-IN",
    "🇮🇳 ਪੰਜਾਬੀ": "pa-IN"
}

# ==================== SESSION STATE ====================
if "active_lang" not in st.session_state:
    st.session_state.active_lang = "🇺🇸 English"

if "selected_character" not in st.session_state:
    st.session_state.selected_character = "Romantic"

if "chat_initialized" not in st.session_state:
    st.session_state.chat_initialized = True
    for lang in LANGUAGES:
        for char in CHARACTER_DATA:
            chat_key = f"chat_history_{lang}_{char}"
            display_key = f"display_history_{lang}_{char}"
            if chat_key not in st.session_state:
                ls = char.split()
                ls = ls[0]
                st.session_state[chat_key] = [
                    {
                        "role": "system",
                        "content": os.getenv(ls) 
                        # "content": os.getenv(char, f"You are {char}, an AI companion.") 
                    }
                ]
            if display_key not in st.session_state:
                st.session_state[display_key] = []

# ==================== HEADER ====================
st.markdown("""
<div class="header-container">
    <div class="main-title">💖 Sweatable</div>
    <div class="subtitle">Your AI Companion - Chat in Your Language</div>
</div>
""", unsafe_allow_html=True)

# ==================== CHARACTER SELECTOR ====================
st.markdown("""
<div class="character-selector">
    <div class="selector-title">🧑‍🎤 Choose Your Character</div>
</div>
""", unsafe_allow_html=True)

# Create character selection in a grid
# char_cols = st.columns(4)
characters = list(CHARACTER_DATA.keys())

# for i, char in enumerate(characters):
#     col_idx = i % 4
#     with char_cols[col_idx]:
#         char_data = CHARACTER_DATA[char]
#         button_text = f"{char_data['emoji']} {char}"
#         if st.button(button_text, key=f"char_{i}", help=char_data['desc']):
#             st.session_state.selected_character = char
#             st.rerun()
#Default selected character
# if "selected_character" not in st.session_state:
#     st.session_state.selected_character = characters[0]

# # Create the selectbox with emoji and name
options = [f"{CHARACTER_DATA[char]['emoji']} {char}" for char in characters]

selected_option = st.selectbox("Choose Me Baby",options)

# Set the selected character in session state
selected_name = selected_option.split(" ", 1)[1]  # Extract name from "emoji name"
st.session_state.selected_character = selected_name

# Optional: Show selected character description
desc = CHARACTER_DATA[st.session_state.selected_character]['desc']
st.markdown(
    f"""
    <div style='text-align: center; font-weight: bold;'>
        📝 Short Description About Your Love : {desc}
    </div>
    """,
    unsafe_allow_html=True
)


# ==================== LANGUAGE SELECTOR ====================
st.markdown("""
<div class="language-selector">
    <div class="language-title">🌐 Choose Your Language</div>
</div>
""", unsafe_allow_html=True)

# Create language selection buttons
lang_cols = st.columns(len(LANGUAGES))
for i, lang in enumerate(LANGUAGES):
    with lang_cols[i]:
        if st.button(lang, key=f"lang_{i}"):
            st.session_state.active_lang = lang
            st.rerun()

# ==================== CURRENT CHAT SETUP ====================
current_lang = st.session_state.active_lang
current_char = st.session_state.selected_character
target_lang_code = LANGUAGES[current_lang]
chat_history_key = f"chat_history_{current_lang}_{current_char}"
display_history_key = f"display_history_{current_lang}_{current_char}"

# Get character data
char_data = CHARACTER_DATA[current_char]
lang_name = current_lang.split(' ')[-1] if ' ' in current_lang else current_lang

# ==================== CHAT HEADER ====================
st.markdown(f"""
<div class="chat-header">
    <div class="chat-title">{char_data['emoji']} {current_char} • {lang_name} • {char_data['desc']}</div>
</div>
""", unsafe_allow_html=True)

# ==================== CHAT DISPLAY ====================
# st.markdown('<div class="chat-container">', unsafe_allow_html=True)

if not st.session_state[display_history_key]:
    st.markdown(f"""
    <div class="welcome-message">
        <span class="welcome-emoji">{char_data['emoji']}</span>
        <div>Hey there! I'm your {current_char} companion! ✨</div>
        <div>{char_data['desc']} - Ready to chat? Just type a message below! 💕</div>
    </div>  
    """, unsafe_allow_html=True)
else:
    for message in st.session_state[display_history_key]:
        st.markdown(message, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ==================== INPUT AREA ====================
# st.markdown('<div class="input-container">', unsafe_allow_html=True)

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "Message", 
        placeholder=f"Chat with your {current_char} companion... {char_data['emoji']}",
        label_visibility="collapsed",
        key="user_message_input"
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        submitted = st.form_submit_button(f"Send Message {char_data['emoji']}", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# ==================== HANDLE CHAT ====================
if submitted and user_input.strip():
    # Add user message
    st.session_state[chat_history_key].append({"role": "user", "content": user_input})
    
    user_message_html = f"""
    <div class="user-message">
        <div class="message-label user-label">You 👤</div>
        <div>{user_input}</div>
    </div>
    """
    st.session_state[display_history_key].append(user_message_html)
    
    # Show typing indicator
    typing_html = f'<div class="typing-indicator">{char_data["emoji"]} Typing...</div>'
    st.session_state[display_history_key].append(typing_html)
    st.rerun()

# Handle API call if there's a pending user message
if (st.session_state[chat_history_key] and 
    st.session_state[chat_history_key][-1]["role"] == "user" and
    st.session_state[display_history_key] and
    "Typing..." in st.session_state[display_history_key][-1]):
    
    try:
        # Remove typing indicator
        st.session_state[display_history_key].pop()
        
        # API call
        headers = {
            "Authorization": f"Bearer {SARVAM_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "sarvam-m",
            "messages": st.session_state[chat_history_key],
            "max_tokens": 500,
            "temperature": 0.7
        }
        
        with st.spinner(f"{char_data['emoji']} Thinking..."):
            response = requests.post(
                "https://api.sarvam.ai/v1/chat/completions", 
                headers=headers, 
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            
            assistant_reply = response.json()["choices"][0]["message"]["content"]
            
            # Translate if needed
            if target_lang_code != "en-IN":
                translation = client.text.translate(
                    input=assistant_reply,
                    source_language_code="en-IN",
                    target_language_code=target_lang_code,
                    speaker_gender="Female" if "GF" in current_char or current_char in ["Romantic", "Caring", "Flirty", "Coder GF", "Spiritual", "Shy", "Moody", "GenZ", "Indian GF", "American GF"] else "Male"
                )
                final_reply = translation.translated_text
            else:
                final_reply = assistant_reply
            
            # Add assistant message
            st.session_state[chat_history_key].append({"role": "assistant", "content": final_reply})
            
            assistant_message_html = f"""
            <div class="assistant-message">
                <div class="message-label assistant-label">{current_char} {char_data['emoji']}</div>
                <div>{final_reply}</div>
            </div>
            """
            st.session_state[display_history_key].append(assistant_message_html)
            
    except requests.exceptions.Timeout:
        st.error("⏰ Request timed out. Please try again.")
        if st.session_state[display_history_key]:
            st.session_state[display_history_key].pop()
    except requests.exceptions.RequestException as e:
        st.error(f"🌐 Network Error: {str(e)}")
        if st.session_state[display_history_key]:
            st.session_state[display_history_key].pop()
    except KeyError as e:
        st.error(f"📝 API Response Error: Missing expected data in response")
        if st.session_state[display_history_key]:
            st.session_state[display_history_key].pop()
    except Exception as e:
        st.error(f"⚠️ Something went wrong: {str(e)}")
        if st.session_state[display_history_key]:
            st.session_state[display_history_key].pop()
    
    st.rerun()

# ==================== FOOTER ====================
st.markdown(f"""
<div style="text-align: center; margin-top: 2rem; padding: 1.5rem; 
            background: rgba(255, 255, 255, 0.05); border-radius: 15px; 
            backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1);">
    <small style="color: rgba(255, 255, 255, 0.8); font-size: 0.9rem;">
        ✨ Made with love by Sweatable Team | Currently chatting with {char_data['emoji']} {current_char} ✨
    </small>
</div>
""", unsafe_allow_html=True)

# ==================== AUTO-SCROLL SCRIPT ====================
st.markdown("""
<script>
// Auto-scroll to bottom of chat
function scrollToBottom() {
    const chatContainer = document.querySelector('.chat-container');
    if (chatContainer) {
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
}

// Run on page load and after updates
document.addEventListener('DOMContentLoaded', scrollToBottom);
setTimeout(scrollToBottom, 100);

// Smooth scroll animation
function smoothScrollToBottom() {
    const chatContainer = document.querySelector('.chat-container');
    if (chatContainer) {
        chatContainer.scrollTo({
            top: chatContainer.scrollHeight,
            behavior: 'smooth'
        });
    }
}

// Enhanced scroll behavior
setInterval(smoothScrollToBottom, 500);
</script>
""", unsafe_allow_html=True)