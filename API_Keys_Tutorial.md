# API Keys Tutorial for Deep Learning & AI
*Prepared for your hackathon - February 2026*

---

## What Are API Keys?

API keys are **unique identifiers** that authenticate your requests to external services. Think of them as passwords that let you access powerful AI models and cloud computing resources without owning the hardware.

---

## What Can You Use API Keys For?

### 1. **Large Language Models (LLMs)**
| Service | What It Offers | Best For |
|---------|---------------|----------|
| **OpenAI** | GPT-4, GPT-4o, DALL-E, Whisper | Text generation, chatbots, image generation, speech-to-text |
| **Anthropic** | Claude 3.5/4 | Long-context tasks, coding, analysis |
| **Google AI** | Gemini Pro/Ultra | Multimodal (text + images), large context |
| **Mistral AI** | Mistral, Mixtral | Open-weight models, European alternative |
| **Cohere** | Command, Embed | Enterprise NLP, embeddings |

### 2. **Cloud GPU Services**
| Service | What It Offers | Pricing |
|---------|---------------|---------|
| **Google Colab Pro** | Free/paid GPU notebooks | Free tier available |
| **Lambda Labs** | A100, H100 GPUs | ~$1-2/hr |
| **RunPod** | On-demand GPUs | ~$0.20-2/hr |
| **Vast.ai** | Community GPUs | Very cheap |
| **Modal** | Serverless GPU | Pay per second |

### 3. **Specialized AI APIs**
| Service | Use Case |
|---------|----------|
| **Hugging Face** | Model hosting, inference endpoints |
| **Replicate** | Run open-source models via API |
| **Stability AI** | Image generation (Stable Diffusion) |
| **ElevenLabs** | Voice cloning, text-to-speech |
| **Pinecone/Weaviate** | Vector databases for RAG |

---

## Security Best Practices

### ❌ NEVER Do This
```python
# BAD - Never hardcode API keys!
api_key = "sk-abc123456789"
```

### ✅ Always Do This

#### Option 1: Environment Variables (Recommended)
```python
import os
api_key = os.environ.get("OPENAI_API_KEY")
```

#### Option 2: `.env` File with python-dotenv
```bash
# .env file (add to .gitignore!)
OPENAI_API_KEY=sk-your-key-here
ANTHROPIC_API_KEY=sk-ant-your-key
```

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

#### Option 3: Config file (gitignored)
```python
# config.py (add to .gitignore!)
OPENAI_API_KEY = "sk-..."
```

---

## Quick Start Examples

### Setup (Run Once)
```bash
pip install openai anthropic google-generativeai python-dotenv requests
```

---

### Example 1: OpenAI (GPT-4)

**Get your key:** https://platform.openai.com/api-keys

```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain transformers in 2 sentences."}
    ],
    max_tokens=150
)

print(response.choices[0].message.content)
```

---

### Example 2: Anthropic (Claude)

**Get your key:** https://console.anthropic.com/settings/keys

```python
import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Write a Python function to calculate fibonacci numbers."}
    ]
)

print(message.content[0].text)
```

---

### Example 3: Google Gemini

**Get your key:** https://aistudio.google.com/app/apikey

```python
import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-pro')
response = model.generate_content("What is machine learning?")

print(response.text)
```

---

### Example 4: Hugging Face Inference API

**Get your key:** https://huggingface.co/settings/tokens

```python
import requests
import os

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-3B-Instruct"
headers = {"Authorization": f"Bearer {os.environ.get('HF_TOKEN')}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({"inputs": "What is the capital of France?"})
print(output)
```

---

### Example 5: Image Generation with Replicate

**Get your key:** https://replicate.com/account/api-tokens

```python
import replicate
import os

os.environ["REPLICATE_API_TOKEN"] = os.environ.get("REPLICATE_API_TOKEN")

output = replicate.run(
    "stability-ai/sdxl:latest",
    input={"prompt": "A futuristic city at sunset, cyberpunk style"}
)

print(output)  # Returns image URL
```

---

## Setting Environment Variables

### Windows (PowerShell) - Temporary
```powershell
$env:OPENAI_API_KEY = "sk-your-key-here"
$env:ANTHROPIC_API_KEY = "sk-ant-your-key"
```

### Windows (PowerShell) - Permanent
```powershell
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sk-your-key", "User")
```

### Using .env file (Recommended for Projects)
1. Create a `.env` file in your project root
2. Add your keys:
```
OPENAI_API_KEY=sk-your-key-here
ANTHROPIC_API_KEY=sk-ant-your-key
GOOGLE_API_KEY=your-google-key
HF_TOKEN=hf_your-token
```
3. Add `.env` to your `.gitignore`:
```
.env
*.env
```

---

## Hackathon Tips

### 1. **Cost Management**
- Set billing limits on all platforms
- Use smaller models during development (gpt-4o-mini instead of gpt-4o)
- Cache responses when possible

### 2. **Rate Limits**
Most APIs have rate limits. Handle them gracefully:
```python
import time
from openai import RateLimitError

def call_with_retry(func, max_retries=3):
    for i in range(max_retries):
        try:
            return func()
        except RateLimitError:
            time.sleep(2 ** i)  # Exponential backoff
    raise Exception("Max retries exceeded")
```

### 3. **Free Tiers to Exploit**
| Service | Free Tier |
|---------|-----------|
| Google Gemini | 60 requests/min free |
| Hugging Face | Free inference (rate limited) |
| Cohere | 100 API calls/min free |
| Google Colab | Free GPU (limited) |
| Groq | Very fast, generous free tier |

### 4. **Quick Prototyping Stack**
```
Frontend: Streamlit or Gradio (1 hour to build UI)
Backend: FastAPI
LLM: OpenAI or Groq (fastest)
Vector DB: ChromaDB (local, free)
```

---

## Useful Links

| Resource | URL |
|----------|-----|
| OpenAI Docs | https://platform.openai.com/docs |
| Anthropic Docs | https://docs.anthropic.com |
| Google AI Docs | https://ai.google.dev/docs |
| Hugging Face | https://huggingface.co/docs |
| LangChain | https://python.langchain.com |
| Groq (fast inference) | https://console.groq.com |

---

## Template: .gitignore for AI Projects

```gitignore
# Environment
.env
*.env
.env.local

# API Keys
config.py
secrets.py

# Python
__pycache__/
*.pyc
.venv/
venv/

# Data
*.csv
*.json
data/

# Models
*.pt
*.pth
*.onnx
models/
```

---

Good luck at your hackathon! 🚀
