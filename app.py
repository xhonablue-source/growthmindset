import streamlit as st
import random

# --- Page Configuration ---
st.set_page_config(
    page_title="Positive Mindset Math: 4th Grade Multiplication",
    page_icon="🌟",
    layout="wide", # Changed to wide for more space
    initial_sidebar_state="expanded" # Changed to expanded for navigation
)

# --- Custom CSS for Styling and Positive Vibe ---
st.markdown("""
<style>
    /* General Styling */
    body {
        font-family: 'Inter', sans-serif;
    }
    .main-header {
        text-align: center;
        color: #6A0572; /* Deep Purple */
        font-size: 3.2rem; /* Slightly larger */
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.15); /* More prominent shadow */
    }
    .sub-header {
        text-align: center;
        color: #4A4A4A;
        font-size: 1.2rem;
        margin-bottom: 2.5rem; /* More space */
    }

    /* Buttons */
    .stButton>button {
        background-color: #FF6F61; /* Coral */
        color: white;
        font-weight: bold;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 5px; /* Added margin for spacing */
    }
    .stButton>button:hover {
        background-color: #E65A5A; /* Darker Coral */
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    .stButton>button:active {
        transform: translateY(0);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* Input Fields */
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #FF6F61;
        padding: 10px;
        font-size: 1.1rem;
    }

    /* Feedback Messages */
    .stSuccess {
        background-color: #D4EDDA; /* Light Green */
        color: #155724; /* Dark Green */
        border-radius: 10px;
        padding: 15px;
        margin-top: 15px;
        font-weight: bold;
        border: 1px solid #C3E6CB;
    }
    .stError {
        background-color: #F8D7DA; /* Light Red */
        color: #721C24; /* Dark Red */
        border-radius: 10px;
        padding: 15px;
        margin-top: 15px;
        font-weight: bold;
        border: 1px solid #F5C6CB;
    }
    .stInfo {
        background-color: #CCE5FF; /* Light Blue */
        color: #004085; /* Dark Blue */
        border-radius: 10px;
        padding: 15px;
        margin-top: 15px;
        font-weight: bold;
        border: 1px solid #B8DAFF;
    }
    .stWarning {
        background-color: #FFF3CD; /* Light Yellow */
        color: #856404; /* Dark Yellow */
        border-radius: 10px;
        padding: 15px;
        margin-top: 15px;
        font-weight: bold;
        border: 1px solid #FFEBA3;
    }

    /* Explanations and Tips */
    .explanation-box {
        background-color: #F0F8FF; /* Alice Blue */
        border-left: 5px solid #6A0572;
        padding: 15px;
        margin-top: 20px;
        border-radius: 8px;
        font-size: 1rem; /* Slightly larger */
        line-height: 1.7;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .growth-mindset-tip {
        background-color: #FFF3CD; /* Light Yellow */
        color: #856404; /* Dark Yellow */
        border-radius: 10px;
        padding: 15px;
        margin-top: 20px;
        font-style: italic;
        text-align: center;
        border: 1px dashed #FFD700;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    /* Badges */
    .badge {
        display: inline-flex;
        align-items: center;
        background-color: #9B59B6; /* Amethyst */
        color: white;
        padding: 8px 15px;
        border-radius: 20px;
        margin: 5px;
        font-weight: bold;
        font-size: 0.9rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .badge-icon {
        font-size: 1.2rem;
        margin-right: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --- Common Core Standard Focus ---
COMMON_CORE_STANDARD = "CCSS.Math.Content.4.NBT.B.5: Multiply a whole number of up to four digits by a one-digit whole number, and multiply two two-digit numbers, using strategies based on place value and the properties of operations."

# --- Positive Mindset Messages ---
POSITIVE_MESSAGES = [
    "You've got this! Every try is a step forward. ✨",
    "Great effort! Learning is a journey, not a race. Keep going! 💪",
    "Mistakes are just opportunities to learn and grow. What can you learn from this? 🤔",
    "Your brain is getting stronger with every challenge you face! 🧠",
    "Don't give up! Persistence is the key to mastering anything. 🚀",
    "Awesome thinking! You're building powerful math skills. 🌟",
    "Celebrate your progress, no matter how small! You're doing great. 🎉",
    "Every problem you solve makes you smarter! Keep shining! 💡",
    "You're amazing! Believe in your ability to learn and grow. 🌱"
]

# --- Multiplication Strategies Explanations ---
STRATEGY_EXPLANATIONS = {
    "Area Model": """
    The **Area Model** helps visualize multiplication using rectangles.
    For example, to multiply $12 \\times 8$:
    Imagine a rectangle with length 12 and width 8.
    You can break 12 into $10 + 2$.
    Then you have two smaller rectangles: $10 \\times 8 = 80$ and $2 \\times 8 = 16$.
    Add the areas: $80 + 16 = 96$. So, $12 \\times 8 = 96$.
    This shows how place value helps us multiply!
    """,
    "Partial Products": """
    The **Partial Products** method involves breaking down numbers by place value and multiplying each part.
    For example, to multiply $23 \\times 4$:
    Multiply the tens: $20 \\times 4 = 80$
    Multiply the ones: $3 \\times 4 = 12$
    Add the partial products: $80 + 12 = 92$. So, $23 \\times 4 = 92$.
    This helps you see each step of the multiplication clearly!
    """,
    "Standard Algorithm": """
    The **Standard Algorithm** is the traditional way we multiply numbers, often taught in columns.
    For example, to multiply $34 \\times 5$:
    ```
      34
    x  5
    ----
    ```
    First, multiply the ones: $5 \\times 4 = 20$. Write down 0, carry over 2.
    ```
      2
      34
    x  5
    ----
       0
    ```
    Next, multiply the tens: $5 \\times 3 = 15$. Add the carried over 2: $15 + 2 = 17$. Write down 17.
    ```
      2
      34
    x  5
    ----
     170
    ```
    So, $34 \\times 5 = 170$. This method is efficient once you understand place value!
    """
}

# --- Session State Initialization ---
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.student_name = ""
    st.session_state.page = "welcome"
    st.session_state.num1 = 0
    st.session_state.num2 = 0
    st.session_state.correct_answer = 0
    st.session_state.attempts = 0
    st.session_state.streak = 0
    st.session_state.total_problems = 0
    st.session_state.total_correct = 0
    st.session_state.show_explanation = False
    st.session_state.current_strategy = random.choice(list(STRATEGY_EXPLANATIONS.keys()))
    st.session_state.difficulty = "2x1" # Default difficulty
    st.session_state.badges = []

# --- Functions ---
def generate_problem_by_difficulty(difficulty):
    """Generates a new multiplication problem based on selected difficulty."""
    if difficulty == "2x1": # Two-digit by one-digit
        num1 = random.randint(10, 99)
        num2 = random.randint(2, 9)
    elif difficulty == "3x1": # Three-digit by one-digit
        num1 = random.randint(100, 999)
        num2 = random.randint(2, 9)
    elif difficulty == "4x1": # Four-digit by one-digit
        num1 = random.randint(1000, 9999)
        num2 = random.randint(2, 9)
    elif difficulty == "2x2": # Two-digit by two-digit
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    else: # Default to 2x1 if invalid difficulty
        num1 = random.randint(10, 99)
        num2 = random.randint(2, 9)

    st.session_state.num1 = num1
    st.session_state.num2 = num2
    st.session_state.correct_answer = num1 * num2
    st.session_state.attempts = 0
    st.session_state.show_explanation = False
    st.session_state.current_strategy = random.choice(list(STRATEGY_EXPLANATIONS.keys()))
    st.session_state.total_problems += 1

def check_answer(user_answer):
    """Checks the user's answer and provides feedback."""
    if user_answer is None:
        st.warning("Please enter an answer before checking!")
        return

    st.session_state.attempts += 1
    if user_answer == st.session_state.correct_answer:
        st.success(f"🎉 Correct, {st.session_state.student_name}! {st.session_state.num1} × {st.session_state.num2} = {st.session_state.correct_answer}")
        st.session_state.streak += 1
        st.session_state.total_correct += 1
        st.markdown(f'<div class="growth-mindset-tip">{random.choice(POSITIVE_MESSAGES)}</div>', unsafe_allow_html=True)
        award_badge() # Check for badges
        st.button("Next Problem", on_click=lambda: generate_problem_by_difficulty(st.session_state.difficulty))
    else:
        st.error(f"Oops! That's not quite right, {st.session_state.student_name}. Try again! You have made {st.session_state.attempts} attempt(s).")
        st.session_state.streak = 0 # Reset streak on incorrect answer
        if st.session_state.attempts >= 2:
            st.info("Don't worry, every mistake helps you learn! Think about the strategy.")
            if st.button("Show Hint/Explanation"):
                st.session_state.show_explanation = True
        st.markdown(f'<div class="growth-mindset-tip">{random.choice(POSITIVE_MESSAGES)}</div>', unsafe_allow_html=True)

def award_badge():
    """Awards badges based on performance."""
    if st.session_state.streak >= 3 and "Streak Star" not in st.session_state.badges:
        st.session_state.badges.append("Streak Star ⭐")
        st.balloons()
        st.success(f"Congratulations, {st.session_state.student_name}! You earned the 'Streak Star' badge for 3 correct answers in a row! Keep up the great work!")
    if st.session_state.total_correct >= 5 and "Math Explorer" not in st.session_state.badges:
        st.session_state.badges.append("Math Explorer 🧭")
        st.balloons()
        st.success(f"Fantastic, {st.session_state.student_name}! You earned the 'Math Explorer' badge for solving 5 problems correctly! You're on your way!")
    if st.session_state.total_correct >= 10 and "Multiplication Master" not in st.session_state.badges:
        st.session_state.badges.append("Multiplication Master 🏆")
        st.balloons()
        st.success(f"Amazing, {st.session_state.student_name}! You earned the 'Multiplication Master' badge for solving 10 problems correctly! You're a math whiz!")

# --- Navigation ---
with st.sidebar:
    st.header("Navigation")
    if st.session_state.student_name:
        st.write(f"Welcome, {st.session_state.student_name}!")
    page_selection = st.radio(
        "Go to:",
        ["Practice Math", "My Progress & Badges", "Math Resources"],
        index=0 if st.session_state.page == "math_practice" else (1 if st.session_state.page == "progress" else 2)
    )
    if page_selection == "Practice Math":
        st.session_state.page = "math_practice"
    elif page_selection == "My Progress & Badges":
        st.session_state.page = "progress"
    elif page_selection == "Math Resources":
        st.session_state.page = "resources"

# --- Page Content ---
if st.session_state.page == "welcome":
    st.markdown('<h1 class="main-header">👋 Welcome to CognitiveCloud.ai Math!</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Let\'s embark on a fun math adventure together!</p>', unsafe_allow_html=True)
    st.write("Before we start, what's your name?")
    name_input = st.text_input("My name is:", key="name_input")
    if st.button("Start My Math Journey!"):
        if name_input:
            st.session_state.student_name = name_input
            st.session_state.page = "math_practice"
            generate_problem_by_difficulty(st.session_state.difficulty) # Generate first problem
            st.experimental_rerun() # Rerun to switch to math practice page
        else:
            st.warning("Please enter your name to start!")

elif st.session_state.page == "math_practice":
    st.markdown(f'<h1 class="main-header">🌟 Math Practice Time, {st.session_state.student_name}! 🌟</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Let\'s master 4th Grade Multiplication together!</p>', unsafe_allow_html=True)

    st.info(f"**Today's Focus:** {COMMON_CORE_STANDARD}")

    st.markdown("---")

    # Difficulty selection
    st.subheader("Choose Your Challenge Level:")
    col_diff1, col_diff2, col_diff3, col_diff4 = st.columns(4)
    with col_diff1:
        if st.button("2-digit x 1-digit", key="diff_2x1"):
            st.session_state.difficulty = "2x1"
            generate_problem_by_difficulty("2x1")
    with col_diff2:
        if st.button("3-digit x 1-digit", key="diff_3x1"):
            st.session_state.difficulty = "3x1"
            generate_problem_by_difficulty("3x1")
    with col_diff3:
        if st.button("4-digit x 1-digit", key="diff_4x1"):
            st.session_state.difficulty = "4x1"
            generate_problem_by_difficulty("4x1")
    with col_diff4:
        if st.button("2-digit x 2-digit", key="diff_2x2"):
            st.session_state.difficulty = "2x2"
            generate_problem_by_difficulty("2x2")

    st.markdown(f"<p style='text-align: center; margin-top: 15px; font-weight: bold;'>Current Challenge: <span style='color: #6A0572;'>{st.session_state.difficulty}</span></p>", unsafe_allow_html=True)

    st.markdown("---")

    st.write(f"## What is {st.session_state.num1} × {st.session_state.num2}?")

    user_input = st.number_input("Your Answer:", min_value=0, step=1, key="user_answer_input", format="%d")

    col_check, col_hint = st.columns(2)
    with col_check:
        if st.button("Check Answer"):
            check_answer(user_input)
    with col_hint:
        if st.session_state.attempts >= 1 and not st.session_state.show_explanation:
            if st.button("Show Hint/Explanation"):
                st.session_state.show_explanation = True
                st.experimental_rerun() # Rerun to display explanation immediately


    st.markdown(f"**Current Streak:** {st.session_state.streak} correct answers in a row! 🎉")

    if st.session_state.show_explanation:
        st.markdown(f"### Let's review the **{st.session_state.current_strategy}** strategy for this type of problem:")
        st.markdown(f'<div class="explanation-box">{STRATEGY_EXPLANATIONS[st.session_state.current_strategy]}</div>', unsafe_allow_html=True)
        st.markdown(f"Remember, the correct answer is: **{st.session_state.correct_answer}**")
        st.button("Try a New Problem", on_click=lambda: generate_problem_by_difficulty(st.session_state.difficulty))

    st.markdown("---")
    st.markdown(f'<div class="growth-mindset-tip">{random.choice(POSITIVE_MESSAGES)}</div>', unsafe_allow_html=True)


elif st.session_state.page == "progress":
    st.markdown(f'<h1 class="main-header">📈 Your Progress, {st.session_state.student_name}!</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">See how much you\'re learning and growing!</p>', unsafe_allow_html=True)

    st.subheader("Your Math Stats:")
    col_p1, col_p2, col_p3 = st.columns(3)
    with col_p1:
        st.metric("Total Problems Attempted", st.session_state.total_problems)
    with col_p2:
        st.metric("Total Correct Answers", st.session_state.total_correct)
    with col_p3:
        accuracy = (st.session_state.total_correct / st.session_state.total_problems * 100) if st.session_state.total_problems > 0 else 0
        st.metric("Accuracy", f"{accuracy:.1f}%")

    st.subheader("Your Badges:")
    if st.session_state.badges:
        badge_html = "<div style='display: flex; flex-wrap: wrap; justify-content: center; margin-top: 10px;'>"
        for badge in st.session_state.badges:
            badge_html += f"<div class='badge'><span class='badge-icon'>{badge.split(' ')[-1]}</span> {badge.rsplit(' ', 1)[0]}</div>"
        badge_html += "</div>"
        st.markdown(badge_html, unsafe_allow_html=True)
    else:
        st.info("No badges yet! Keep practicing to earn your first one! ✨")

    st.markdown("---")
    st.markdown(f'<div class="growth-mindset-tip">{random.choice(POSITIVE_MESSAGES)}</div>', unsafe_allow_html=True)


elif st.session_state.page == "resources":
    st.markdown(f'<h1 class="main-header">📚 Math & STEM Resources!</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-header">Hello {st.session_state.student_name}! Explore these amazing resources to take your learning even further!</p>', unsafe_allow_html=True)

    st.subheader("🚀 Local Engineering & STEM Youth Programs (Placeholder Links):")
    st.info("These are example links. Please search online for programs in your local area!")
    st.markdown("""
    * **Girls Who Code:** [Find a Club Near You](https://girlswhocode.com/programs/clubs) (Focuses on computer science, but great for STEM!)
    * **Boys & Girls Clubs of America - STEM Programs:** [Explore STEM](https://www.bgca.org/our-impact/programs/stem) (Many local clubs offer STEM activities)
    * **FIRST Robotics:** [Find a Team](https://www.firstinspires.org/team-and-event-search) (Robotics competitions for various age groups)
    * **YMCA STEM Programs:** [Search for Programs](https://www.ymca.net/what-we-do/youth-development/stem) (Many YMCAs offer local STEM camps and clubs)
    * **Local Universities/Colleges:** Check the outreach or K-12 programs sections of universities near you. They often have summer camps or weekend workshops in engineering, science, and math.
    * **Science Museums & Discovery Centers:** Many local science museums offer youth programs, workshops, and summer camps related to engineering and science.
    """)

    st.subheader("💡 General Online Math & Learning Resources:")
    st.markdown("""
    * **Khan Academy:** [Math by Grade Level](https://www.khanacademy.org/math/cc-fourth-grade-math) (Free lessons, practice exercises, and videos for all math topics)
    * **Prodigy Math Game:** [Play Prodigy](https://www.prodigygame.com/) (Engaging math game for grades 1-8)
    * **Cool Math Games:** [Play Now](https://www.coolmathgames.com/) (Fun math games for various ages)
    * **National Geographic Kids:** [Science & Innovation](https://kids.nationalgeographic.com/science-and-innovation/) (Explore science, technology, and engineering topics)
    """)

    st.markdown("---")
    st.markdown(f'<div style="text-align: center; margin-top: 2rem; color: #666;">Learning is an adventure, and you\'re doing great, {st.session_state.student_name}!</div>', unsafe_allow_html=True)

# --- Footer (always visible) ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 2rem; color: #666;">
    <p>💡 <strong>Empowering Young Minds in STEAM</strong></p>
    <p>Powered by CognitiveCloud.ai Education</p>
</div>
""", unsafe_allow_html=True)
