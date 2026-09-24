import sys
import yt_dlp

def main():
    print("=== YouTube Video Downloader ===")
    url = input("YouTube-URL eingeben: ").strip()
    if not url:
        print("Keine URL eingegeben.")
        return

    # Option: Ton erwünscht?
    sound_choice = input("Mit Ton herunterladen? (j/n, Standard: j): ").strip().lower()
    with_sound = sound_choice != 'n'

    ydl_opts_info = {
        'quiet': True,
        'no_warnings': True,
    }

    print("\nLade Video-Informationen...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        print(f"Fehler beim Abrufen der Video-Infos: {e}")
        return

    formats = info.get('formats', [])
    
    # Verfügbare Auflösungen filtern
    resolutions = set()
    for f in formats:
        if f.get('vcodec') != 'none' and f.get('height'):
            resolutions.add(f['height'])

    sorted_res = sorted(list(resolutions), reverse=True)

    if not sorted_res:
        print("Keine passenden Video-Auflösungen gefunden.")
        return

    print("\nVerfügbare Auflösungen:")
    for idx, res in enumerate(sorted_res, 1):
        print(f"[{idx}] {res}p")

    choice = input(f"Wähle eine Auflösung (1-{len(sorted_res)}, Standard: 1): ").strip()
    try:
        selected_index = int(choice) - 1 if choice else 0
        target_res = sorted_res[selected_index]
    except (ValueError, IndexError):
        target_res = sorted_res[0]

    print(f"\nGewählte Einstellung: {target_res}p | Ton: {'Ja' if with_sound else 'Nein'}")

    # Format-String für yt-dlp aufbauen
    if with_sound:
        # Beste Videospur bis zur Zielauflösung + beste Audiospur
        format_str = f"bestvideo[height<={target_res}]+bestaudio/best[height<={target_res}]"
    else:
        # Nur Video-Spur ohne Audio
        format_str = f"bestvideo[height<={target_res}]"

    download_opts = {
        'format': format_str,
        'outtmpl': '%(title)s (%(height)sp).%(ext)s',
        'merge_output_format': 'mp4' if with_sound else None,
    }

    print("Starte Download...")
    try:
        with yt_dlp.YoutubeDL(download_opts) as ydl:
            ydl.download([url])
        print("\nDownload erfolgreich abgeschlossen!")
    except Exception as e:
        print(f"Fehler beim Download: {e}")

if __name__ == "__main__":
    main()
