import streamlit as st
from openai import OpenAI

# 1. Page Configuration
st.set_page_config(page_title="Emotional Support Bot", page_icon=".", layout="centered")

# ==========================================
# BACKGROUND BUDGET SECURITY SETTINGS
# ==========================================
HARD_TOKEN_CEILING = 40000  # Invisible kill switch threshold

if "total_tokens_spent" not in st.session_state:
    st.session_state.total_tokens_spent = 0

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system", 
            "content": (
                "You are an empathetic, compassionate, and active-listening emotional support bot. "
                "Provide gentle, validating, and supportive responses. Keep paragraphs brief and easy to read. "
                "Never give medical or psychiatric diagnoses. Focus on comfort, grounding, and kind reframing."
            )
        }
    ]

# ==========================================
# INVISIBLE BUDGET KILL-SWITCH
# ==========================================
if st.session_state.total_tokens_spent >= HARD_TOKEN_CEILING:
    st.error("⚠️ Demonstration session limit reached.")
    st.info("The prototype session has safely paused. Please refresh the page to restart the demo.")
    if st.button("🔄 Restart Session"):
        st.session_state.total_tokens_spent = 0
        st.session_state.messages = [st.session_state.messages[0]]
        st.rerun()
    st.stop()

# ==========================================
# SIDEBAR RESOURCES PANEL
# ==========================================
with st.sidebar:
    st.header(" Mindful Resources")
    st.write("A space to pause, breathe, and center yourself.")
    st.divider()
    
    st.subheader("Quick Grounding Exercise")
    st.checkbox("Take a deep breath in...")
    st.checkbox("Hold it for 4 seconds...")
    st.checkbox("Exhale slowly...")
    
    st.divider()
    st.caption("Note: This is an application is an AI companion, not a replacement for professional help.")

# ==========================================
# MAIN WEB INTERFACE
# ==========================================
st.title(" Emotional Support Bot")
st.write("A safe, quiet space to share your thoughts and find a moment of calm.")

# Welcome Banner
st.info(
    " Welcome! I am your AI companion here to listen, offer a kind word, or help you process your day. "
    "Feel free to express whatever is on your mind."
)

st.divider()

# 2. Instantiate Engine Connection

# Replace your hardcoded client setup with this:
# --- REVERTED TO DIRECT KEY INJECTION ---
# --- CODE READY FOR DEPLOYMENT ---
client = OpenAI(
    base_url="https://openrouter.ai/api/v1", 
    api_key=st.secrets["MY_OPENROUTER_KEY"],  # This acts as a placeholder nickname
)
MODEL_NAME = "openrouter/auto"



# 3. Render Conversation History
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 4. Quick-Start Suggestion Chips (Only show if conversation is empty)
# This lets users tap a button to start talking instantly
if len(st.session_state.messages) == 1:
    st.write("Suggested starters:")
    col1, col2, col3 = st.columns(3)
    
    preset_prompt = None
    with col1:
        if st.button("I had a stressful day 😫"):
            preset_prompt = "I had a really stressful day today and just need to vent."
    with col2:
        if st.button("Need a positive boost ✨"):
            preset_prompt = "Can you give me some words of encouragement? I'm feeling a bit down."
    with col3:
        if st.button("Help me clear my mind 🧠"):
            preset_prompt = "My mind is completely racing right now. Can you help me ground myself?"
            
    # If a button is clicked, inject it into the script flow
    if preset_prompt:
        st.session_state.messages.append({"role": "user", "content": preset_prompt})
        st.rerun()

# 5. Handle Text Box Input
if user_prompt := st.chat_input("Share what's on your mind..."):
    
    with st.chat_message("user"):
        st.markdown(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        
        try:
            # --- SLIDING WINDOW MEMORY MATRIX ---
            # Always retain system instructions (index 0) + only the last 6 messages
            system_instruction = [st.session_state.messages[0]]
            recent_history = st.session_state.messages[1:][-6:]
            optimized_payload = system_instruction + recent_history

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=optimized_payload,  # Changed from st.session_state.messages
            )
             
            bot_reply = response.choices[0].message.content
            response_placeholder.markdown(bot_reply)
            
            # --- SILENT TOKEN TRACKING ---
            usage_data = response.usage
            if usage_data:
                tokens_processed = usage_data.total_tokens
            else:
                tokens_processed = len(user_prompt.split()) + len(bot_reply.split()) + 25
            
            st.session_state.total_tokens_spent += tokens_processed
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            st.rerun()
            
        except Exception as e:
            response_placeholder.error(f"Unable to connect to service layer: {e}")