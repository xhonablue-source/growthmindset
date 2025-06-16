import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
st.set_page_config(page_title="MathCraft: Growth Mindset Tracker", layout="centered")

# --- Header ---
st.markdown("""
<div style='text-align: center;'>
    <h1 style='color:#4B0082;'>🧠 MathCraft: Growth Mindset Tracker</h1>
    <h3 style='color:#444;'>Your Beliefs About Learning Math Matter</h3>
    <p style='font-size: 0.9rem; color: #555;'>Built by <strong>Xavier Honablue, M.Ed</strong></p>
</div>
<hr style='border-top: 2px solid #ccc;' />
""", unsafe_allow_html=True)

# --- Survey Questions ---
st.subheader("📋 Student Growth Mindset Survey")
st.markdown("Rate each statement from 1 (Strongly Disagree) to 5 (Strongly Agree)")

questions = [
    "I believe that people can get better at math through practice.",
    "I believe that all people find learning math to be difficult at times.",
    "I believe that every student in this class can learn the math concepts that we will study this year.",
    "I believe that I can persevere in math."
]

responses = {}
for q in questions:
    responses[q] = st.slider(q, 1, 5, 3)

# --- Analyze Responses ---
if st.button("📊 Show Class Bar Graph"):
    df = pd.DataFrame({"Statement": list(responses.keys()), "Score": list(responses.values())})
    fig = px.bar(df, x="Score", y="Statement", orientation="h", title="Class Growth Mindset Profile", color="Score", range_x=[1, 5])
    st.plotly_chart(fig)

# --- Reflection ---
st.subheader("💬 Student Reflection Prompt")
st.markdown("Pick one idea from your survey that you'd like to improve or share.")
st.text_area("What does this statement mean to you, and how could it help you succeed in math this year?")

# --- Teacher Facilitation Option ---
st.markdown("""
<hr>
<h4>👩🏽‍🏫 Teacher Dashboard (Optional)</h4>
<ol>
  <li>Use the bar graph to highlight class-wide attitudes and open discussion on mindset.</li>
  <li>Create a poster summarizing students' strategies for persevering in math.</li>
  <li>Return to this tool monthly to track shifts in beliefs over time.</li>
</ol>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<hr>
<p style='text-align: center; font-size: 0.8rem; color: gray;'>
Built with ❤️ for classroom empowerment | <strong>Xavier Honablue, M.Ed</strong>
</p>
""", unsafe_allow_html=True)
