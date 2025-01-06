import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from ttkthemes import ThemedTk
import yt_dlp as ytdl
import json


# Speichern und Laden der Einstellungen
def save_settings(theme, download_path, ffmpeg_path):
    settings = {
        'theme': theme,
        'download_path': download_path,
        'ffmpeg_path': ffmpeg_path
    }
    with open('settings.json', 'w') as f:
        json.dump(settings, f)


def load_settings():
    if os.path.exists('settings.json'):
        with open('settings.json', 'r') as f:
            settings = json.load(f)
        return settings
    return {}


# Video herunterladen
def download_video(url, resolution, download_path, ffmpeg_path):
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'ffmpeg_location': ffmpeg_path,
        'noplaylist': True,
        'merge_output_format': 'mp4',  # Setze das Ausgabeformat auf mp4 (falls Video+Audio)
        'format': 'bestvideo+bestaudio',  # Lädt das beste Video und Audio herunter
        'format_sort': ['codec:avc1:m4a'],  # Bevorzuge Video mit avc1 und Audio mit m4a
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',  # Verwendet FFmpeg zum Zusammenführen von Video und Audio
            'preferedformat': 'mp4',  # Sicherstellen, dass die Ausgabe im MP4-Format erfolgt
        }],
    }

    with ytdl.YoutubeDL(ydl_opts) as ydl:
        # Abrufen der verfügbaren Formate
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])

        # Auswahl des besten Videoformats basierend auf der Auflösung
        selected_format = None
        for format in formats:
            if 'height' in format and format['height'] == int(resolution.replace('p', '')):
                selected_format = format
                break
        
        if selected_format:
            ydl_opts['format'] = f"{selected_format['format_id']}+bestaudio"  # Wählt das Video und das beste Audio
        else:
            ydl_opts['format'] = 'bestvideo+bestaudio/best'  # Fallback auf bestes Video und Audio

        # Download des Videos
        with ytdl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])




# GUI erstellen
class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")

        # Laden der Einstellungen
        self.settings = load_settings()
        self.theme = self.settings.get('theme', 'arc')  # Standardmäßig 'arc'
        self.download_path = self.settings.get('download_path', os.path.expanduser("~"))
        self.ffmpeg_path = self.settings.get('ffmpeg_path', '')

        # Setze das Thema
        self.root.set_theme(self.theme)

        # URL-Eingabe
        self.url_label = ttk.Label(root, text="YouTube URL:")
        self.url_label.grid(row=0, column=0, padx=10, pady=10)
        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        # Auflösungswahl
        self.resolution_label = ttk.Label(root, text="Auflösung:")
        self.resolution_label.grid(row=1, column=0, padx=10, pady=10)
        self.resolution_combobox = ttk.Combobox(root, values=["360p", "480p", "720p", "1080p"], state="readonly")
        self.resolution_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.resolution_combobox.set("720p")

        # Download-Pfad auswählen
        self.download_button = ttk.Button(root, text="Download Pfad auswählen", command=self.select_download_path)
        self.download_button.grid(row=2, column=0, padx=10, pady=10)

        # FFmpeg-Pfad auswählen
        self.ffmpeg_button = ttk.Button(root, text="FFmpeg Pfad auswählen", command=self.select_ffmpeg_path)
        self.ffmpeg_button.grid(row=2, column=1, padx=10, pady=10)

        # Download-Button
        self.download_button = ttk.Button(root, text="Herunterladen", command=self.on_download)
        self.download_button.grid(row=3, column=0, columnspan=2, pady=20)

        # Theme Toggle Button
        self.toggle_theme_button = ttk.Button(root, text="Dunkel/Hell-Modus wechseln", command=self.toggle_theme)
        self.toggle_theme_button.grid(row=4, column=0, columnspan=2, pady=10)

    def select_download_path(self):
        self.download_path = filedialog.askdirectory(initialdir=self.download_path)
        save_settings(self.theme, self.download_path, self.ffmpeg_path)

    def select_ffmpeg_path(self):
        self.ffmpeg_path = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe")])
        save_settings(self.theme, self.download_path, self.ffmpeg_path)

    def toggle_theme(self):
        new_theme = 'dark' if self.theme == 'arc' else 'arc'
        self.root.set_theme(new_theme)
        self.theme = new_theme
        save_settings(self.theme, self.download_path, self.ffmpeg_path)

    def on_download(self):
        url = self.url_entry.get()
        resolution = self.resolution_combobox.get()
        if not url:
            messagebox.showerror("Fehler", "Bitte geben Sie eine YouTube-URL ein.")
            return
        download_video(url, resolution, self.download_path, self.ffmpeg_path)
        messagebox.showinfo("Erfolg", "Der Download wurde gestartet!")


# Hauptfunktion zum Starten der App
def main():
    root = ThemedTk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
