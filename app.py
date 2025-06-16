import streamlit as st

# Page config
st.set_page_config(page_title="MathCraft: Growth Mindset in Math", layout="wide")

# --- MATHCRAFT HEADER ---
st.markdown("""
<div style='text-align: center; padding: 1rem 0;'>
    <img src='https://raw.githubusercontent.com/xhonablue/mathcraft-assets/main/logo.png' width='150'>
    <h1 style='color: #4B0082;'>🧠 MathCraft</h1>
    <h3>Your Mind. Your Math. Your Power.</h3>
    <p style='font-size: 0.9rem; color: #555;'>Built by <strong>Xavier Honablue, M.Ed</strong></p>
    <hr style='border-top: 2px solid #ccc;'/>
</div>
""", unsafe_allow_html=True)

# --- SECTION: Introduction to Growth Mindset ---
st.header("🌱 Growth Mindset in Mathematics")
st.markdown("""
A **growth mindset** is the belief that abilities and intelligence can be developed through dedication and hard work.
In math, this means believing that everyone can improve their mathematical thinking with effort and the right strategies.

> "I’m not good at math… YET." 

Use that word — **YET** — to remind yourself that math is a journey.
"""
)

# --- SECTION: Productive Disposition ---
st.subheader("💡 What is Productive Disposition?")
st.markdown("""
According to the National Research Council's *Adding It Up*, productive disposition means:
> "The habitual inclination to see mathematics as sensible, useful, and worthwhile, coupled with a belief in diligence and one’s own efficacy."

In this app, you’ll explore ways to connect math to the real world, boost your confidence, and understand why math matters.
""")

# --- SECTION: Real-World Application Activity ---
st.subheader("🌍 Connect Math to the Real World")
st.markdown("""
Pick one of these real-world math challenges to try:
- Plan a budget for a music event
- Calculate how many gallons of paint to cover your dream bedroom
- Use ratios to design your own smoothie recipe

These activities help you **see value in math**, which strengthens your **productive disposition**.
""")

# --- SECTION: Reflect and Share ---
st.subheader("🧠 Reflect: How Do You Think About Math?")
st.text_input("What’s something hard in math you pushed through before? What helped you?")
st.text_input("Why do you think math is important in the world?")

# --- SECTION: Enrichment Links ---
st.subheader("🔗 Want to Learn More?")
st.markdown("""
Here are some awesome resources that help build a math growth mindset:
- [Youcubed – Growth Mindset in Math](https://www.youcubed.org/resource/what-is-a-math-mindset/)
- [Khan Academy – Growth Mindset Videos](https://www.khanacademy.org/resources/parents-mentors-1/helping-your-child/a/what-is-a-growth-mindset)
- [Classroom Posters & Tools from Mindset Works](https://www.mindsetworks.com/free-resources)
- [Big Ideas from Jo Boaler](https://www.youcubed.org/resource_category/teaching-ideas/)
""")

# --- FOOTER ---
st.markdown("""
<hr style='border-top: 1px solid #ccc;'>
<p style='font-size: 0.8rem; text-align: center;'>Built with ❤️ by Xavier Honablue, M.Ed | MathCraft Initiative | All rights reserved.</p>
""", unsafe_allow_html=True)
