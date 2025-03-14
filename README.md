# YouTube Summarizer 🎥📝
A mini NLP project that extracts and summarizes YouTube video subtitles using Natural Language Processing (NLP).
Supports two summarization methods: TF-IDF (statistical) and BART (deep learning-based).

🔹 Features

✅ Extracts subtitles from YouTube videos using YouTube Transcript API.

✅ Supports two summarization techniques:
TF-IDF (TextRank-based)
BART (Transformer-based)

✅ User-friendly Streamlit web interface.

✅ Lightweight & efficient NLP processing.

🛠 Installation

1️⃣ Clone the Repository

git clone https://github.com/Sankethakumbar/Youtube_Summarizer.git

cd youtube-summarizer

2️⃣ Create & Activate Virtual Environment

# On Windows

python -m venv venv
venv\Scripts\activate

# On macOS/Linux

python3 -m venv venv

source venv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

🚀 How to Run
1️⃣ Command-Line Interface (CLI)

Run the summarization script using:

python main.py

🔹 It will prompt for a YouTube video URL and summarization method (TF-IDF or BART).

2️⃣ Streamlit Web Interface

To launch the Streamlit-based web app:

streamlit run app.py

🔹 Open the link displayed in the terminal (e.g., http://localhost:8501)

🔧 Requirements
Python 3.7+
pytube (for video processing)
nltk (for NLP preprocessing)
transformers (for BART model)
streamlit (for web interface)
