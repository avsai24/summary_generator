# 🧠 Project Summary Generator (Powered by Gemini 1.5 Pro)

This tool automatically analyzes a fullstack codebase, identifies important source files, and generates a structured `project_summary.md` file with readable summaries of each file using **Google Gemini 1.5 Pro**.

---

## ✨ Features

- 🔍 **Scans frontend and backend code** across any project structure  
- 📂 **Filters only important files** (e.g., `.ts`, `.py`, `.proto`, etc.)  
- 🧠 **Generates concise summaries** of what each file does using Gemini LLM  
- 📄 **Outputs a Markdown document** with filename, full code, and summary  
- ⚙️ **Fully configurable** with clean file filters and limits (e.g., max JSON size)  
- ✅ Ideal for documentation, onboarding, architecture review, or audits

---

## 📁 Folder Structure Example

Your project might look like this:

```
genpod_UI/
├── genpod_ui/         # Frontend (Next.js)
└── genpod_backend/    # Backend (FastAPI, gRPC)
```

---

## 🧪 How It Works

1. You set your **Gemini API key** and your **project folder path**
2. The script:
   - Recursively scans files
   - Skips irrelevant ones (e.g., `node_modules`, `.venv`, test files)
   - Sends file content to Gemini
   - Writes a clean, Markdown summary with code + description
3. Final output is saved as:
   ```
   /document generator/project_summary.md
   ```

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install google-generativeai
```

### 2. Set up and run

Edit `main.py` and set your variables:

```python
GEMINI_API_KEY = "your-api-key"
PROJECT_PATH = "/path/to/genpod_UI"
OUTPUT_PATH = "/path/to/project_summary.md"
```

Then run:

```bash
python main.py
```

---

## ✅ Output Format

```md
## 📄 File: `src/app/layout.tsx`
_Type: Layout Component_

```tsx
// code here
```

**Summary:**  
Wraps all app pages in layout and auth providers, ensuring consistent context across routes.

---
```

---

## 🔐 Gemini API

This tool uses [Google's Gemini 1.5 Pro](https://ai.google.dev/) via the official SDK:

- Your API key is only used locally
- Prompts are short and structured for fast response
- Each summary is rate-limited for quota safety

---

## 🧠 Why Use This?

- ⚡️ Get a **high-level understanding of a codebase** in minutes
- 📚 Create clean **technical documentation automatically**
- 🤝 Improve **developer onboarding and knowledge sharing**
- 📊 Use in **AI agents or internal tooling pipelines**

---

## 📌 Roadmap

- [ ] Add section grouping (Frontend / Backend)
- [ ] Support architecture-level summary (cross-file reasoning)
- [ ] Gemini streaming or batch summarization
- [ ] Optional visual dependency maps

---

## 📬 License

MIT License  
Built with ❤️ by [avs.ai](https://github.com/avsai24)
