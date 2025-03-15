import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="My Portfolio", page_icon="📂", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #00ffcc, #0066ff);
            color: white;
            font-family: Arial, sans-serif;
        }
        .main {
            text-align: center;
        }
        .profile-pic {
            border-radius: 50%;
            width: 200px;
            height: 200px;
            border: 4px solid #00ffcc;
            box-shadow: 0px 0px 15px #00ffcc;
        }
        .header-text {
            font-size: 40px;
            font-weight: bold;
            margin-top: 10px;
            color: #00ffcc;
            text-shadow: 0px 0px 15px #00ffcc;
        }
        .sub-header {
            font-size: 22px;
            color: #bbbbbb;
        }
        .section-title {
            font-size: 28px;
            font-weight: bold;
            margin-top: 20px;
            border-bottom: 2px solid #00ffcc;
            padding-bottom: 5px;
            text-shadow: 0px 0px 10px #00ffcc;
        }
        .contact-box {
            border: 1px solid #00ffcc;
            padding: 10px;
            border-radius: 5px;
            margin-top: 20px;
            display: inline-block;
            background: rgba(0, 0, 0, 0.3);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.title("Syed Hassaan")
page = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Contact"])

# Load user profile picture
profile_pic = Image.open("C:/Users/abc/Desktop/my pic/img13.jpeg")

if page == "Home":
    st.image(profile_pic, caption="Syed Hassaan", width=200, use_column_width=False)
    st.markdown('<div class="header-text">Hello, I am Syed Hassaan</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Python Developer | AI Enthusiast | Web Scraper</div>', unsafe_allow_html=True)

elif page == "About":
    st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)
    st.write(
        """
        I am a passionate Python developer specializing in AI bots, chatbots, and web scraping.
        I have experience working on automation projects, and I enjoy solving complex problems.
        """
    )
    
elif page == "Projects":
    st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)
    projects = {
        "🔹 AI Chatbot": "Built an AI-powered chatbot for automating responses.",
        "🔹 Web Scraping Tool": "Developed a scraper to extract data from websites.",
        "🔹 Marketplace Bot": "Automated Facebook Marketplace ad posting."
    }
    for project, desc in projects.items():
        st.write(f"**{project}** - {desc}")
    
elif page == "Contact":
    st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)
    st.markdown('<div class="contact-box">📧 Email: syedhassaan255@gmail.com</div>', unsafe_allow_html=True)

# Footer
st.write("---")
st.write("Designed with ❤️ using Streamlit")
