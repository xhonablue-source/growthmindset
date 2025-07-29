import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
import random

# --- Page Setup ---
st.set_page_config(
    page_title="MathCraft: Common Core Confidence Journey", 
    page_icon="🌟", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Common Core Standards Database ---
COMMON_CORE_STANDARDS = {
    # Grade 6
    6: {
        'ratios': {
            'standard': '6.RP.A.1',
            'description': 'Understand the concept of a ratio and use ratio language to describe relationships',
            'problems': [
                {'problem': 'In a class of 24 students, 9 are boys. What is the ratio of boys to girls?', 'answer': '9:15 or 3:5', 'solution': 'Girls = 24-9 = 15. Ratio = 9:15 = 3:5'},
                {'problem': 'A recipe calls for 2 cups flour to 3 cups sugar. How much flour for 9 cups sugar?', 'answer': '6 cups', 'solution': '2:3 = x:9, so x = 6'}
            ]
        },
        'expressions': {
            'standard': '6.EE.A.2',
            'description': 'Write, read, and evaluate expressions in which letters stand for numbers',
            'problems': [
                {'problem': 'Write an expression for "5 more than 3 times a number n"', 'answer': '3n + 5', 'solution': '3 times n is 3n, then add 5'},
                {'problem': 'Evaluate 2x + 7 when x = 4', 'answer': '15', 'solution': '2(4) + 7 = 8 + 7 = 15'}
            ]
        },
        'geometry': {
            'standard': '6.G.A.1',
            'description': 'Find area of triangles, quadrilaterals, and polygons',
            'problems': [
                {'problem': 'Find the area of a triangle with base 8 cm and height 6 cm', 'answer': '24 cm²', 'solution': 'Area = ½ × base × height = ½ × 8 × 6 = 24'},
                {'problem': 'A rectangle has length 12 ft and width 7 ft. Find its area.', 'answer': '84 ft²', 'solution': 'Area = length × width = 12 × 7 = 84'}
            ]
        }
    },
    # Grade 7
    7: {
        'proportions': {
            'standard': '7.RP.A.2',
            'description': 'Recognize and represent proportional relationships between quantities',
            'problems': [
                {'problem': 'If 3 pizzas cost $24, how much do 5 pizzas cost?', 'answer': '$40', 'solution': '3:24 = 5:x, so x = 40'},
                {'problem': 'A car travels 180 miles in 3 hours. At this rate, how far in 5 hours?', 'answer': '300 miles', 'solution': 'Rate = 180÷3 = 60 mph. Distance = 60×5 = 300'}
            ]
        },
        'integers': {
            'standard': '7.NS.A.1',
            'description': 'Apply properties of operations as strategies to add and subtract rational numbers',
            'problems': [
                {'problem': 'Calculate: (-15) + (+8)', 'answer': '-7', 'solution': 'Different signs: subtract and keep sign of larger: 15-8=7, negative'},
                {'problem': 'Find: (+12) - (-5)', 'answer': '17', 'solution': 'Subtracting negative = adding positive: 12 + 5 = 17'}
            ]
        },
        'equations': {
            'standard': '7.EE.B.4',
            'description': 'Use variables to represent quantities in real-world problems',
            'problems': [
                {'problem': 'Solve: 3x + 8 = 23', 'answer': 'x = 5', 'solution': '3x = 23-8 = 15, so x = 15÷3 = 5'},
                {'problem': 'A number increased by 12 equals 35. Find the number.', 'answer': '23', 'solution': 'x + 12 = 35, so x = 35-12 = 23'}
            ]
        }
    },
    # Grade 8
    8: {
        'linear_equations': {
            'standard': '8.EE.C.7',
            'description': 'Solve linear equations in one variable',
            'problems': [
                {'problem': 'Solve: 4(x - 3) = 2x + 6', 'answer': 'x = 9', 'solution': '4x - 12 = 2x + 6, 2x = 18, x = 9'},
                {'problem': 'Solve: 3x/4 + 5 = 14', 'answer': 'x = 12', 'solution': '3x/4 = 9, 3x = 36, x = 12'}
            ]
        },
        'functions': {
            'standard': '8.F.A.1',
            'description': 'Understand that a function assigns exactly one output to each input',
            'problems': [
                {'problem': 'Is this a function? {(1,2), (2,4), (3,6), (2,8)}', 'answer': 'No', 'solution': 'Input 2 has two outputs (4 and 8), so not a function'},
                {'problem': 'If f(x) = 2x + 3, find f(5)', 'answer': '13', 'solution': 'f(5) = 2(5) + 3 = 10 + 3 = 13'}
            ]
        },
        'geometry': {
            'standard': '8.G.B.7',
            'description': 'Apply the Pythagorean Theorem',
            'problems': [
                {'problem': 'Find the hypotenuse of a right triangle with legs 3 and 4', 'answer': '5', 'solution': 'c² = 3² + 4² = 9 + 16 = 25, so c = 5'},
                {'problem': 'A ladder reaches 12 ft up a wall, base is 5 ft from wall. Find ladder length.', 'answer': '13 ft', 'solution': 'c² = 12² + 5² = 144 + 25 = 169, so c = 13'}
            ]
        }
    },
    # High School Algebra
    9: {
        'quadratics': {
            'standard': 'A-REI.B.4',
            'description': 'Solve quadratic equations in one variable',
            'problems': [
                {'problem': 'Solve: x² - 5x + 6 = 0', 'answer': 'x = 2 or x = 3', 'solution': 'Factor: (x-2)(x-3) = 0, so x = 2 or x = 3'},
                {'problem': 'Solve using quadratic formula: x² + 4x - 5 = 0', 'answer': 'x = 1 or x = -5', 'solution': 'x = (-4 ± √(16+20))/2 = (-4 ± 6)/2'}
            ]
        },
        'systems': {
            'standard': 'A-REI.C.6',
            'description': 'Solve systems of linear equations',
            'problems': [
                {'problem': 'Solve: 2x + y = 7, x - y = 2', 'answer': 'x = 3, y = 1', 'solution': 'Add equations: 3x = 9, so x = 3. Then y = 7-6 = 1'},
                {'problem': 'Solve: 3x + 2y = 12, x + y = 5', 'answer': 'x = 2, y = 3', 'solution': 'From second: x = 5-y. Substitute: 3(5-y) + 2y = 12'}
            ]
        },
        'exponentials': {
            'standard': 'A-SSE.B.3',
            'description': 'Choose and produce equivalent forms of expressions',
            'problems': [
                {'problem': 'Simplify: (2³)² × 2⁴', 'answer': '2¹⁰ = 1024', 'solution': '2⁶ × 2⁴ = 2¹⁰ = 1024'},
                {'problem': 'If 2ˣ = 16, find x', 'answer': 'x = 4', 'solution': '2ˣ = 2⁴, so x = 4'}
            ]
        }
    }
}

# --- Initialize Session State ---
if 'student_name' not in st.session_state:
    st.session_state.student_name = ""
if 'current_week' not in st.session_state:
    st.session_state.current_week = 1
if 'confidence_scores' not in st.session_state:
    st.session_state.confidence_scores = [5, 5, 5, 5]
if 'completed_activities' not in st.session_state:
    st.session_state.completed_activities = {
        'week_1': [], 'week_2': [], 'week_3': [], 'week_4': []
    }
if 'daily_reflections' not in st.session_state:
    st.session_state.daily_reflections = {}
if 'challenge_level' not in st.session_state:
    st.session_state.challenge_level = "Grade 6"
if 'problem_scores' not in st.session_state:
    st.session_state.problem_scores = {}
if 'mastery_tracker' not in st.session_state:
    st.session_state.mastery_tracker = {}

# --- Helper Functions ---
def get_grade_level(challenge_level):
    grade_map = {"Grade 6": 6, "Grade 7": 7, "Grade 8": 8, "High School": 9}
    return grade_map.get(challenge_level, 6)

def get_common_core_content(grade, topic):
    return COMMON_CORE_STANDARDS.get(grade, {}).get(topic, {})

def update_confidence_score(week, score):
    st.session_state.confidence_scores[week-1] = score

def mark_activity_complete(week, activity):
    week_key = f'week_{week}'
    if reflection:
        st.session_state.daily_reflections[activity_key] = reflection

def render_standards_mastery_check(week_num):
    st.markdown("### 🎯 Weekly Standards Mastery Check")
    
    grade = get_grade_level(st.session_state.challenge_level)
    week_standards = {
        1: ['Number Systems', 'Basic Operations', 'Mathematical Practices'],
        2: ['Ratios & Proportions', 'Expressions & Equations', 'Statistics'],
        3: ['Functions', 'Geometry', 'Mathematical Modeling'],
        4: ['Advanced Topics', 'Integrated Problem Solving', 'Communication']
    }
    
    standards = week_standards.get(week_num, [])
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Standards for this week:**")
        for standard in standards:
            mastery_key = f"{grade}_{standard}_{week_num}"
            current_level = st.session_state.mastery_tracker.get(mastery_key, "Beginning")
            
            new_level = st.selectbox(
                f"{standard}:",
                ["Beginning", "Developing", "Proficient", "Mastery"],
                index=["Beginning", "Developing", "Proficient", "Mastery"].index(current_level),
                key=f"mastery_{mastery_key}"
            )
            st.session_state.mastery_tracker[mastery_key] = new_level
    
    with col2:
        st.markdown("**Mastery Level Guide:**")
        st.markdown("""
        - **Beginning:** Still learning basic concepts
        - **Developing:** Understanding most concepts with support
        - **Proficient:** Can apply concepts independently
        - **Mastery:** Can teach others and solve complex problems
        """)

# --- Dashboard ---
def render_dashboard():
    st.markdown("## 📊 Your MathCraft Dashboard")
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Current Week", st.session_state.current_week)
    
    with col2:
        avg_confidence = np.mean(st.session_state.confidence_scores)
        st.metric("Avg Confidence", f"{avg_confidence:.1f}/10")
    
    with col3:
        total_activities = sum(len(activities) for activities in st.session_state.completed_activities.values())
        st.metric("Activities Completed", total_activities)
    
    with col4:
        overall_progress = np.mean([get_progress_percentage(w) for w in range(1, 5)])
        st.metric("Overall Progress", f"{overall_progress:.0f}%")
    
    # Standards Mastery Overview
    st.markdown("### 📈 Common Core Standards Mastery")
    
    if st.session_state.mastery_tracker:
        mastery_df = pd.DataFrame([
            {"Standard": key.split('_')[1], "Week": key.split('_')[2], "Level": value}
            for key, value in st.session_state.mastery_tracker.items()
        ])
        
        # Convert mastery levels to numeric for visualization
        level_map = {"Beginning": 1, "Developing": 2, "Proficient": 3, "Mastery": 4}
        mastery_df['Level_Numeric'] = mastery_df['Level'].map(level_map)
        
        fig = px.bar(mastery_df, x='Standard', y='Level_Numeric', color='Level',
                    title='Standards Mastery Progress',
                    color_discrete_map={
                        'Beginning': '#ff4444',
                        'Developing': '#ffaa44', 
                        'Proficient': '#44aaff',
                        'Mastery': '#44ff44'
                    })
        fig.update_yaxis(tickvals=[1,2,3,4], ticktext=['Beginning','Developing','Proficient','Mastery'])
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Complete some activities to see your standards mastery progress!")
    
    # Confidence Journey Chart
    st.markdown("### 📈 Confidence Journey")
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        y=st.session_state.confidence_scores,
        mode='lines+markers',
        name='Confidence Level',
        line=dict(color='#4B0082', width=3),
        marker=dict(size=12)
    ))
    fig.update_layout(
        title="Your Math Confidence Over Time",
        xaxis_title="Week",
        yaxis_title="Confidence Level (1-10)",
        yaxis=dict(range=[0, 10])
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Problem Solving Performance
    if st.session_state.problem_scores:
        st.markdown("### 🎯 Problem Solving Performance")
        
        performance_data = []
        for topic, scores in st.session_state.problem_scores.items():
            if scores:
                avg_score = np.mean(scores)
                performance_data.append({
                    'Topic': topic.replace('_', ' ').title(),
                    'Average Score': avg_score,
                    'Problems Attempted': len(scores)
                })
        
        if performance_data:
            perf_df = pd.DataFrame(performance_data)
            fig = px.bar(perf_df, x='Topic', y='Average Score', 
                        title='Average Scores by Topic',
                        color='Average Score',
                        color_continuous_scale='RdYlGn')
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)

