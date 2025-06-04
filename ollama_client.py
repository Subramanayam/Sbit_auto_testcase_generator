import subprocess
import json
import sys

def is_ollama_installed():
    try:
        subprocess.run(['ollama', '--version'], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_ollama():
    print("Ollama is not installed. Installing Ollama...")

    # For macOS, typically you'd install via Homebrew:
    if sys.platform == 'darwin':
        subprocess.run(['brew', 'install', 'ollama'], check=True)
    # For Linux or Windows, you might want to download installer manually
    else:
        print("Please install Ollama manually from https://ollama.com/download")

def ensure_ollama_installed():
    if not is_ollama_installed():
        install_ollama()
    else:
        print("Ollama is already installed.")

def generate_test_cases(prompt: str) -> str:
    ensure_ollama_installed()   # <- check and install before generating
    try:
        # Call ollama CLI, pass prompt via stdin
        process = subprocess.run(
            ['ollama', 'run', 'llama2:7b'],
            input=prompt,
            capture_output=True,
            text=True,
            encoding='utf-8',
            check=True
        )
        return process.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error calling Ollama: {e.stderr}")
        return ""
