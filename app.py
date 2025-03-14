import streamlit as st
import whisper
from src.youtube_summary import summarize_youtube_video

# Set Streamlit Page Config
st.set_page_config(page_title="YouTube Video Summarizer", page_icon="🎬", layout="centered")

# Custom CSS for Styling
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .title {
            color: #e50914;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #444;
        }
        .summary-box {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            box-shadow: inset 2px 2px 5px rgba(0,0,0,0.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# UI Layout
st.markdown('<h1 class="title">YouTube Video Summarizer 🎥</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Enter a YouTube video URL and choose a summarization method to generate a quick summary.</p>', unsafe_allow_html=True)

# Input Field
video_url = st.text_input("🔗 Enter YouTube Video URL")

# Summarization Method Selection
method = st.radio("📝 Choose Summarization Method", ["TF-IDF", "BART"], horizontal=True)

# Summarize Button with Styling
if st.button("⚡ Summarize Now"):
    if video_url:
        with st.spinner("⏳ Summarizing... Please wait."):
            try:
                summary = summarize_youtube_video(video_url, method=method.lower())
                st.success("✅ Summary Generated Successfully!")
                st.markdown('<div class="summary-box">', unsafe_allow_html=True)
                st.write(summary)
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a valid YouTube URL.")

# Footer
st.markdown("<br><hr><p style='text-align:center;'>✨ Built by Data_pirates</p>", unsafe_allow_html=True)
