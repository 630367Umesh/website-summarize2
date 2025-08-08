import streamlit as st
from website_summarizer import summarize
from datetime import datetime

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(page_title="Website Summarizer", layout="wide", page_icon="🌐")

# ---------------------- CUSTOM STYLES ----------------------
st.markdown("""
<style>
    .main {
        background-color: #f9fafb;
    }
    .title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .summary-box {
        padding: 1.2rem;
        border-radius: 8px;
        font-size: 1rem;
        line-height: 1.6;
        background-color: transparent; /* Removed white */
        box-shadow: none; /* Removed shadow */
    }
    .stTextInput > div > div > input {
        border-radius: 8px;
    }
    .stButton button {
        border-radius: 8px;
        background-color: #2563eb;
        color: white;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #1e40af;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------- APP TITLE ----------------------
st.markdown("<div class='title'>🌐 Website Summarizer with GROQ AI</div>", unsafe_allow_html=True)

# ---------------------- SIDEBAR ----------------------
st.sidebar.header("📜 Summary History")
if "history" not in st.session_state:
    st.session_state.history = []

if st.session_state.history:
    for item in reversed(st.session_state.history):
        st.sidebar.markdown(f"**{item['time']}** — [{item['url']}]({item['url']})")

# ---------------------- INPUT ----------------------
url_input = st.text_input("🔗 Enter a website URL to summarize:", placeholder="https://example.com")

# ---------------------- ACTION ----------------------
if st.button("🚀 Summarize Website"):
    if url_input.strip():
        with st.spinner("🔍 Fetching and summarizing website content..."):
            try:
                summary = summarize(url_input)
                # Save to history
                st.session_state.history.append({"url": url_input, "summary": summary, "time": datetime.now().strftime("%H:%M:%S")})

                # Display summary without white background
                st.markdown("### 📄 Summary")
                st.markdown(f"<div class='summary-box'>{summary}</div>", unsafe_allow_html=True)

                # Download button
                st.download_button(
                    label="💾 Download Summary (.md)",
                    data=summary,
                    file_name="website_summary.md",
                    mime="text/markdown"
                )

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter a valid URL before summarizing.")

# ---------------------- FOOTER ----------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: gray;'>Built with ❤️ using Groq AI & Streamlit</p>",
    unsafe_allow_html=True
)
