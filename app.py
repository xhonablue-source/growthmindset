import streamlit as st
import io
import openai
import requests
from PIL import Image # Keep this for robustness, though direct bytes might suffice

# --- Page Configuration ---
st.set_page_config(
    page_title="CognitiveCloud.ai: Growth Mindset Explorer",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS ---
st.markdown("""
<style>
    body {
        font-family: 'Inter', sans-serif;
        background-color: #F8F7F4;
        color: #333333;
    }
    .main-header {
        text-align: center;
        color: #6A0572;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #4B0082;
        font-size: 1.8rem;
        margin-bottom: 2rem;
    }
    .section-header {
        color: #005A9C;
        font-size: 2.2rem;
        font-weight: bold;
        margin-top: 2.5rem;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #E0E0E0;
        padding-bottom: 0.5rem;
    }
    .card {
        background-color: #FFFFFF;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
        border: 1px solid #E0E0E0;
    }
    .highlight-box {
        background-color: #E8F5E9;
        border-left: 5px solid #4CAF50;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .feedback-box {
        background-color: #e0f7fa; /* Light blue for feedback */
        border-left: 5px solid #00BCD4; /* Cyan accent */
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1rem;
        font-style: italic;
        color: #006064;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<h1 class="main-header">🌱 CognitiveCloud.ai: Growth Mindset Explorer</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Unlock Your Potential: Embrace Challenges, Learn from Mistakes, and Grow!</p>', unsafe_allow_html=True)

# --- Welcome Card with Quotes ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Welcome, Future Achiever!</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="highlight-box">
    <strong>"The tragedy of life is not that it ends so soon, but that we wait so long to begin it."</strong> - Benjamin Elijah Mays
</div>

<p style='font-size: 1.1rem;'>Your abilities grow with effort, mistakes, and perseverance. Let these voices guide your journey:</p>
<div class="highlight-box">
    <strong>"The power of 'not yet'!"</strong> - Carol Dweck
</div>
<div class="highlight-box">
    <strong>"The tragedy of life is not that it ends so soon, but that we wait so long to begin it."</strong> - Benjamin Elijah Mays
</div>
<div class="highlight-box">
    <strong>"Invest in the human soul. Who knows, it might be a diamond in the rough."</strong> - Mary McLeod Bethune
</div>
<div class="highlight-box">
    <strong>"Success is not to be measured by where you stand in life, but by the obstacles you have overcome."</strong> - Booker T. Washington
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Gallery Section ---
st.markdown('<h2 class="section-header">Meet the Mindset Leaders</h2>', unsafe_allow_html=True)
leader_images = {
    "Carol Dweck": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Carol_Dweck.jpg/220px-Carol_Dweck.jpg",
    "Benjamin Elijah Mays": "https://upload.wikimedia.org/wikipedia/commons/9/9b/Benjamin_Mays_1969.jpg",
    "Mary McLeod Bethune": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Mary_McLeod_Bethune_with_notebook.jpg/330px-Mary_McLeod_Bethune_with_notebook.jpg",
    "Booker T. Washington": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Booker_T_Washington_retouched.jpg/330px-Booker_T_Washington_retouched.jpg"
}

cols = st.columns(len(leader_images))
for col, (name, url) in zip(cols, leader_images.items()):
    with col:
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
            image_bytes = io.BytesIO(response.content)

            # Determine image format (optional, but good practice)
            if 'png' in url.lower():
                output_format = "PNG"
            elif 'jpg' in url.lower() or 'jpeg' in url.lower():
                output_format = "JPEG"
            else:
                output_format = "auto" # Let Streamlit try to infer

            st.image(image_bytes, use_column_width=True, output_format=output_format)
            st.markdown(f"<p style='text-align:center;font-weight:bold'>{name}</p>", unsafe_allow_html=True)
        except requests.exceptions.RequestException as e:
            st.warning(f"Could not load image for {name}. Error: {e}")
            # Fallback to a placeholder if image fails to load
            st.image("https://placehold.co/150x150/cccccc/000000?text=Image+Error", use_column_width=True)
            st.markdown(f"<p style='text-align:center;font-weight:bold'>{name}</p>", unsafe_allow_html=True)
        except Exception as e:
            st.warning(f"An unexpected error occurred while loading image for {name}: {e}")
            st.image("https://placehold.co/150x150/cccccc/000000?text=Image+Error", use_column_width=True)
            st.markdown(f"<p style='text-align:center;font-weight:bold'>{name}</p>", unsafe_allow_html=True)


# --- Journaling Section ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Your Growth Journal</h2>', unsafe_allow_html=True)

# Initialize session state for feedback if not already present
if 'challenge_feedback' not in st.session_state:
    st.session_state.challenge_feedback = ""
if 'effort_feedback' not in st.session_state:
    st.session_state.effort_feedback = ""
if 'mistake_feedback' not in st.session_state:
    st.session_state.mistake_feedback = ""
if 'lesson_feedback' not in st.session_state:
    st.session_state.lesson_feedback = ""
if 'action_feedback' not in st.session_state:
    st.session_state.action_feedback = ""

# Function to get LLM feedback for a specific entry
def get_llm_feedback(entry_content, entry_type):
    try:
        openai.api_key = st.secrets["OPENAI_API_KEY"]
    except KeyError:
        st.error("OpenAI API key not found in Streamlit secrets. Please configure it.")
        return "Error: API key not configured."

    system_prompt = (
        "You are Dr. X, a friendly growth mindset coach for middle and high school students. "
        "Offer supportive, encouraging, and constructive feedback based on the provided entry. "
        "Always end with a recommended resource link that is appropriate, current, and helpful for further growth mindset learning "
        "(e.g., https://www.youcubed.org/resource/growth-mindset/ or https://biglifejournal.com/blogs/blog/growth-mindset-activities-children)."
    )
    user_prompt = f"Here is my journal entry for '{entry_type}':\n\n{entry_content}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error getting feedback: {e}"


# Challenge
challenge_text = st.text_area("Describe a challenge you're facing:", height=100, key="challenge_input")
if st.button("🤖 Get Feedback for Challenge", key="feedback_challenge_btn"):
    if challenge_text.strip():
        with st.spinner("Dr. X is thinking about your challenge..."):
            st.session_state.challenge_feedback = get_llm_feedback(challenge_text, "Challenge")
    else:
        st.session_state.challenge_feedback = "Please describe your challenge before getting feedback."
if st.session_state.challenge_feedback:
    st.markdown(f'<div class="feedback-box">{st.session_state.challenge_feedback}</div>', unsafe_allow_html=True)

# Effort
effort_taken = st.text_area("What effort have you made so far?", height=100, key="effort_input")
if st.button("🤖 Get Feedback for Effort", key="feedback_effort_btn"):
    if effort_taken.strip():
        with st.spinner("Dr. X is thinking about your effort..."):
            st.session_state.effort_feedback = get_llm_feedback(effort_taken, "Effort")
    else:
        st.session_state.effort_feedback = "Please describe your effort before getting feedback."
if st.session_state.effort_feedback:
    st.markdown(f'<div class="feedback-box">{st.session_state.effort_feedback}</div>', unsafe_allow_html=True)

# Mistake
mistake_text = st.text_area("Describe a mistake you’ve made:", height=100, key="mistake_input")
if st.button("🤖 Get Feedback for Mistake", key="feedback_mistake_btn"):
    if mistake_text.strip():
        with st.spinner("Dr. X is thinking about your mistake..."):
            st.session_state.mistake_feedback = get_llm_feedback(mistake_text, "Mistake")
    else:
        st.session_state.mistake_feedback = "Please describe your mistake before getting feedback."
if st.session_state.mistake_feedback:
    st.markdown(f'<div class="feedback-box">{st.session_state.mistake_feedback}</div>', unsafe_allow_html=True)

# Lesson Learned
lesson_learned = st.text_area("What did you learn from that mistake?", height=100, key="lesson_input")
if st.button("🤖 Get Feedback for Lesson Learned", key="feedback_lesson_btn"):
    if lesson_learned.strip():
        with st.spinner("Dr. X is thinking about your lesson learned..."):
            st.session_state.lesson_feedback = get_llm_feedback(lesson_learned, "Lesson Learned")
    else:
        st.session_state.lesson_feedback = "Please describe your lesson learned before getting feedback."
if st.session_state.lesson_feedback:
    st.markdown(f'<div class="feedback-box">{st.session_state.lesson_feedback}</div>', unsafe_allow_html=True)

# Growth Action
growth_action = st.text_input("One action you’ll take to grow this week:", "e.g., Ask for help on a tough math problem", key="action_input")
if st.button("🤖 Get Feedback for Growth Action", key="feedback_action_btn"):
    if growth_action.strip():
        with st.spinner("Dr. X is thinking about your growth action..."):
            st.session_state.action_feedback = get_llm_feedback(growth_action, "Growth Action")
    else:
        st.session_state.action_feedback = "Please describe your growth action before getting feedback."
if st.session_state.action_feedback:
    st.markdown(f'<div class="feedback-box">{st.session_state.action_feedback}</div>', unsafe_allow_html=True)

# --- Export Button ---
st.markdown("---") # Separator before download button for clarity
if st.button("📅 Download My Journal as Text File"):
    buffer = io.StringIO()
    buffer.write("Growth Mindset Reflection Journal\n\n")
    buffer.write(f"Challenge: {challenge_text}\nFeedback: {st.session_state.challenge_feedback}\n\n")
    buffer.write(f"Effort: {effort_taken}\nFeedback: {st.session_state.effort_feedback}\n\n")
    buffer.write(f"Mistake: {mistake_text}\nFeedback: {st.session_state.mistake_feedback}\n\n")
    buffer.write(f"Lesson Learned: {lesson_learned}\nFeedback: {st.session_state.lesson_feedback}\n\n")
    buffer.write(f"Growth Action: {growth_action}\nFeedback: {st.session_state.action_feedback}\n")
    st.download_button(
        label="Click to download",
        data=buffer.getvalue(),
        file_name="growth_journal.txt",
        mime="text/plain"
    )
st.markdown('</div>', unsafe_allow_html=True) # Closing tag for the main card

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 2rem; color: #666;">
    <p>💡 <strong>Empowering Young Minds in STEAM</strong></p>
    <p>Developed by Xavier Honablue M.Ed for CognitiveCloud.ai Education</p>
</div>
""", unsafe_allow_html=True)