# --- Resources Page ---
def render_resources():
    st.markdown("## 🔗 Common Core & Growth Mindset Resources")
    
    tab1, tab2, tab3 = st.tabs(["📚 Common Core", "🧠 Growth Mindset", "🛠️ Math Tools"])
    
    with tab1:
        st.markdown("### Common Core Mathematics Resources")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Official Standards & Documentation:**
            - [Common Core State Standards - Mathematics](http://www.corestandards.org/Math/)
            - [Illustrative Mathematics](https://www.illustrativemathematics.org/)
            - [Achieve the Core](https://achievethecore.org/category/774/mathematics-focus-by-grade-level)
            - [UnboundEd Mathematics](https://www.unbounded.org/mathematics)
            """)
        
        with col2:
            st.markdown("""
            **Grade-Level Specific Resources:**
            - [Grade 6 Math Standards](http://www.corestandards.org/Math/Content/6/introduction/)
            - [Grade 7 Math Standards](http://www.corestandards.org/Math/Content/7/introduction/)
            - [Grade 8 Math Standards](http://www.corestandards.org/Math/Content/8/introduction/)
            - [High School Math Standards](http://www.corestandards.org/Math/Content/HSA/introduction/)
            """)
        
        st.markdown("### Mathematical Practices")
        practices = [
            "Make sense of problems and persevere in solving them",
            "Reason abstractly and quantitatively", 
            "Construct viable arguments and critique the reasoning of others",
            "Model with mathematics",
            "Use appropriate tools strategically",
            "Attend to precision",
            "Look for and make use of structure",
            "Look for and express regularity in repeated reasoning"
        ]
        
        for i, practice in enumerate(practices, 1):
            st.markdown(f"**Practice {i}:** {practice}")
    
    with tab2:
        st.markdown("### Growth Mindset Resources")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Research & Theory:**
            - [Mindset Works](https://www.mindsetworks.com/)
            - [YouCubed Growth Mindset](https://www.youcubed.org/resource/growth-mindset/)
            - [Carol Dweck's Research](https://mindsetonline.com/)
            - [Mathematical Mindsets by Jo Boaler](https://www.youcubed.org/mathematical-mindsets/)
            """)
        
        with col2:
            st.markdown("""
            **Practical Applications:**
            - [Growth Mindset Interventions](https://www.mindsetworks.com/science/)
            - [Math Anxiety Resources](https://www.youcubed.org/math-anxiety/)
            - [Building Mathematical Confidence](https://www.edutopia.org/math-anxiety-growth-mindset)
            - [Parent Resources](https://www.mindsetworks.com/parents/)
            """)
        
        st.markdown("### 🌱 Daily Affirmations for Math Success")
        affirmations = [
            "I'm not good at math... **YET**.",
            "Mistakes help my brain grow stronger.",
            "Math is about thinking, not just getting the right answer.",
            "I can learn anything with time and effort.",
            "My mathematical abilities can be developed.",
            "Challenging problems help me learn more.",
            "I am becoming a mathematical thinker.",
            "Every mathematician started as a beginner."
        ]
        
        for affirmation in affirmations:
            st.markdown(f"> {affirmation}")
    
    with tab3:
        st.markdown("### Mathematical Tools & Technology")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Graphing & Visualization:**
            - [Desmos Graphing Calculator](https://www.desmos.com/calculator)
            - [GeoGebra](https://www.geogebra.org/)
            - [Wolfram Alpha](https://www.wolframalpha.com/)
            - [Matplotlib (Python)](https://matplotlib.org/)
            """)
        
        with col2:
            st.markdown("""
            **Learning Platforms:**
            - [Khan Academy](https://www.khanacademy.org/math)
            - [IXL Math](https://www.ixl.com/math/)
            - [Prodigy Math](https://www.prodigygame.com/)
            - [DeltaMath](https://www.deltamath.com/)
            """)
        
        st.markdown("""
        ### 🎯 Study Strategies for Common Core Math
        
        **Before You Start:**
        - Read the problem carefully and identify what's being asked
        - Look for key vocabulary and mathematical relationships
        - Consider what strategies might be helpful
        
        **During Problem Solving:**
        - Show your work step by step
        - Use multiple representations (words, numbers, pictures, graphs)
        - Check your answers for reasonableness
        
        **After Solving:**
        - Reflect on your solution method
        - Consider if there are other ways to solve the problem
        - Connect the problem to other mathematical concepts
        """)

# --- Main Content Renderer ---
def render_week_content(week_num):
    render_week_activities(week_num)
    
    # Weekly Confidence Check
    st.markdown("---")
    st.markdown("### 🎯 Weekly Confidence Check")
    
    current_confidence = st.session_state.confidence_scores[week_num - 1]
    new_confidence = st.slider(
        "How confident do you feel about math this week?",
        min_value=1, max_value=10, value=current_confidence,
        help="1 = Not confident at all, 10 = Extremely confident",
        key=f"confidence_week_{week_num}"
    )
    
    if new_confidence != current_confidence:
        update_confidence_score(week_num, new_confidence)
        st.success(f"Confidence level updated to {new_confidence}/10! 📈")

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
        
        ### 🌱 Growth Mindset Meets Common Core
        
        MathCraft combines **growth mindset principles** with **Common Core mathematics standards** 
        to create a personalized learning journey that builds both skills and confidence.
        
        **What makes MathCraft different:**
        - ✅ Aligned with Common Core State Standards
        - ✅ Personalized to your grade level
        - ✅ Builds mathematical practices alongside content
        - ✅ Tracks mastery of specific standards
        - ✅ Emphasizes growth mindset and resilience
        
        ### 🎯 Your 4-Week Journey:
        - **Week 1:** Foundation - Master basic concepts and build confidence
        - **Week 2:** Connection - See math in the real world around you  
        - **Week 3:** Application - Apply skills to solve complex problems
        - **Week 4:** Mastery - Demonstrate your mathematical thinking
        
        **Ready to begin? Enter your name in the sidebar to start your journey!**
        """)
    
    # Footer
    st.markdown("""
    ---
    <p style='font-size: 0.8rem; text-align: center; color: #666;'>
    Built with ❤️ by Xavier Honablue, M.Ed | MathCraft Initiative<br>
    Aligned with Common Core State Standards | All rights reserved.
    </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() activity not in st.session_state.completed_activities[week_key]:
        st.session_state.completed_activities[week_key].append(activity)

def get_progress_percentage(week):
    week_key = f'week_{week}'
    total_activities = 5
    completed = len(st.session_state.completed_activities[week_key])
    return min(100, (completed / total_activities) * 100)

def calculate_mastery_level(topic_scores):
    if not topic_scores:
        return 0
    avg_score = np.mean(list(topic_scores.values()))
    if avg_score >= 90:
        return "Mastery"
    elif avg_score >= 80:
        return "Proficient"
    elif avg_score >= 70:
        return "Developing"
    else:
        return "Beginning"

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
            <h3 style='margin: 0;'>Common Core Confidence Journey</h3>
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
    
    # Challenge Level (Grade Level)
    st.session_state.challenge_level = st.sidebar.selectbox(
        "🎯 Choose Your Challenge Level:",
        ["Grade 6", "Grade 7", "Grade 8", "High School"]
    )
    
    # Week Navigation
    st.sidebar.markdown("### 📅 Weekly Progress")
    week_names = ['Foundation', 'Connection', 'Application', 'Mastery']
    for week in range(1, 5):
        progress = get_progress_percentage(week)
        if st.sidebar.button(f"Week {week}: {week_names[week-1]} ({progress:.0f}%)", 
                           key=f"week_nav_{week}"):
            st.session_state.current_week = week
    
    # Confidence Tracker
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

# --- Common Core Practice Problems ---
def render_cc_practice_problems(week_num, topic_focus):
    grade = get_grade_level(st.session_state.challenge_level)
    
    # Get topics based on week
    topic_map = {
        1: ['ratios', 'expressions', 'integers'],  # Foundation
        2: ['proportions', 'equations', 'linear_equations'],  # Connection
        3: ['geometry', 'functions', 'systems'],  # Application
        4: ['quadratics', 'exponentials', 'geometry']  # Mastery
    }
    
    available_topics = []
    for topic in topic_map[week_num]:
        if topic in COMMON_CORE_STANDARDS.get(grade, {}):
            available_topics.append(topic)
    
    if not available_topics:
        # Fall back to grade 6 content
        grade = 6
        available_topics = [topic for topic in topic_map[week_num] if topic in COMMON_CORE_STANDARDS.get(grade, {})]
    
    if available_topics:
        selected_topic = st.selectbox(f"Choose a topic for Week {week_num}:", available_topics, key=f"topic_week_{week_num}")
        topic_content = get_common_core_content(grade, selected_topic)
        
        if topic_content:
            st.markdown(f"**📋 Common Core Standard:** {topic_content['standard']}")
            st.markdown(f"**🎯 Learning Goal:** {topic_content['description']}")
            
            # Practice Problems
            st.markdown("### 📝 Practice Problems")
            problems = topic_content.get('problems', [])
            
            topic_key = f"{grade}_{selected_topic}"
            if topic_key not in st.session_state.problem_scores:
                st.session_state.problem_scores[topic_key] = []
            
            for i, prob_data in enumerate(problems):
                with st.expander(f"Problem {i+1}: {prob_data['problem']}", expanded=True):
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        user_answer = st.text_input(
                            f"Your answer:", 
                            key=f"answer_{week_num}_{selected_topic}_{i}",
                            placeholder="Enter your answer here..."
                        )
                        
                        if user_answer:
                            if st.button(f"Check Answer", key=f"check_{week_num}_{selected_topic}_{i}"):
                                correct_answer = prob_data['answer'].lower().replace(" ", "")
                                user_clean = user_answer.lower().replace(" ", "")
                                
                                if correct_answer in user_clean or user_clean in correct_answer:
                                    st.success("🎉 Correct! Great job!")
                                    st.session_state.problem_scores[topic_key].append(100)
                                else:
                                    st.error(f"Not quite. The correct answer is: {prob_data['answer']}")
                                    st.session_state.problem_scores[topic_key].append(50)
                                    
                                st.info(f"**Solution:** {prob_data['solution']}")
                    
                    with col2:
                        if st.button(f"Show Hint", key=f"hint_{week_num}_{selected_topic}_{i}"):
                            st.info(prob_data['solution'])

# --- Week Activities ---
def render_week_activities(week_num):
    activities_data = {
        1: {  # Foundation Week
            'title': '🌱 Foundation Week: "I Can Learn Math"',
            'theme': 'Building Basic Confidence with Common Core',
            'color': '#28a745',
            'activities': [
                {
                    'name': 'Growth Mindset Assessment',
                    'description': 'Assess your current math mindset and set growth goals',
                    'type': 'assessment',
                    'cc_focus': 'Mathematical Practices'
                },
                {
                    'name': 'Common Core Diagnostic',
                    'description': 'Identify your current skill level in key areas',
                    'type': 'diagnostic',
                    'cc_focus': 'Grade-level Standards'
                },
                {
                    'name': 'Foundational Skills Practice',
                    'description': 'Master basic operations and number sense',
                    'type': 'practice',
                    'cc_focus': 'Number Systems & Operations'
                },
                {
                    'name': 'Math Vocabulary Builder',
                    'description': 'Learn key mathematical terms and concepts',
                    'type': 'vocabulary',
                    'cc_focus': 'Mathematical Language'
                },
                {
                    'name': 'Success Tracker Setup',
                    'description': 'Create your personal learning goals and milestones',
                    'type': 'planning',
                    'cc_focus': 'Goal Setting'
                }
            ]
        },
        2: {  # Connection Week
            'title': '🔗 Connection Week: "Math is Everywhere"',
            'theme': 'Connecting Common Core to Real Life',
            'color': '#17a2b8',
            'activities': [
                {
                    'name': 'Real-World Ratios & Proportions',
                    'description': 'Apply proportional reasoning to everyday situations',
                    'type': 'application',
                    'cc_focus': 'Ratios & Proportional Relationships'
                },
                {
                    'name': 'Algebraic Thinking in Context',
                    'description': 'Use variables and expressions to model real situations',
                    'type': 'modeling',
                    'cc_focus': 'Expressions & Equations'
                },
                {
                    'name': 'Statistical Analysis Project',
                    'description': 'Collect and analyze data from your daily life',
                    'type': 'project',
                    'cc_focus': 'Statistics & Probability'
                },
                {
                    'name': 'Geometric Reasoning Challenge',
                    'description': 'Apply geometric concepts to solve practical problems',
                    'type': 'challenge',
                    'cc_focus': 'Geometry'
                },
                {
                    'name': 'Mathematical Communication',
                    'description': 'Explain your mathematical thinking clearly',
                    'type': 'communication',
                    'cc_focus': 'Mathematical Practices'
                }
            ]
        },
        3: {  # Application Week
            'title': '🚀 Application Week: "I Can Use Math"',
            'theme': 'Applying Common Core Skills Confidently',
            'color': '#ffc107',
            'activities': [
                {
                    'name': 'Multi-Step Problem Solving',
                    'description': 'Tackle complex problems requiring multiple strategies',
                    'type': 'problem_solving',
                    'cc_focus': 'Mathematical Practices'
                },
                {
                    'name': 'Function Analysis Project',
                    'description': 'Explore linear and nonlinear relationships',
                    'type': 'analysis',
                    'cc_focus': 'Functions'
                },
                {
                    'name': 'Mathematical Modeling Task',
                    'description': 'Create mathematical models for real-world scenarios',
                    'type': 'modeling',
                    'cc_focus': 'Modeling'
                },
                {
                    'name': 'Peer Teaching Session',
                    'description': 'Teach a Common Core concept to another student',
                    'type': 'teaching',
                    'cc_focus': 'Mathematical Communication'
                },
                {
                    'name': 'Standards Mastery Check',
                    'description': 'Demonstrate mastery of key grade-level standards',
                    'type': 'assessment',
                    'cc_focus': 'Grade-level Standards'
                }
            ]
        },
        4: {  # Mastery Week
            'title': '👑 Mastery Week: "I Am a Mathematician"',
            'theme': 'Demonstrating Common Core Mastery',
            'color': '#6f42c1',
            'activities': [
                {
                    'name': 'Capstone Performance Task',
                    'description': 'Complete a comprehensive mathematical investigation',
                    'type': 'capstone',
                    'cc_focus': 'Integrated Standards'
                },
                {
                    'name': 'Mathematical Reasoning Portfolio',
                    'description': 'Showcase your mathematical thinking and growth',
                    'type': 'portfolio',
                    'cc_focus': 'Mathematical Practices'
                },
                {
                    'name': 'Standards Self-Assessment',
                    'description': 'Evaluate your mastery of Common Core standards',
                    'type': 'self_assessment',
                    'cc_focus': 'All Standards'
                },
                {
                    'name': 'Math Mentoring Project',
                    'description': 'Guide another student through challenging concepts',
                    'type': 'mentoring',
                    'cc_focus': 'Leadership & Communication'
                },
                {
                    'name': 'Future Learning Plan',
                    'description': 'Plan your next steps in mathematical learning',
                    'type': 'planning',
                    'cc_focus': 'Goal Setting'
                }
            ]
        }
    }
    
    week_data = activities_data[week_num]
    
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
            st.markdown(f"**Common Core Focus:** {activity['cc_focus']}")
            st.markdown(f"**Type:** {activity['type'].title()}")
            st.markdown(f"**Description:** {activity['description']}")
            
            # Activity-specific content
            if activity['type'] == 'practice':
                render_cc_practice_problems(week_num, activity['cc_focus'])
            
            elif activity['type'] == 'assessment' or activity['type'] == 'diagnostic':
                render_assessment_activity(week_num, activity['name'])
            
            elif activity['type'] == 'project' or activity['type'] == 'capstone':
                render_project_activity(week_num, activity['name'])
            
            elif activity['type'] == 'reflection' or activity['type'] == 'self_assessment':
                render_reflection_activity(activity_key, activity['name'])
            
            # Mark as complete button
            if not is_completed:
                if st.button(f"Mark '{activity['name']}' as Complete", key=f"{activity_key}_complete"):
                    mark_activity_complete(week_num, activity['name'])
                    st.success(f"Great job completing '{activity['name']}'! 🎉")
                    st.rerun()
    
    # Weekly Standards Mastery Check
    render_standards_mastery_check(week_num)

def render_assessment_activity(week_num, activity_name):
    st.markdown("### 📊 Assessment Questions")
    
    if "Growth Mindset" in activity_name:
        questions = [
            "I believe I can improve my math skills with effort and practice.",
            "When I make mistakes in math, I learn from them.",
            "I enjoy challenging math problems, even if they're difficult.",
            "I ask for help when I don't understand something in math.",
            "I believe that everyone can be good at math with the right support."
        ]
        
        total_score = 0
        for i, question in enumerate(questions):
            score = st.slider(f"{question}", 1, 5, 3, key=f"mindset_{week_num}_{i}")
            total_score += score
        
        mindset_level = "Growth Oriented" if total_score >= 20 else "Developing Growth Mindset" if total_score >= 15 else "Fixed Mindset Tendencies"
        st.markdown(f"**Your Mindset Level:** {mindset_level}")
        
    elif "Diagnostic" in activity_name:
        grade = get_grade_level(st.session_state.challenge_level)
        st.markdown(f"**Grade {grade} Common Core Diagnostic**")
        
        # Sample diagnostic questions based on grade level
        if grade == 6:
            st.markdown("**Ratios & Proportions:** In a bag of 20 marbles, 8 are red. What fraction are red?")
            diag_answer1 = st.text_input("Answer:", key="diag_1")
            
            st.markdown("**Expressions:** Write an expression for 'twice a number plus 7'")
            diag_answer2 = st.text_input("Answer:", key="diag_2")
            
        elif grade == 7:
            st.markdown("**Proportional Relationships:** If y = 3x, is this proportional? Why?")
            diag_answer1 = st.text_area("Answer:", key="diag_1")
            
            st.markdown("**Integer Operations:** Calculate: (-8) + (+15)")
            diag_answer2 = st.text_input("Answer:", key="diag_2")

def render_project_activity(week_num, activity_name):
    st.markdown("### 🎯 Project Guidelines")
    
    if "Statistical Analysis" in activity_name:
        st.markdown("""
        **Project Requirements:**
        1. Choose a topic that interests you (sports, social media, weather, etc.)
        2. Collect at least 20 data points
        3. Create appropriate graphs (bar chart, line graph, histogram)
        4. Calculate measures of center (mean, median, mode)
        5. Write conclusions based on your data
        """)
        
        project_file = st.file_uploader("Upload your project", type=['pdf', 'docx', 'pptx'], key=f"project_{week_num}")
        
    elif "Capstone" in activity_name:
        st.markdown("""
        **Capstone Performance Task:**
        Choose one of these real-world problems to solve:
        
        1. **School Budget Analysis:** Analyze your school's budget and propose improvements
        2. **Environmental Impact Study:** Use math to study local environmental issues
        3. **Business Plan:** Create a mathematical model for a student business
        4. **Community Health Survey:** Design and analyze a health survey for your community
        """)
        
        selected_task = st.selectbox("Choose your capstone task:", 
                                   ["School Budget", "Environmental Study", "Business Plan", "Health Survey"],
                                   key=f"capstone_{week_num}")
        
        # Provide specific guidance based on selection
        if selected_task == "School Budget":
            st.markdown("""
            **Mathematical Skills to Use:**
            - Percentages and ratios
            - Data analysis and graphing
            - Linear equations for budget projections
            - Statistical analysis of spending patterns
            """)

def render_reflection_activity(activity_key, activity_name):
    reflection_prompts = {
        "Growth Mindset Assessment": "How has your attitude toward math changed this week?",
        "Math Anxiety Assessment": "What specific math topics make you feel anxious, and why?",
        "Personal Math Story": "Describe your relationship with math from elementary school to now.",
        "Connection Reflection": "What new connections between math and real life did you discover?",
        "Standards Self-Assessment": "Which Common Core standards do you feel most/least confident about?"
    }
    
    prompt = reflection_prompts.get(activity_name, "Reflect on your learning this week.")
    
    reflection = st.text_area(
        f"**Reflection Prompt:** {prompt}",
        value=st.session_state.daily_reflections.get(activity_key, ""),
        key=f"{activity_key}_reflection",
        placeholder="Share your thoughts and insights...",
        height=150
    )
    
    if
