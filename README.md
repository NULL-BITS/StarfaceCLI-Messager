# Starface CLI Messenger

Ein schlankes, sicheres CLI-Tool, um Nachrichten direkt über die Starface-Anlage zu senden – ohne Umwege über unsichere REST-Schnittstellen.

## 🚀 Features
* **XMPP-basiert:** Nutzt die native Kommunikationsschnittstelle der Starface für maximale Kompatibilität.
* **Sicher:** Keine Passwörter in der Befehlszeile oder Shell-History.
* **Leichtgewichtig:** Benötigt nur `slixmpp`.
* **Benutzerfreundlich:** Automatische Hilfe-Generierung via `--help`.

## 📋 Voraussetzungen
* Python 3.x
* Starface Anlage mit aktivierter XMPP-Schnittstelle (Port 5222).

## ⚙️ Installation

1. Repository klonen:
   ```bash
   git clone [https://github.com/DEIN-USERNAME/starface-cli.git](https://github.com/DEIN-USERNAME/starface-cli.git)
   cd starface-cli

Abhängigkeiten installieren:
   ```bash pip install -r requirements.txt```

🛠 Benutzung

   ```python starface_cli.py --host 192.168.188.20 -u 205 -t 13 -m "Hallo! Nachricht kommt per CLI."   ```

### Argumente

| Argument | Beschreibung |
| :--- | :--- |
| `--host` | IP-Adresse oder Hostname deiner Starface-Anlage |
| `-u`, `--user` | Deine Benutzer-ID / Nebenstellennummer |
| `-t`, `--to` | Ziel-Rufnummer des Empfängers |
| `-m`, `--msg` | Der zu sendende Nachrichtentext |



Nach dem Start des Skripts wirst du sicher nach deinem Passwort gefragt. Die Eingabe bleibt im Terminal unsichtbar.🔒 

Sicherheitshinweis
Dieses Skript speichert zu keiner Zeit Anmeldedaten. 
Die Passwort-Abfrage erfolgt interaktiv über getpass, um zu verhindern, dass Passwörter in Log-Dateien oder der Shell-Historie (~/.bash_history) landen.
