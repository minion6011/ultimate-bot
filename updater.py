import os
import requests

# Imposta l'URL del repository GitHub e i file da aggiornare
github_repo_url = "https://github.com/minion6011/ultimate-bot"
files_to_update = [
    "requirements.txt",
    "main.py",
]

# Funzione per scaricare il contenuto di un file da GitHub
def download_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Funzione per aggiornare un file locale con il contenuto scaricato
def update_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"File '{filename}' aggiornato.")

# Funzione per eseguire l'autoupdater
def run_autoupdater():
    print("Avvio dell'autoupdater...")
    for filename in files_to_update:
        # Costruisci l'URL del file nel repository GitHub
        file_url = f"{github_repo_url}/raw/main/{filename}"
        print(f"Controllo aggiornamenti per '{filename}'...")
        
        # Scarica il contenuto del file dal repository GitHub
        file_content = download_file(file_url)
        if file_content is not None:
            # Aggiorna il file locale con il contenuto scaricato
            update_file(filename, file_content)
        else:
            print(f"Impossibile ottenere i dati per '{filename}'.")
    
    print("Autoupdater completato.")

# Esegui l'autoupdater
run_autoupdater()
