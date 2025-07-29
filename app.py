import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

# --- Page Setup ---
st.set_page_config(
    page_title="MathCraft: Positive Mindset Math", 
    page_icon="🌟", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Initialize Session State ---
if 'student_name' not in st.session_state:
    st.session_state.student_name = ""
if 'current_week' not in st.session_state:
    st.session_state.current_week = 1
if 'confidence_scores' not in st.session_state:
    st.session_state.confidence_scores = [5, 5, 5, 5]  # Weekly confidence scores
if 'completed_activities' not in st.session_state:
    st.session_state.completed_activities = {
        'week_1': [],
        'week_2': [],
        'week_3': [],
        'week_4': []
    }
if 'daily_reflections' not in st.session_state:
    st.session_state.daily_reflections = {}
if 'challenge_level' not in st.session_state:
    st.session_state.challenge_level = "Explorer"

# --- Helper Functions ---
def update_confidence_score(week, score):
    st.session_state.confidence_scores[week-1] = score

def mark_activity_complete(week, activity):
    week_key = f'week_{week}'
    if activity not in st.session_state.completed_activities[week_key]:
        st.session_state.completed_activities[week_key].append(activity)

def get_progress_percentage(week):
    week_key = f'week_{week}'
    total_activities = 5  # Each week has 5 main activities
    completed = len(st.session_state.completed_activities[week_key])
    return min(100, (completed / total_activities) * 100)

# --- Header ---
def render_header():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        try:
            st.image("njit_logo.png", width=80)
        except:
            st.markdown("🏫")
    
    with col2:
        st.markdown("""
        <div style='text-align: center;'>
            <h1 style='color: #4B0082; margin: 0;'>🧠 MathCraft</h1>
            <h3 style='margin: 0;'>Your Mind. Your Math. Your Power.</h3>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("### www.cognitivecloud.ai")
        st.markdown("**Xavier Honablue M.Ed**")

# --- Sidebar Navigation ---
def render_sidebar():
    st.sidebar.title("🚀 Your Journey")
    
    # Student Profile
    if not st.session_state.student_name:
        st.session_state.student_name = st.sidebar.text_input("✨ What's your name?", placeholder="Enter your name")
    else:
        st.sidebar.success(f"Welcome, {st.session_state.student_name}! 🌟")
    
    # Challenge Level
    st.session_state.challenge_level = st.sidebar.selectbox(
        "🎯 Choose Your Challenge Level:",
        ["Explorer", "Adventurer", "Champion", "Master"]
    )
    
    # Week Navigation
    st.sidebar.markdown("### 📅 Weekly Progress")
    for week in range(1, 5):
        progress = get_progress_percentage(week)
        if st.sidebar.button(f"Week {week}: {['Foundation', 'Connection', 'Application', 'Mastery'][week-1]} ({progress:.0f}%)", 
                           key=f"week_nav_{week}"):
            st.session_state.current_week = week
    
    # Overall Progress Chart
    st.sidebar.markdown("### 📊 Confidence Tracker")
    fig, ax = plt.subplots(figsize=(6, 3))
    weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
    ax.plot(weeks, st.session_state.confidence_scores, marker='o', color='#4B0082')
    ax.set_ylim(1, 10)
    ax.set_ylabel('Confidence Level')
    ax.set_title('Your Math Confidence Journey')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.sidebar.pyplot(fig)
    plt.close()

# --- Week Content ---
def render_week_content(week_num):
    weeks_data = {
        1: {
            'title': '🌱 Foundation Week: "I Can Learn Math"',
            'theme': 'Building Basic Confidence',
            'color': '#28a745',
            'activities': [
                {
                    'name': 'Growth Mindset Visualization',
                    'description': 'Create a visual representation of your brain growing',
                    'type': 'creative'
                },
                {
                    'name': 'Math Anxiety Assessment',
                    'description': 'Identify and address your math fears',
                    'type': 'reflection'
                },
                {
                    'name': 'Personal Math Story',
                    'description': 'Write about your relationship with math',
                    'type': 'writing'
                },
                {
                    'name': 'Basic Problem Solving',
                    'description': 'Start with problems you can solve',
                    'type': 'practice'
                },
                {
                    'name': 'Success Celebration',
                    'description': 'Document and celebrate small wins',
                    'type': 'reflection'
                }
            ]
        },
        2: {
            'title': '🔗 Connection Week: "Math is Everywhere"',
            'theme': 'Connecting Math to Real Life',
            'color': '#17a2b8',
            'activities': [
                {
                    'name': 'Math in My Life Hunt',
                    'description': 'Find math in your daily activities',
                    'type': 'exploration'
                },
                {
                    'name': 'Career Math Connections',
                    'description': 'Explore how math relates to your future',
                    'type': 'research'
                },
                {
                    'name': 'Real-World Problem Solving',
                    'description': 'Solve problems that matter to you',
                    'type': 'practice'
                },
                {
                    'name': 'Math Interview Project',
                    'description': 'Interview someone about math in their job',
                    'type': 'project'
                },
                {
                    'name': 'Connection Reflection',
                    'description': 'Reflect on new math connections discovered',
                    'type': 'reflection'
                }
            ]
        },
        3: {
            'title': '🚀 Application Week: "I Can Use Math"',
            'theme': 'Applying Math Skills Confidently',
            'color': '#ffc107',
            'activities': [
                {
                    'name': 'Challenge Problem Set',
                    'description': 'Tackle progressively harder problems',
                    'type': 'practice'
                },
                {
                    'name': 'Math Teaching Moment',
                    'description': 'Teach a math concept to someone else',
                    'type': 'teaching'
                },
                {
                    'name': 'Creative Math Project',
                    'description': 'Create something using mathematical concepts',
                    'type': 'project'
                },
                {
                    'name': 'Mistake Analysis',
                    'description': 'Learn from errors and misconceptions',
                    'type': 'reflection'
                },
                {
                    'name': 'Progress Celebration',
                    'description': 'Celebrate your growing abilities',
                    'type': 'celebration'
                }
            ]
        },
        4: {
            'title': '👑 Mastery Week: "I Am a Mathematician"',
            'theme': 'Embracing Mathematical Identity',
            'color': '#6f42c1',
            'activities': [
                {
                    'name': 'Mathematical Identity Essay',
                    'description': 'Write about becoming a mathematician',
                    'type': 'writing'
                },
                {
                    'name': 'Capstone Project',
                    'description': 'Complete a significant math challenge',
                    'type': 'project'
                },
                {
                    'name': 'Peer Mentoring',
                    'description': 'Help another student with math',
                    'type': 'mentoring'
                },
                {
                    'name': 'Future Math Goals',
                    'description': 'Plan your continued math journey',
                    'type': 'planning'
                },
                {
                    'name': 'Journey Reflection',
                    'description': 'Reflect on your 4-week transformation',
                    'type': 'reflection'
                }
            ]
        }
    }
    
    week_data = weeks_data[week_num]
    
    # Week Header
    st.markdown(f"""
    <div style='background: linear-gradient(90deg, {week_data['color']}, #ffffff); 
                padding: 2rem; border-radius: 10px; margin-bottom: 2rem;'>
        <h2 style='color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>{week_data['title']}</h2>
        <h4 style='color: white; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);'>{week_data['theme']}</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Progress Bar
    progress = get_progress_percentage(week_num)
    st.progress(progress / 100, text=f"Week {week_num} Progress: {progress:.0f}%")
    
    # Activities
    st.markdown("### 📋 This Week's Activities")
    
    for i, activity in enumerate(week_data['activities']):
        activity_key = f"week_{week_num}_activity_{i}"
        is_completed = activity['name'] in st.session_state.completed_activities[f'week_{week_num}']
        
        with st.expander(f"{'✅' if is_completed else '📝'} {activity['name']}", expanded=not is_completed):
            st.markdown(f"**Type:** {activity['type'].title()}")
            st.markdown(f"**Description:** {activity['description']}")
            
            # Activity-specific content
            if activity['type'] == 'reflection':
                reflection_key = f"{activity_key}_reflection"
                reflection = st.text_area(
                    "Your reflection:",
                    value=st.session_state.daily_reflections.get(reflection_key, ""),
                    key=reflection_key,
                    placeholder="Share your thoughts and insights..."
                )
                if reflection:
                    st.session_state.daily_reflections[reflection_key] = reflection
            
            elif activity['type'] == 'practice':
                render_practice_problems(week_num, activity['name'])
            
            elif activity['type'] == 'creative' or activity['type'] == 'project':
                st.file_uploader(f"Upload your {activity['name']}", 
                               type=['png', 'jpg', 'pdf', 'docx'], 
                               key=f"{activity_key}_upload")
            
            # Mark as complete button
            if not is_completed:
                if st.button(f"Mark '{activity['name']}' as Complete", key=f"{activity_key}_complete"):
                    mark_activity_complete(week_num, activity['name'])
                    st.success(f"Great job completing '{activity['name']}'! 🎉")
                    st.rerun()
    
    # Weekly Confidence Check
    st.markdown("### 🎯 Weekly Confidence Check")
    current_confidence = st.session_state.confidence_scores[week_num - 1]
    new_confidence = st.slider(
        "How confident do you feel about math this week?",
        min_value=1, max_value=10, value=current_confidence,
        help="1 = Not confident at all, 10 = Extremely confident"
    )
    
    if new_confidence != current_confidence:
        update_confidence_score(week_num, new_confidence)
        st.success(f"Confidence level updated to {new_confidence}/10! 📈")

def render_practice_problems(week_num, activity_name):
    """Render practice problems based on challenge level and week"""
    problems = {
        1: {  # Foundation Week
            "Explorer": [
                {"problem": "What is 15 + 27?", "answer": 42},
                {"problem": "Calculate 8 × 9", "answer": 72},
                {"problem": "What is 100 - 37?", "answer": 63}
            ],
            "Adventurer": [
                {"problem": "Solve: 3x + 5 = 14", "answer": 3},
                {"problem": "What is 25% of 80?", "answer": 20},
                {"problem": "Find the area of a rectangle: length = 12, width = 8", "answer": 96}
            ],
            "Champion": [
                {"problem": "Solve: 2x² - 8x + 6 = 0", "answer": "x = 1 or x = 3"},
                {"problem": "Find the slope of the line passing through (2,3) and (5,9)", "answer": 2},
                {"problem": "Calculate: sin(30°) + cos(60°)", "answer": 1}
            ],
            "Master": [
                {"problem": "Find the derivative of f(x) = 3x³ - 2x² + 5x - 1", "answer": "f'(x) = 9x² - 4x + 5"},
                {"problem": "Solve the system: 3x + 2y = 12, x - y = 1", "answer": "x = 2, y = 3"},
                {"problem": "Find the integral of ∫(2x + 3)dx", "answer": "x² + 3x + C"}
            ]
        }
        # Add more weeks and levels as needed
    }
    
    level_problems = problems.get(week_num, {}).get(st.session_state.challenge_level, [])
    
    if level_problems:
        st.markdown(f"**Practice Problems for {st.session_state.challenge_level} Level:**")
        for i, prob in enumerate(level_problems):
            st.markdown(f"**Problem {i+1}:** {prob['problem']}")
            user_answer = st.text_input(f"Your answer for Problem {i+1}:", key=f"prob_{week_num}_{i}")
            if user_answer:
                # Simple answer checking (in real app, you'd want more sophisticated checking)
                if str(user_answer).strip().lower() == str(prob['answer']).lower():
                    st.success("Correct! Great job! 🎉")
                else:
                    st.info(f"Keep trying! The answer is: {prob['answer']}")

# --- Dashboard ---
def render_dashboard():
    st.markdown("## 📊 Your MathCraft Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Current Week", st.session_state.current_week, delta=None)
    
    with col2:
        avg_confidence = np.mean(st.session_state.confidence_scores)
        st.metric("Avg Confidence", f"{avg_confidence:.1f}/10", delta=None)
    
    with col3:
        total_activities = sum(len(activities) for activities in st.session_state.completed_activities.values())
        st.metric("Activities Completed", total_activities, delta=None)
    
    with col4:
        overall_progress = np.mean([get_progress_percentage(w) for w in range(1, 5)])
        st.metric("Overall Progress", f"{overall_progress:.0f}%", delta=None)
    
    # Confidence Chart
    st.markdown("### 📈 Confidence Journey")
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        y=st.session_state.confidence_scores,
        mode='lines+markers',
        name='Confidence Level',
        line=dict(color='#4B0082', width=3),
        marker=dict(size=10)
    ))
    fig.update_layout(
        title="Your Math Confidence Over Time",
        xaxis_title="Week",
        yaxis_title="Confidence Level (1-10)",
        yaxis=dict(range=[0, 10])
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Resources Page ---
def render_resources():
    st.markdown("## 🔗 Growth Mindset & Math Resources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🧠 Mindset Resources
        - [Mindset Works Official Site](https://sites.google.com/mindsetworks.com/mindsetworks/home)
        - [YouCubed: Growth Mindset Resources](https://www.youcubed.org/resource/growth-mindset/)
        - [Khan Academy: Growth Mindset](https://www.khanacademy.org/youcanlearnanything)
        - [Angela Duckworth: Grit (TED Talk)](https://www.ted.com/talks/angela_lee_duckworth_grit_the_power_of_passion_and_perseverance)
        """)
    
    with col2:
        st.markdown("""
        ### 📚 Math Learning Tools
        - [Desmos Graphing Calculator](https://www.desmos.com/calculator)
        - [Khan Academy Math](https://www.khanacademy.org/math)
        - [Equitable Math](https://equitablemath.org/)
        - [Math is Fun](https://www.mathsisfun.com/)
        """)
    
    st.markdown("""
    ### 🌱 Daily Affirmations
    > "I'm not good at math... **YET**."
    
    > "Mistakes help my brain grow stronger."
    
    > "Math is about thinking, not just getting the right answer."
    
    > "I can learn anything with time and effort."
    """)

# --- Main App ---
def main():
    render_header()
    render_sidebar()
    
    # Main content area
    if st.session_state.student_name:
        tab1, tab2, tab3 = st.tabs(["📅 Current Week", "📊 Dashboard", "🔗 Resources"])
        
        with tab1:
            render_week_content(st.session_state.current_week)
        
        with tab2:
            render_dashboard()
        
        with tab3:
            render_resources()
    else:
        st.markdown("""
        ## Welcome to MathCraft! 🌟
        
        ### 🌱 Growth Mindset in Mathematics
        A **growth mindset** means believing that abilities improve with effort and the right tools. 
        In this app, you'll:
        - Build confidence through structured activities
        - Connect math to your real life
        - Prove that math is for **everyone**
        
        **Please enter your name in the sidebar to begin your 4-week confidence journey!**
        """)
    
    # Footer
    st.markdown("""
    ---
    <p style='font-size: 0.8rem; text-align: center;'>
    Built with ❤️ by Xavier Honablue, M.Ed | MathCraft Initiative | All rights reserved.
    </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
