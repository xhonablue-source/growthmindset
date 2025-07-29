import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="MathCraft: Growth Mindset Math", page_icon="🌱", layout="wide")

# --- HEADER: MathCraft Branding ---
st.markdown("""
<div style='text-align: center; padding: 1rem 0;'>
    <img src='https://raw.githubusercontent.com/xhonablue/mathcraft-assets/main/logo.png' width='150'>
    <h1 style='color: #4B0082;'>🧠 MathCraft</h1>
    <h3>Your Mind. Your Math. Your Power.</h3>
    <p style='font-size: 0.9rem; color: #555;'>Built by <strong>Xavier Honablue, M.Ed</strong></p>
    <hr style='border-top: 2px solid #ccc;'/>
</div>
""", unsafe_allow_html=True)

# --- INTRO SECTION: Growth Mindset ---
st.header("🌱 Growth Mindset in Mathematics")
st.markdown("""
A **growth mindset** is the belief that abilities and intelligence can be developed through dedication and hard work.
In math, this means believing that everyone can improve their mathematical thinking with effort and the right strategies.

> "I’m not good at math… YET." 

Use that word — **YET** — to remind yourself that math is a journey, not a competition.
""")

# --- Productive Disposition ---
st.subheader("💡 What is Productive Disposition?")
st.markdown("""
From *Adding It Up* by the National Research Council:

> "The habitual inclination to see mathematics as sensible, useful, and worthwhile, coupled with a belief in diligence and one’s own efficacy."

In this app, you’ll explore how real math connects to real life and why your effort is the key to success.
""")

# --- Real-World Reflection Activity ---
st.subheader("🌍 Connect Math to the Real World")
st.markdown("""
Pick a challenge below to see math's usefulness:
- 🧮 Plan a party budget with inequalities
- 🎨 Calculate paint needed for your dream room (volume + surface area)
- 🍓 Create your own smoothie recipe using ratios
""")
st.text_input("🔄 What's one real situation where math helped you?")
st.text_input("🧠 What’s a tough math topic you eventually learned? What helped?")

# --- LIVE RESOURCE LINKS ---
st.subheader("🔗 Learn More, Grow More")
st.markdown("""
- 🧠 [**Khan Academy: Growth Mindset**](https://www.khanacademy.org/youcanlearnanything)
- 📘 [**YouCubed: What is a Math Mindset?**](https://www.youcubed.org/resource/what-is-a-math-mindset/)
- 🧩 [**Which One Doesn’t Belong**](https://wodb.ca/)
- 🔥 [**Angela Duckworth: Grit (TED)**](https://www.ted.com/talks/angela_lee_duckworth_grit_the_power_of_passion_and_perseverance)
- 🧮 [**Desmos Graphing Calculator**](https://www.desmos.com/calculator)
- ⚖️ [**Equitable Math Tools**](https://equitablemath.org/)
- 🧪 [**Mindset Works Posters & Tools**](https://www.mindsetworks.com/free-resources)
""")

# --- CALL TO ADVENTURE ---
st.markdown("""---""")
st.title("📅 Start Your 4-Week Positive Math Mindset Journey")

# Include your full weekly curriculum here
# Copy the 4-week `week_tabs` block from your original Positive Mindset Math program here.
# It's over 400 lines — but nothing needs to change except possibly adding:
# - The enrichment links above at the top
# - Optionally: `st.selectbox()` to toggle between Growth Intro and Weekly Curriculum (if modular UI desired)

# --- Footer ---
st.markdown("""
<hr style='border-top: 1px solid #ccc;'>
<p style='font-size: 0.8rem; text-align: center;'>Built with ❤️ by Xavier Honablue, M.Ed | MathCraft Initiative | All rights reserved.</p>
""", unsafe_allow_html=True)
