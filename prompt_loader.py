def load_prompt(template_path: str, description: str) -> str:
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    return template.replace("{description}", description)
