import sys
sys.path.insert(0, './local_lib')

from path import Path

def main():
    # Créer un dossier et un fichier, puis écrire dans le fichier
    folder = Path("my_folder")
    folder.mkdir_p()
    
    file = folder / "my_file.txt"
    file.write_text("Ceci est un test.")
    
    # Lire et afficher le contenu du fichier
    content = file.read_text()
    print(f"Contenu du fichier : {content}")

if __name__ == "__main__":
    main()
