import sys
import os
import re
import settings

def render_template(template_file):
    if not template_file.endswith(".template"):
        raise Exception("File extension must be .template")
    
    # Vérifie si le fichier existe
    if not os.path.exists(template_file):
        raise Exception(f"File {template_file} does not exist.")
    
    # Lit le fichier template
    with open(template_file, "r") as f:
        content = f.read()

    # Remplace les valeurs par celles de settings.py
    content = re.sub(r"\{name\}", settings.name, content)

    # Écris dans un fichier .html
    output_file = template_file.replace(".template", ".html")
    with open(output_file, "w") as f:
        f.write(content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 render.py <template_file>")
        sys.exit(1)
    
    template_file = sys.argv[1]
    try:
        render_template(template_file)
    except Exception as e:
        print(e)
