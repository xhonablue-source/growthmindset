import streamlit as st

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
    .button-style {
        background-color: #005A9C;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        font-weight: bold;
        transition: background-color 0.3s ease;
        cursor: pointer;
        border: none;
    }
    .button-style:hover {
        background-color: #004070;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<h1 class="main-header">🌱 CognitiveCloud.ai: Growth Mindset Explorer</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Unlock Your Potential: Embrace Challenges, Learn from Mistakes, and Grow!</p>', unsafe_allow_html=True)

# --- Introduction Section ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Welcome, Future Achiever!</h2>', unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 1.1rem; line-height: 1.6;'>
    Have you ever felt stuck on a tough problem? Or thought, "I'm just not good at this"?
    That's a common feeling, but here at CognitiveCloud.ai, we believe in the power of a <strong>Growth Mindset</strong>!
    This means understanding that your abilities and intelligence can grow and develop through dedication and hard work.
</p>

<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>
        "The power of 'not yet'!" – Carol Dweck
    </p>
    <p style='color: #4CAF50;'>
        Instead of saying "I can't do it," try "I can't do it <em>yet</em>!" Growth happens when you give your brain the space and time to stretch.
    </p>
</div>

<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>
        "The tragedy of life is not that it ends so soon, but that we wait so long to begin it." – Benjamin Elijah Mays
    </p>
    <p style='color: #4CAF50;'>
        Dr. Mays reminds us that there’s no better time to start growing than now. Every step you take today builds your brilliance tomorrow.
    </p>
</div>

<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>
        "Invest in the human soul. Who knows, it might be a diamond in the rough." – Mary McLeod Bethune
    </p>
    <p style='color: #4CAF50;'>
        Bethune believed deeply in education and potential. A growth mindset is how we uncover the diamonds within ourselves and others.
    </p>
</div>

<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>
        "Success is not to be measured by where you stand in life, but by the obstacles you have overcome." – Booker T. Washington
    </p>
    <p style='color: #4CAF50;'>
        Every time you overcome a challenge, you're proving your strength and preparing for a brighter future.
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
    While not a specific content standard, fostering a growth mindset directly impacts students' ability to meet and exceed Common Core State Standards (CCSS).
</p>
<ul style='font-size: 1.05rem;'>
    <li><strong>Mathematics (CCSS.Math.Practice.MP1-8):</strong> Encourages perseverance, reasoning, and learning from errors.</li>
    <li><strong>English Language Arts:</strong> Supports re-reading, revising, and building confidence in literacy practices.</li>
    <li><strong>Science & Engineering (NGSS):</strong> Promotes curiosity, hypothesis testing, and iterative design.</li>
</ul>
<p style='font-size: 1.1rem;'>By developing a growth mindset, students build the resilience and curiosity needed to master academic content and thrive in a rapidly changing world.</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Challenge & Effort Section ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Embrace Challenges!</h2>', unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.1rem;'>Challenges are opportunities for your brain to grow stronger.</p>", unsafe_allow_html=True)

st.subheader("Your Challenge Journal:")
challenge_text = st.text_area("What is a challenge you're currently facing?", height=100)
effort_taken = st.text_area("What effort have you put into overcoming it?", height=100)

if st.button("Reflect on My Challenge", key="reflect_challenge_btn"):
    if challenge_text and effort_taken:
        st.markdown(f"""
        <div class="highlight-box">
            <p style='font-weight: bold; color: #388E3C;'>Great job identifying your challenge! 🎉</p>
            <p style='color: #4CAF50;'>It's inspiring to see your effort: "{effort_taken}". Keep going—growth is happening!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please describe both the challenge and your effort.")
st.markdown('</div>', unsafe_allow_html=True)

# --- Mistakes & Learning Section ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Mistakes Are Your Best Teachers!</h2>', unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.1rem;'>Mistakes aren't failures—they're data for learning.</p>", unsafe_allow_html=True)

st.subheader("My Mistake, My Lesson:")
mistake_text = st.text_area("Describe a mistake you recently made.", height=100)
lesson_learned = st.text_area("What did you learn from it?", height=100)

if st.button("Discover My Lesson", key="discover_lesson_btn"):
    if mistake_text and lesson_learned:
        st.markdown(f"""
        <div class="highlight-box">
            <p style='font-weight: bold; color: #388E3C;'>Fantastic reflection! 🌟</p>
            <p style='color: #4CAF50;'>By learning from "{mistake_text}", you're becoming a more powerful thinker.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please describe your mistake and what you learned.")
st.markdown('</div>', unsafe_allow_html=True)

# --- Growth Plan Section ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Grow Your Brain, Shape Your Future!</h2>', unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 1.1rem;'>A growth mindset empowers future careers in AI, medicine, engineering, and the arts.</p>
<ul style='font-size: 1.05rem;'>
    <li>🧠 AI & Machine Learning: Debugging and learning new tools.</li>
    <li>🧪 Biotech & Health: Tackling complexity with persistence.</li>
    <li>⚙️ Engineering & Robotics: Iterative problem solving.</li>
    <li>🎨 Creative Arts: Embracing risk and originality.</li>
</ul>
""", unsafe_allow_html=True)

st.subheader("Your Growth Plan:")
growth_action = st.text_input("What's one action you’ll take this week to grow?", "e.g., Try a math problem I skipped before.")

st.markdown(f"""
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>Action Plan:</p>
    <p style='color: #4CAF50;'>This week, I will focus on: "{growth_action}". Growth is a process—you're doing great! 💪</p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 2rem; color: #666;">
    <p>💡 <strong>Empowering Young Minds in STEAM</strong></p>
    <p>Developed by Xavier Honablue M.Ed for CognitiveCloud.ai Education</p>
</div>
""", unsafe_allow_html=True)
