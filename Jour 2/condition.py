def main():  
# Tueur de fichier
    file_name = input("Entrez l'extension de fichier classifier (ex: .txt): ")
    file_name = file_name.lower()
    if file_name.endswith(".txt"):
        print("Dossier : textes")
    elif file_name.endswith(".jpg") or file_name.endswith(".png"):
        print("Dossier : images")
    elif file_name.endswith(".mp3"):
        print("Dossier : musiques")
    elif file_name.endswith(".pdf"):
        print("Dossier : documents")
    elif file_name.endswith(".py") or file_name.endswith(".js") or file_name.endswith(".java") or file_name.endswith(".c"):
        print("Dossier : scripts")
    else:
        print("Dossier : autres")
if __name__ == "__main__":
    main()