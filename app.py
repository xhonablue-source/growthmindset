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
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
            image_bytes = io.BytesIO(response.content)

            # Determine image format (optional, but good practice)
            if 'png' in url.lower():
                output_format = "PNG"
            elif 'jpg' in url.lower() or 'jpeg' in url.lower():
                output_format = "JPEG"
            else:
                output_format = "auto" # Let Streamlit try to infer

            st.image(image_bytes, use_column_width=True, output_format=output_format)
            st.markdown(f"<p style='text-align:center;font-weight:bold'>{name}</p>", unsafe_allow_html=True)
        except requests.exceptions.RequestException as e:
            st.warning(f"Could not load image for {name}. Error: {e}")
            # Fallback to a placeholder if image fails to load
            st.image("https://placehold.co/150x150/cccccc/000000?text=Image+Error", use_column_width=True)
            st.markdown(f"<p style='text-align:center;font-weight:bold'>{name}</p>", unsafe_allow_html=True)
        except Exception as e:
            st.warning(f"An unexpected error occurred while loading image for {name}: {e}")
            st.image("https://placehold.co/150x150/cccccc/000000?text=Image+Error", use_column_width=True)
            st.markdown(f"<p style='text-align:center;font-weight:bold'>{name}</p>", unsafe_allow_html=True)
