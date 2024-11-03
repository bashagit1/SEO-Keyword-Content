import streamlit as st
import os
from openai import OpenAI

# Set up OpenAI API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Title and Description
st.set_page_config(page_title="SEO Keyword & Content Idea Generator", page_icon="🔍")

# Title and Description with Icons
st.markdown("<h1 style='text-align: center;'>🔍 SEO Keyword & Content Idea Generator 🔍</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Generate SEO keywords and content ideas for your blog or website.</h4>", unsafe_allow_html=True)

# Sidebar for input options with icons
with st.sidebar:
    st.header("🛠️ Options")
    content_type = st.selectbox("📝 Select Content Type", ["Blog Post", "Article", "Product Description", "Social Media"])
    target_audience = st.text_input("👥 Enter Target Audience", placeholder="e.g., Small Business Owners")

# User Input for topic/theme
user_input = st.text_input("💬 Enter a topic for keyword generation", placeholder="e.g., Digital Marketing")

# Function to generate keywords and content ideas
def generate_ideas(content_type, user_input, target_audience):
    prompt_keywords = f"Generate SEO keywords for {content_type.lower()} about {user_input} targeting {target_audience}."
    prompt_content_ideas = f"Generate content ideas for {content_type.lower()} about {user_input} targeting {target_audience}."
    
    # Generate responses from OpenAI
    keywords_response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt_keywords}],
        model="gpt-3.5-turbo"
    )
    
    content_ideas_response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt_content_ideas}],
        model="gpt-3.5-turbo"
    )

    # Accessing the response text correctly
    keywords = keywords_response.choices[0].message.content
    content_ideas = content_ideas_response.choices[0].message.content
    
    return keywords, content_ideas

# Generate and Display Response
if st.button("🚀 Generate Ideas", key="generate"):
    if user_input and target_audience:
        keywords_response, content_ideas_response = generate_ideas(content_type, user_input, target_audience)
        
        st.subheader("🔑 Generated SEO Keywords")
        st.write(keywords_response)
        
        st.subheader("📝 Content Ideas")
        st.write(content_ideas_response)
    else:
        st.warning("⚠️ Please enter a topic and target audience to generate ideas.")

# Display User Instructions
st.info("""
### How to Use:
1. Enter a topic for keyword generation.
2. Specify your target audience.
3. Select the type of content you are creating.
4. Click 'Generate Ideas' to create keywords and content ideas!
""")
