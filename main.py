import os
import time
import google.generativeai as genai

# === CONFIGURATION ===
GEMINI_API_KEY = "AIzaSyCPq7nCWR3fO3tFaZM1BXsYAnblRq9deAo"  
PROJECT_PATH = "/Users/venkatasaiancha/Documents/captenai/genpod_UI"
OUTPUT_PATH = "/Users/venkatasaiancha/Documents/captenai/document generator/project_summary.md"

ALLOWED_EXTENSIONS = {'.ts', '.tsx', '.js', '.jsx', '.py', '.html', '.css', '.yml', '.yaml', '.proto', '.json'}
EXCLUDED_EXTENSIONS = {'.md', '.log', '.lock', '.map', '.zip', '.png', '.jpg'}
EXCLUDED_FOLDERS = {
    'node_modules', '.git', '.vscode', 'dist', 'build',
    '__pycache__', '.next', '.venv', 'venv', 'site-packages'
}
MAX_JSON_LINES = 2000
MIN_LINES_REQUIRED = 5
SUMMARY_PROMPT = (
    "Summarize the functionality of this file in 3–5 sentences. "
    "This file is part of a fullstack AI web application with frontend and backend components."
)

# === SETUP GEMINI ===
def setup_gemini(api_key: str):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-pro")

# === FILE SCANNING LOGIC ===
def is_important_file(file_path: str) -> bool:
    _, ext = os.path.splitext(file_path)
    if ext in EXCLUDED_EXTENSIONS or ext not in ALLOWED_EXTENSIONS:
        return False
    if any(folder in file_path.split(os.sep) for folder in EXCLUDED_FOLDERS):
        return False
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if len(lines) < MIN_LINES_REQUIRED:
                return False
            if ext == '.json' and len(lines) > MAX_JSON_LINES:
                return False
            return True
    except Exception as e:
        print(f"⚠️ Skipping (read error): {file_path} - {e}")
        return False

def walk_project_files(base_path: str):
    important_files = []
    for root, dirs, files in os.walk(base_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_FOLDERS]
        for file in files:
            full_path = os.path.join(root, file)
            if is_important_file(full_path):
                important_files.append(full_path)
    return important_files

# === MAIN SUMMARIZATION LOGIC ===
def summarize_files(files, model, output_md_path):
    with open(output_md_path, 'w', encoding='utf-8') as out:
        out.write("# 📘 Project Summary\n\n")

        for file_path in files:
            rel_path = os.path.relpath(file_path, PROJECT_PATH)
            print(f"✨ Summarizing: {rel_path}")

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    code = f.read()
                
                response = model.generate_content(f"{SUMMARY_PROMPT}\n\n```{code}```")
                summary = response.text.strip()

                out.write(f"## 📄 File: `{rel_path}`\n\n")
                out.write("```text\n")
                out.write(code[:5000])  # Limit code to 5000 chars
                out.write("\n```\n\n")
                out.write(f"**Summary:**\n{summary}\n\n---\n\n")

                time.sleep(1.5)  # Rate limiting

            except Exception as e:
                print(f"⚠️ Failed to summarize {rel_path}: {e}")

# === MAIN EXECUTION ===
if __name__ == "__main__":
    model = setup_gemini(GEMINI_API_KEY)
    files = walk_project_files(PROJECT_PATH)
    print(f"\n✅ Found {len(files)} important files.")

    summarize_files(files, model, OUTPUT_PATH)
    print(f"\n📄 Summary saved to: {OUTPUT_PATH}")