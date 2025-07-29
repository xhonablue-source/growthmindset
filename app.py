import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --- Page Setup ---
st.set_page_config(page_title="MathCraft: Positive Mindset Math", page_icon="🌟", layout="wide")

# --- Developer Credit ---
col1, col2 = st.columns([1, 4])
with col1:
    try:
        st.image("njit_logo.png", width=80)
    except:
        st.markdown("🏫")
with col2:
    st.markdown("### www.cognitivecloud.ai")
    st.markdown("**Developed by Xavier Honablue M.Ed**")
    st.markdown("*For Middle & High School Students*")

# --- MathCraft Branding & Growth Mindset Block ---
st.markdown("""
<div style='text-align: center; padding: 1rem 0;'>
    <img src='https://raw.githubusercontent.com/xhonablue/mathcraft-assets/main/logo.png' width='150'>
    <h1 style='color: #4B0082;'>🧠 MathCraft</h1>
    <h3>Your Mind. Your Math. Your Power.</h3>
</div>
""", unsafe_allow_html=True)

st.markdown("""
### 🌱 Growth Mindset in Mathematics
A **growth mindset** means believing that abilities improve with effort and the right tools. In this app, you'll:
- Build confidence
- Connect math to your real life
- Prove that math is for **everyone**

> "I'm not good at math... **YET**."
""")

# --- Enrichment and Mindset Resource Links ---
st.markdown("""
### 🔗 Enrichment: Mindset & Real Math Resources
- [Youcubed – Growth Mindset](https://www.youcubed.org/resource/what-is-a-math-mindset/)
- [Khan Academy: Growth Mindset](https://www.khanacademy.org/youcanlearnanything)
- [Mindset Works Posters](https://www.mindsetworks.com/free-resources)
- [Angela Duckworth: Grit (TED Talk)](https://www.ted.com/talks/angela_lee_duckworth_grit_the_power_of_passion_and_perseverance)
- [Which One Doesn’t Belong?](https://wodb.ca/)
- [Equitable Math](https://equitablemath.org/)
- [Desmos Graphing Tool](https://www.desmos.com/calculator)
""")

# --- Introduction to Weekly Journey ---
st.markdown("""
---
## 📅 Begin Your 4-Week Math Confidence Journey
""")

# Append the full week_tabs content you’ve already pasted above here.
# Already contains: student profile setup, challenge levels, 4 themed weeks, quizzes, visuals, metrics, and score tracking.

# --- Footer ---
st.markdown("""
---
<p style='font-size: 0.8rem; text-align: center;'>
Built with ❤️ by Xavier Honablue, M.Ed | MathCraft Initiative | All rights reserved.
</p>
""", unsafe_allow_html=True)
