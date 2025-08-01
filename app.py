import streamlit as st
import io
import time # For exponential backoff (though less critical with external API)
import json # For parsing JSON responses
import requests # For making HTTP requests
# Removed: import openai (as it's handled by the external API)
# Removed: import os (as it's no longer used for direct API key handling)

# --- Page Configuration ---
st.set_page_config(
    page_title="CognitiveCloud.ai: Growth Mindset Explorer",
    page_icon="🌱", # A plant icon to symbolize growth
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for consistent styling (Inter font, CognitiveCloud.ai colors) ---
st.markdown("""
<style>
    body {
        font-family: 'Inter', sans-serif;
        background-color: #F8F7F4; /* Light neutral background */
        color: #333333; /* Dark text for readability */
    }
    .main-header {
        text-align: center;
        color: #6A0572; /* CognitiveCloud.ai primary header color */
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #4B0082; /* CognitiveCloud.ai secondary header color */
        font-size: 1.8rem;
        margin-bottom: 2rem;
    }
    .section-header {
        color: #005A9C; /* CognitiveCloud.ai accent blue */
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
        background-color: #E8F5E9; /* Light green for positive reinforcement */
        border-left: 5px solid #4CAF50; /* Green accent */
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }
    /* Updated button styling to target Streamlit's default button elements */
    .stButton > button {
        background-color: #005A9C; /* Accent blue button */
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        font-weight: bold;
        transition: background-color 0.3s ease;
        cursor: pointer;
        border: none;
        margin-top: 10px; /* Add some space below the text area */
    }
    .stButton > button:hover {
        background-color: #004070; /* Darker blue on hover */
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
<p style='font-size: 1.1rem;'>Your abilities grow with effort, mistakes, and perseverance. Let these voices guide your journey:</p>
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>
        "The power of 'not yet'!" - Carol Dweck
    </p>
    <p style='color: #4CAF50;'>
        Instead of saying "I can't do it," try "I can't do it *yet*!" This simple shift opens up possibilities for learning and improvement.
    </p>
</div>
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>
        "Success is not to be measured by where you stand in life, but by the obstacles you have overcome." - Booker T. Washington
    </p>
    <p style='color: #4CAF50;'>
        This powerful quote reminds us that true achievement comes from facing and conquering difficulties, not just from natural talent. Every challenge you overcome builds your capacity for future success.
    </p>
</div>
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>
        "The tragedy of life is not that it ends so soon, but that we wait so long to begin it." - Benjamin Elijah Mays
    </p>
    <p style='color: #4CAF50;'>
        Dr. Mays' words encourage us to seize the moment, embrace learning, and start pursuing our potential now, without hesitation or fear of failure. Every day is an opportunity to grow!
    </p>
</div>
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>
        "Invest in the human soul. Who knows, it might be a diamond in the rough." - Mary McLeod Bethune
    </p>
    <p style='color: #4CAF50;'>
        Mary McLeod Bethune's inspiring words highlight the immense, often hidden, potential within each individual, encouraging us to nurture and believe in our own and others' capacity for greatness.
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Common Core Connections Section ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Connections to Common Core Standards</h2>', unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 1.1rem; line-height: 1.6;'>
    A growth mindset is a powerful tool that supports learning across all subjects and grade levels.
    While not a specific content standard, fostering a growth mindset directly impacts students' ability to meet and exceed Common Core State Standards (CCSS) in various disciplines.
</p>
<ul class="list-disc list-inside text-gray-700 space-y-2 mb-4">
    <li>**Mathematics (CCSS.Math.Practice.MP1-8):** The Standards for Mathematical Practice emphasize problem-solving, perseverance, reasoning, and precision. A growth mindset directly cultivates these practices by encouraging students to:
        <ul>
            <li>**Make sense of problems and persevere in solving them (MP1):** Students with a growth mindset view challenging problems as opportunities to learn, rather than obstacles.</li>
            <li>**Reason abstractly and quantitatively (MP2):** They are more willing to try different approaches and learn from mistakes when reasoning.</li>
            <li>**Attend to precision (MP6):** They see errors as feedback to improve their accuracy and understanding.</li>
        </ul>
    </li>
    <li>**English Language Arts (CCSS.ELA-Literacy.R.CCR.1-10, W.CCR.1-10):** A growth mindset helps students in ELA by:
        <ul>
            <li>**Reading closely and making logical inferences (R.CCR.1):** They are more open to re-reading and re-evaluating texts when faced with comprehension challenges.</li>
            <li>**Producing clear and coherent writing (W.CCR.4):** They embrace the iterative process of drafting, revising, and editing, seeing it as a path to better writing.</li>
        </ul>
    </li>
    <li>**Science & Engineering Practices (NGSS):** Similar to math, a growth mindset is essential for scientific inquiry and engineering design, encouraging students to:
        <ul>
            <li>**Ask questions and define problems (SEP1):** They are curious and not afraid to explore unknowns.</li>
            <li>**Construct explanations and design solutions (SEP6):** They persist through failures and iterate on their designs.</li>
        </ul>
    </li>
</ul>
<p style='font-size: 1.1rem; line-height: 1.6;'>
    By developing a growth mindset, students build the resilience and intellectual curiosity needed to master academic content and thrive in a rapidly changing world.
</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# Initialize session state for Dr. X chat (for general chat)
if 'general_chat_history' not in st.session_state:
    st.session_state.general_chat_history = [
        {"role": "assistant", "content": "Hello! I'm Dr. X, your AI growth mindset coach. How can I help you explore your potential today?"}
    ]

# Dr. X API function (from Quarterback Crown)
def ask_drx(message):
    try:
        response = requests.post(
            'https://ask-drx-730124987572.us-central1.run.app',
            json={'message': message},
            timeout=30
        )
        if response.status_code == 200:
            return response.json().get('reply', "Sorry, I couldn't process that.")
        else:
            return f"I'm having trouble connecting right now. Server responded with status {response.status_code}. Please try again."
    except requests.exceptions.Timeout:
        return "I'm having trouble connecting right now. The request timed out. Please try again."
    except requests.exceptions.ConnectionError:
        return "I'm having trouble connecting right now. There was a network error. Please check your internet connection and try again."
    except Exception as e:
        return f"I'm having trouble connecting right now. An unexpected error occurred: {e}. Please try again."

# --- Dr. X General Chat Interface ---
st.header("💬 Talk to Dr. X (General Chat)")
st.markdown("Ask Dr. X anything about growth mindset, challenges, mistakes, or your personal growth journey!")

# Display chat messages from history on app rerun
for message in st.session_state.general_chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask Dr. X about your growth...", key="drx_general_chat_input"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.general_chat_history.append({"role": "user", "content": prompt})

    with st.spinner("Dr. X is thinking..."):
        assistant_response = ask_drx(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
    # Add assistant response to chat history
    st.session_state.general_chat_history.append({"role": "assistant", "content": assistant_response})


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

# Function to get LLM feedback for a specific entry (now uses ask_drx)
def get_llm_feedback_journal(entry_content, entry_type):
    user_prompt = f"As a growth mindset coach, provide supportive, encouraging, and constructive feedback on this journal entry for '{entry_type}':\n\n{entry_content}\n\nRemember to end with a relevant resource link."
    return ask_drx(user_prompt)


# Challenge Entry
challenge_text = st.text_area("Describe a challenge you're facing:", height=100, key="journal_challenge_text")
# Changed from `if challenge_text:` to a button click to trigger feedback
if st.button("Get Feedback on Challenge", key="feedback_challenge_btn"):
    if challenge_text.strip():
        with st.spinner("Dr. X is thinking..."):
            st.session_state.challenge_feedback = get_llm_feedback_journal(challenge_text, "a challenge")
    else:
        st.session_state.challenge_feedback = "Please describe your challenge before getting feedback."
if st.session_state.challenge_feedback:
    st.markdown(f"<div class='feedback-box'>{st.session_state.challenge_feedback}</div>", unsafe_allow_html=True)

# Effort Entry
effort_taken = st.text_area("What effort have you made so far?", height=100, key="journal_effort_taken")
# Changed from `if effort_taken:` to a button click to trigger feedback
if st.button("Get Feedback on Effort", key="feedback_effort_btn"):
    if effort_taken.strip():
        with st.spinner("Dr. X is thinking..."):
            st.session_state.effort_feedback = get_llm_feedback_journal(effort_taken, "effort made")
    else:
        st.session_state.effort_feedback = "Please describe your effort before getting feedback."
if st.session_state.effort_feedback:
    st.markdown(f"<div class='feedback-box'>{st.session_state.effort_feedback}</div>", unsafe_allow_html=True)

# Mistake Entry
mistake_text = st.text_area("Describe a mistake you’ve made:", height=100, key="journal_mistake_text")
# Changed from `if mistake_text:` to a button click to trigger feedback
if st.button("Get Feedback on Mistake", key="feedback_mistake_btn"):
    if mistake_text.strip():
        with st.spinner("Dr. X is thinking..."):
            st.session_state.mistake_feedback = get_llm_feedback_journal(mistake_text, "a mistake")
    else:
        st.session_state.mistake_feedback = "Please describe your mistake before getting feedback."
if st.session_state.mistake_feedback:
    st.markdown(f"<div class='feedback-box'>{st.session_state.mistake_feedback}</div>", unsafe_allow_html=True)

# Lesson Learned Entry
lesson_learned = st.text_area("What did you learn from that mistake?", height=100, key="journal_lesson_learned")
# Changed from `if lesson_learned:` to a button click to trigger feedback
if st.button("Get Feedback on Lesson Learned", key="feedback_lesson_btn"):
    if lesson_learned.strip():
        with st.spinner("Dr. X is thinking..."):
            st.session_state.lesson_feedback = get_llm_feedback_journal(lesson_learned, "a lesson learned")
    else:
        st.session_state.lesson_feedback = "Please describe your lesson learned before getting feedback."
if st.session_state.lesson_feedback:
    st.markdown(f"<div class='feedback-box'>{st.session_state.lesson_feedback}</div>", unsafe_allow_html=True)

# Growth Action Entry
growth_action = st.text_input("One action you’ll take to grow this week:", "e.g., Ask for help on a tough math problem", key="journal_growth_action")
# Changed from `if growth_action:` to a button click to trigger feedback
if st.button("Get Feedback on Growth Action", key="feedback_growth_action_btn"):
    if growth_action.strip():
        with st.spinner("Dr. X is thinking..."):
            st.session_state.action_feedback = get_llm_feedback_journal(growth_action, "an action step")
    else:
        st.session_state.action_feedback = "Please enter a growth action before getting feedback."
if st.session_state.action_feedback:
    st.markdown(f"<div class='feedback-box'>{st.session_state.action_feedback}</div>", unsafe_allow_html=True)

# --- Export Button ---
if st.button("📅 Download My Journal as Text File", key="download_journal_btn"):
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
        mime="text/plain",
        key="download_button_final"
    )
st.markdown('</div>', unsafe_allow_html=True)


# --- Actionable Steps & Future Connections (Moved from previous location to be separate from journal) ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Grow Your Brain, Shape Your Future!</h2>', unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 1.1rem; line-height: 1.6;'>
    Your brain is like a muscle – the more you challenge it and learn from your experiences, the stronger it gets!
    This growth mindset isn't just for school; it's a superpower for life.
    It helps you tackle new technologies, solve complex problems, and innovate in fields like:
</p>
<ul class="list-disc list-inside text-gray-700 space-y-2 mb-4">
    <li>**Artificial Intelligence & Machine Learning:** Learning new algorithms and debugging code.</li>
    <li>**Biotechnology & Medicine:** Discovering new treatments and understanding complex biological systems.</li>
    <li>**Engineering & Robotics:** Designing, building, and refining innovative solutions.</li>
    <li>**Creative Arts & Design:** Pushing boundaries and developing unique styles.</li>
</ul>
<p style='font-size: 1.1rem; line-height: 1.6;'>
    Every time you persist, every time you learn from a mistake, you're building the skills you'll need to excel in these future-forward careers!
</p>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>
        Remember: Consistency is key to growth! You've got this! 💪
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 2rem; color: #666;'>
    <p>💡 <strong>Empowering Young Minds in STEAM</strong></p>
    <p>Developed by Xavier Honablue M.Ed for CognitiveCloud.ai Education</p>
</div>
""", unsafe_allow_html=True)
