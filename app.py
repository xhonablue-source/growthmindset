import streamlit as st
import io

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
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<h1 class="main-header">🌱 CognitiveCloud.ai: Growth Mindset Explorer</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Unlock Your Potential: Embrace Challenges, Learn from Mistakes, and Grow!</p>', unsafe_allow_html=True)

# --- Welcome Card with Quotes ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Welcome, Future Achiever!</h2>', unsafe_allow_html=True)

# FIX: Wrapped the problematic HTML block in st.markdown()
st.markdown("""
<div class="highlight-box">
    <strong>"The tragedy of life is not that it ends so soon, but that we wait so long to begin it."</strong> – Benjamin Elijah Mays
</div>
""", unsafe_allow_html=True)

st.markdown("""
<p style='font-size: 1.1rem;'>Your abilities grow with effort, mistakes, and perseverance. Let these voices guide your journey:</p>
<div class="highlight-box">
    <strong>"The power of 'not yet'!"</strong> – Carol Dweck
</div>
<div class="highlight-box">
    <strong>"The tragedy of life is not that it ends so soon, but that we wait so long to begin it."</strong> – Benjamin Elijah Mays
</div>
<div class="highlight-box">
    <strong>"Invest in the human soul. Who knows, it might be a diamond in the rough."</strong> – Mary McLeod Bethune
</div>
<div class="highlight-box">
    <strong>"Success is not to be measured by where you stand in life, but by the obstacles you have overcome."</strong> – Booker T. Washington
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
        st.image(url, use_column_width=True)
        st.markdown(f"<p style='text-align:center;font-weight:bold'>{name}</p>", unsafe_allow_html=True)

# --- Journaling Section ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Your Growth Journal</h2>', unsafe_allow_html=True)
challenge_text = st.text_area("Describe a challenge you're facing:", height=100)
effort_taken = st.text_area("What effort have you made so far?", height=100)
mistake_text = st.text_area("Describe a mistake you’ve made:", height=100)
lesson_learned = st.text_area("What did you learn from that mistake?", height=100)
growth_action = st.text_input("One action you’ll take to grow this week:", "e.g., Ask for help on a tough math problem")

# --- Export Button ---
if st.button("📅 Download My Journal as Text File"):
    buffer = io.StringIO()
    buffer.write("Growth Mindset Reflection Journal\n\n")
    buffer.write(f"Challenge: {challenge_text}\n")
    buffer.write(f"Effort: {effort_taken}\n\n")
    buffer.write(f"Mistake: {mistake_text}\n")
    buffer.write(f"Lesson Learned: {lesson_learned}\n\n")
    buffer.write(f"Growth Action: {growth_action}\n")
    st.download_button(
        label="Click to download",
        data=buffer.getvalue(),
        file_name="growth_journal.txt",
        mime="text/plain"
    )
st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 2rem; color: #666;">
    <p>💡 <strong>Empowering Young Minds in STEAM</strong></p>
    <p>Developed by Xavier Honablue M.Ed for CognitiveCloud.ai Education</p>
</div>
""", unsafe_allow_html=True)
```
