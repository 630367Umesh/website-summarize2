import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from groq import Groq

# Load .env variables
load_dotenv()

# Get GROQ API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found in .env.")
else:
    print("✅ GROQ API key loaded successfully.")

# Initialize Groq client
groq = Groq(api_key=api_key)

# Max text to send (approx. 2000–2500 tokens)
MAX_CHARS = 10000

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}

# Clean and prepare website text
class Website:
    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')

        self.title = soup.title.string.strip() if soup.title else "No title found"

        for tag in soup.body(["script", "style", "img", "input"]):
            tag.decompose()

        # Truncate content to avoid exceeding token limits
        raw_text = soup.body.get_text(separator="\n", strip=True)
        self.text = raw_text[:MAX_CHARS]

# Prompt builder
def user_prompt_for(website):
    return (
        f"You are looking at a website titled: {website.title}.\n"
        "The contents of this website are as follows:\n\n"
        f"{website.text}\n\n"
        "Please provide a short summary in markdown. "
        "If it includes news or announcements, summarize them too."
    )

SYSTEM_PROMPT = (
    "You are an assistant that analyzes the contents of a website "
    "and provides a short summary, ignoring navigation-related text. "
    "Respond in markdown format."
)

def messages_for(website):
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt_for(website)}
    ]

# Summarizer entry
def summarize(url):
    website = Website(url)
    response = groq.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages_for(website)
    )
    return response.choices[0].message.content
