YouTube Video Downloader 🎬

Ein einfaches Python-Befehlszeilen-Tool (CLI), mit dem du YouTube-Videos in gewünschter Auflösung mit oder ohne Ton direkt auf dein lokales Gerät herunterladen kannst.

🚀 Features

📊 Auflösung wählbar: Erkennt automatisch verfügbare Auflösungen (z. B. 1080p, 720p, 480p) und lässt dich auswählen.

🔊 Audio-Option: Option, das Video mit oder ohne Tonspur herunterzuladen.

⚡ Hohe Geschwindigkeit: Verwendet yt-dlp für die beste Performance.

🛠️ Voraussetzungen

Bevor du das Tool nutzt, stelle sicher, dass Folgendes auf deinem System installiert ist:

Python 3.7+: Python herunterladen

FFmpeg: Wird benötigt, um hochauflösende Video- und Audiospuren zusammenzufügen.

Windows: winget install FFmpeg oder via Chocolatey: choco install ffmpeg

macOS: Via Homebrew: brew install ffmpeg

Linux (Debian/Ubuntu): sudo apt update && sudo apt install ffmpeg

📦 Installation

Repository klonen:

git clone https://github.com/Gollum734/ytd.git
cd ytd


Abhängigkeiten installieren:

pip install yt-dlp


💻 Benutzung

Starte das Skript im Terminal:

python yt_downloader.py


Ablauf im Terminal:

Füge die YouTube-URL ein.

Wähle, ob das Video mit Ton (j) oder ohne Ton (n) gespeichert werden soll.

Wähle die gewünschte Auflösung aus der Liste der verfügbaren Optionen aus.

Das Video wird automatisch im aktuellen Ordner gespeichert.
