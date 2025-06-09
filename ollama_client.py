import subprocess
import sys

class OllamaClient:
    def __init__(self, model_name="llama2:7b"):
        self.model_name = model_name

    def is_installed(self):
        try:
            subprocess.run(['ollama', '--version'], check=True, capture_output=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    def install(self):
        print("Ollama is not installed.")
        if sys.platform == 'darwin':
            print("Attempting automatic install via Homebrew...")
            subprocess.run(['brew', 'install', 'ollama'], check=True)
        else:
            print("Please install Ollama manually from https://ollama.com/download")

    def ensure_installed(self):
        if not self.is_installed():
            self.install()
        else:
            print(" Ollama is already installed.")

    def generate_test_cases(self, prompt: str) -> str:
        self.ensure_installed()

        try:
            result = subprocess.run(
                ['ollama', 'run', self.model_name],
                input=prompt,
                capture_output=True,
                text=True,
                encoding='utf-8',
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f" Error running Ollama: {e.stderr}")
            return ""
