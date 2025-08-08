# 🧠 Website Summarizer using Groq & GPT

A Python-based tool that fetches, cleans, and summarizes the content of any website using the **Groq API** with the `llama3-70b-8192` model.  
It’s fast, markdown-friendly, and works both in **Jupyter Notebooks** and as a **Python script**.

---

## 🔍 Perfect For

- Quickly understanding long articles, news posts, or product pages
- Skimming lengthy text to extract main ideas
- Learning how to integrate **Groq LLMs** into Python projects
- Building your own summarization apps or browser tools

---

## 📦 Features

✅ Uses Groq’s blazing-fast **llama3-70b-8192** model  
✅ Fetches and cleans HTML content with **BeautifulSoup**  
✅ Skips navigation and ads for cleaner summaries  
✅ Generates **Markdown-formatted** summaries  
✅ Secure API key handling with **dotenv**  

---

## 📁 Project Structure

website-summarizer/
├── .env # Stores your GROQ_API_KEY (DO NOT commit)
├── requirements.txt # Python dependencies
├── streamlit_app.py # (Optional) Streamlit web UI
├── website_summarizer.py # Core summarization script
├── demo_summary.ipynb # Jupyter Notebook demo
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/website-summarizer.git
cd website-summarizer
2️⃣ Set up a Virtual Environment
Windows

powershell
Copy
Edit
python -m venv .venv
.venv\Scripts\activate
macOS/Linux

bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Create a .env File
Inside the project root:

ini
Copy
Edit
GROQ_API_KEY=your_actual_groq_api_key_here
5️⃣ Run in Jupyter Notebook
bash
Copy
Edit
jupyter notebook
Open demo_summary.ipynb and run the cells.

6️⃣ Run as Python Script
bash
Copy
Edit
python website_summarizer.py
7️⃣ (Optional) Run Streamlit App
bash
Copy
Edit
streamlit run streamlit_app.py
🧠 Example Usage
python
Copy
Edit
from website_summarizer import summarize

url = "https://example.com/some-article"
summary = summarize(url)
print(summary)
Example Output

markdown
Copy
Edit
## Summary
- The article discusses the latest advancements in AI.
- Key focus on LLMs and Groq's role in speeding up inference.
- Mentions upcoming industry events and trends.
⚙️ Requirements
Python 3.9+

Groq API Key → Get one here

📦 Dependencies
Install all dependencies with:

bash
Copy
Edit
pip install -r requirements.txt
requirements.txt

nginx
Copy
Edit
groq
python-dotenv
requests
beautifulsoup4
ipython
jupyter
streamlit
📌 Notes
Your .env file must not be pushed to GitHub (add it to .gitignore)

Summaries are generated using the llama3-70b-8192 model by default

HTML cleaning removes scripts, styles, images, and inputs

📄 License
MIT License

yaml
Copy
Edit

---

If you want, I can also **add a ready-made Streamlit UI** to this project so you can summarize websites from a browser instead of Jupyter or CLI. That would make this README’s “Run Streamlit App” section instantly usable.







