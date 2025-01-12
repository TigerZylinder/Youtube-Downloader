import os
import tkinter as tk
import yt_dlp as ytdl
import json
import subprocess
import customtkinter
import subprocess
import pyperclip
from tkinter import filedialog, messagebox
from PIL import Image

# Speichern und Laden der Einstellungen
def save_settings(download_path, ):
    command = f"cd .. && cd .. && cd set && python set.py -dldir \"{download_path}\""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(result.stdout)
    print(result.stderr)


def load_settings():
    # Get the current directory of the script
    current_dir = os.path.dirname(os.path.abspath(__file__))    
    # Create the path to the 'set' directory
    set_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'set'))   
    # Full path to the set.json file
    set_json_path = os.path.join(set_dir, 'set.json')  
    # Check if the set.json file exists in the 'set' directory
    if os.path.exists(set_json_path):
        with open(set_json_path, 'r') as f:
            settings = json.load(f)
        return settings
    return {}

def load_themes():
    # Get the current directory of the script
    current_dir = os.path.dirname(os.path.abspath(__file__))    
    # Create the path to the 'set' directory
    src_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'src'))   
    # Full path to the set.json file
    styles_json_path = os.path.join(src_dir, 'styles_en.json')  
    # Check if the set.json file exists in the 'set' directory
    if os.path.exists(styles_json_path):
        with open(styles_json_path, 'r') as f:
            settings = json.load(f)
        return settings
    return {}

# Video oder nur Audio herunterladen
def download_video(url, resolution, download_path, ffmpeg_path, audio_only=False , playlist=False):

    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'ffmpeg_location': ffmpeg_path,
        'noplaylist': playlist,
        'merge_output_format': 'mp3',  # Setze das Ausgabeformat auf mp4 (falls Video+Audio)
        'format': 'bestaudio',  # Lädt das beste Video und Audio herunter
        'format_sort': ['m4a'],  # Bevorzuge Video mit avc1 und Audio mit m4a
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',  # Verwendet FFmpeg zum Zusammenführen von Video und Audio
            'preferedformat': 'mp3',  # Sicherstellen, dass die Ausgabe im MP4-Format erfolgt
        }],
    }

    if not audio_only:
        
        ydl_opts = {
          'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
          'ffmpeg_location': ffmpeg_path,
          'noplaylist': playlist,
          'merge_output_format': 'mp4',  # Setze das Ausgabeformat auf mp4 (falls Video+Audio)
         'format': 'bestvideo+bestaudio',  # Lädt das beste Video und Audio herunter
         'format_sort': ['codec:avc1:m4a'],  # Bevorzuge Video mit avc1 und Audio mit m4a
         'postprocessors': [{
             'key': 'FFmpegVideoConvertor',  # Verwendet FFmpeg zum Zusammenführen von Video und Audio
             'preferedformat': 'mp4',  # Sicherstellen, dass die Ausgabe im MP4-Format erfolgt
         }],
     }

    with ytdl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# Video oder nur Audio herunterladen
def download_videos(urls_list, download_path, ffmpeg_path, audio_only=False, playlist=False):

    urls_list = urls_list.split(',')

    # Create separate variables for each URL dynamically
    for index, url in enumerate(urls_list, start=1):
        globals()[f'url{index}'] = url

    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'ffmpeg_location': ffmpeg_path,
        'noplaylist': playlist,
        'merge_output_format': 'mp3',  # Setze das Ausgabeformat auf mp4 (falls Video+Audio)
        'format': 'bestaudio',  # Lädt das beste Video und Audio herunter
        'format_sort': ['m4a'],  # Bevorzuge Video mit avc1 und Audio mit m4a
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',  # Verwendet FFmpeg zum Zusammenführen von Video und Audio
            'preferedformat': 'mp3',  # Sicherstellen, dass die Ausgabe im MP4-Format erfolgt
        }],
    }

    if not audio_only:
        
        ydl_opts = {
          'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
          'ffmpeg_location': ffmpeg_path,
          'noplaylist': playlist,
          'merge_output_format': 'mp4',  # Setze das Ausgabeformat auf mp4 (falls Video+Audio)
         'format': 'bestvideo+bestaudio',  # Lädt das beste Video und Audio herunter
         'format_sort': ['codec:avc1:m4a'],  # Bevorzuge Video mit avc1 und Audio mit m4a
         'postprocessors': [{
             'key': 'FFmpegVideoConvertor',  # Verwendet FFmpeg zum Zusammenführen von Video und Audio
             'preferedformat': 'mp4',  # Sicherstellen, dass die Ausgabe im MP4-Format erfolgt
         }],
     }
    # Videos herunterladen
    with ytdl.YoutubeDL(ydl_opts) as ydl:
        for index in range(1, len(urls_list) + 1):
            ydl.download([globals()[f'url{index}']])  # Download each URL dynamically
    

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.settings = load_settings()
        self.theme = self.settings.get('theme', os.path.expanduser("~"))
        self.color = self.settings.get('color', os.path.expanduser("~"))
        # Styling
        customtkinter.set_appearance_mode(self.theme)
        customtkinter.set_default_color_theme(self.color)
        
        # Normal Var:
        self.entry_count = 1  # Start bei 1

        # Get the current directory of the script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        src_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'src'))
        icons_dir = os.path.abspath(os.path.join(src_dir, 'icons'))


        self.copy_image = os.path.abspath(os.path.join(icons_dir ,'copy.png'))
        self.copy_image = Image.open(self.copy_image)
        self.copy_image = self.copy_image.resize((30, 30))
        self.copy_image = customtkinter.CTkImage(light_image=self.copy_image, dark_image=self.copy_image)

        self.goto_image = os.path.abspath(os.path.join(icons_dir ,'goto.png'))
        self.goto_image = Image.open(self.goto_image)
        self.goto_image = self.goto_image.resize((30, 30))
        self.goto_image = customtkinter.CTkImage(light_image=self.goto_image, dark_image=self.goto_image)

        self.settings_image = os.path.abspath(os.path.join(icons_dir ,'settings.png'))
        self.settings_image = Image.open(self.settings_image)
        self.settings_image = self.settings_image.resize((40, 40))
        self.settings_image = customtkinter.CTkImage(light_image=self.settings_image, dark_image=self.settings_image)

        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("600x280")  # Width x Height
        self.root.resizable(False, False)  # Disable resizing in both directions


        # Path to ffmpeg.exe
        self.ffmpeg_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'prog', 'ffmpeg.exe'))

        # Load settings
        self.download_path = self.settings.get('dldir', os.path.expanduser("~"))

        # URL entry
        self.yt_url_titel = customtkinter.CTkLabel(root, text="YouTube URL:")
        self.yt_url_titel.grid(row=0, column=0, padx=10, pady=10)
        self.url_entry = customtkinter.CTkEntry(root, width=400)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        # Resolution selection
        customtkinter.CTkLabel(root, text="Resolution:").grid(row=1, column=0, padx=10, pady=10)
        self.resolution_combobox = customtkinter.CTkComboBox(root, values=["360p", "480p", "720p", "1080p"])
        self.resolution_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.resolution_combobox.set("1080p")

        # Audio-only option
        self.audio_only_var = customtkinter.StringVar(value="False")
        self.audio_only_check = customtkinter.CTkCheckBox(
            root, text="Audio only (MP3)", variable=self.audio_only_var, onvalue="True", offvalue="False"
        )
        self.audio_only_check.place(x=200, y=108)

        # Playlist download option
        self.playlist_var = customtkinter.StringVar(value="False")
        self.playlist_check = customtkinter.CTkCheckBox(
            root, text="Download playlist", variable=self.playlist_var, onvalue="True", offvalue="False"
        )
        self.playlist_check.place(x=350, y=108)

        box = customtkinter.CTkFrame(root, border_width=1, border_color="grey", width=500, height=30)
        box.place(x=10,y=150)
        
        # Download path selection
        self.select_download_path_button = customtkinter.CTkButton(root, text="Select download path", command=self.select_download_path)
        self.select_download_path_button.place(x=20, y=106)
        self.download_path_txt = customtkinter.CTkLabel(box, text=self.download_path, wraplength=500, fg_color="transparent")
        self.download_path_txt.place(x=7, y=1)

        self.copy_dwl_path = customtkinter.CTkButton(root, image= self.copy_image, text="", width=30, height=30, command=self.copy_downl_path)
        self.copy_dwl_path.place(x=515,y=150)

        self.goto_dwl_path = customtkinter.CTkButton(root, image= self.goto_image, text="", width=30, height=30, command=self.open_downl_path)
        self.goto_dwl_path.place(x=558,y=150)

        # Download button
        self.download_btn = customtkinter.CTkButton(root, text="Download", command=self.on_download)
        self.download_btn.place(x=150,y=200)

        # Multi Download button
        self.download_multi_btn = customtkinter.CTkButton(root, text="Multi download", command=self.on_multi_download)
        self.download_multi_btn.place(x=300,y=200)

        # Settings button
        self.settings_btn = customtkinter.CTkButton(root, image= self.settings_image, text="", width=40, height=40, command=self.open_settings_window)
        self.settings_btn.place(x=555,y=5)

    def select_download_path(self):
        selected_path = filedialog.askdirectory(initialdir=self.download_path)
        if selected_path:
            self.download_path = selected_path
            self.download_path_txt.configure(text=self.download_path)
            save_settings(self.download_path)
    
    def open_downl_path(self):
        download_path = self.download_path
        print(download_path)
        os.startfile(f"{download_path}")

    def copy_downl_path(self):
        download_path = self.download_path
        pyperclip.copy(download_path)


    def on_download(self):
        url = self.url_entry.get()
        resolution = self.resolution_combobox.get()
        audio_only = self.audio_only_var.get() == "True"
        playlist = self.playlist_var.get() == "True"

        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL.")
            return

        download_video(url, resolution, self.download_path, self.ffmpeg_path, audio_only, playlist)

        if audio_only:
            messagebox.showinfo("Success", "The audio download (MP3) has been completed successfully!")
        else:
            messagebox.showinfo("Success", "The video download (MP4) has been successfully completed!")


    def on_multi_download(self):
        root=self.root

        root.geometry("1200x300")
        self.yt_url_titel.place(x=650,y=15)
        self.url_entry.place(x=750,y=50)
        self.yt_url_titel.configure(text="YouTube URLs:")
        self.download_multi_btn.destroy()
        self.download_single_btn = customtkinter.CTkButton(root, text="Single Download", command=self.on_single_download)
        self.download_single_btn.place(x=300,y=200)
        self.select_download_path_button.place(x=20, y=58)
        self.audio_only_check.place(x=200, y=60)
        self.playlist_check.place(x=350, y=60)
        self.add_btn = customtkinter.CTkButton(root, text="Add", command=self.addlink, width=50)
        self.add_btn.place(x=665,y=50)
        self.download_btn.configure(command=self.multi_download)

    def multi_download(self):
        std = self.url_entry.get()
        audio_only = self.audio_only_var.get() == "True"
        playlist = self.playlist_var.get() == "True"
        urls_string = ",".join([entry.get().strip() for entry in self.url_entries if entry.get().strip()]) + "," + std
        if not urls_string:
            print("No valid URLs entered.")
            return

        download_videos(urls_string, self.download_path, self.ffmpeg_path, audio_only, playlist)

    def addlink(self):
        root = self.root
        self.spacing = 40     # Abstand zwischen den Feldern
        self.start_y = 50     # Startposition für die Y-Koordinate
    
        # Initialize entry_count und url_entries, wenn nötig
        if not hasattr(self, 'entry_count'):
            self.entry_count = 1
        if not hasattr(self, 'url_entries'):
            self.url_entries = []  # Liste für alle URL-Eingabefelder

        if self.entry_count < 6:
            y_position = self.start_y + self.entry_count * self.spacing
            url_entry = customtkinter.CTkEntry(root, width=400)
            url_entry.place(x=750, y=y_position)   

            # URL-Eingabefeld zur Liste hinzufügen
            self.url_entries.append(url_entry)
            self.entry_count += 1

            if self.entry_count >= 2 and not hasattr(self, 'remove_link_btn'):
                self.remove_link_btn = customtkinter.CTkButton(root, text="Remove", command=self.removelink, width=50)
                self.remove_link_btn.place(x=665, y=85)


    def removelink(self):
        # Sicherstellen, dass entry_count nicht 1 ist
        if self.entry_count > 0:
            # Das zuletzt hinzugefügte Eingabefeld entfernen (aus der Liste)
            last_entry = self.url_entries.pop()
            last_entry.destroy()
            # Den Zähler für die Eingabefelder verringern
            self.entry_count -= 1
            # Den Entfernen-Button nach Bedarf wieder entfernen
            if self.entry_count < 2:
                self.remove_link_btn.destroy()
                del self.remove_link_btn
        else:
            print("There are no input fields to remove!")

    def on_single_download(self):
        self.download_single_btn.destroy()
        self.download_multi_btn = customtkinter.CTkButton(self.root, text="Multi download", command=self.on_multi_download)
        self.download_multi_btn.place(x=300,y=200)  
        self.root.geometry("600x280")  # Width x Height
        self.audio_only_check.place(x=200, y=108)
        self.playlist_check.place(x=350, y=108)
        while not self.entry_count < 2:
            last_entry = self.url_entries.pop()
            last_entry.destroy()
            # Den Zähler für die Eingabefelder verringern
            self.entry_count -= 1

            if hasattr(self, 'remove_link_btn'):
                self.remove_link_btn.destroy()
                del self.remove_link_btn

            if hasattr(self, 'add_btn'):
                self.add_btn.destroy()
                del self.add_btn

        self.select_download_path_button.place(x=20, y=106)
        self.yt_url_titel.configure(text="YouTube URL:")
        self.yt_url_titel.grid(row=0, column=0, padx=10, pady=10)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)
        self.download_btn.configure(command=self.on_download)

    def open_settings_window(self):
        # Einstellungen laden
        self.settings = load_settings()
        self.theme = self.settings.get('theme', 'dark')  # Default-Wert hinzufügen
        self.color = self.settings.get('color', os.path.expanduser("~"))
        print(self.color)
        # Dateinamen extrahieren
        basename_color = os.path.basename(self.color)  # Holt "Hades.json"
        print(basename_color)
        color_name = os.path.splitext(basename_color)[0]  # Entfernt die Erweiterung, gibt "Hades" zurück

        # Mappings
        color_mapping = {"dark-blue": "Darkblue", "NightTrain": "NightTrain", "Hades": "Hades", "MoonlitSky": "MoonlitSky","NeonBanana": "NeonBanana"}
        print(color_name)
        theme_mapping = {"dark": "Dark", "light": "Light"}
        
        # Überprüfen, ob der Wert vorhanden ist, sonst Standardwert setzen
        selected_theme = theme_mapping.get(self.theme, "N/A")
        selected_color = color_mapping.get(color_name, "N/A")

        print(f"Selected Theme: {selected_theme}")
        print(f"Selected Color: {selected_color}")

        ctk = customtkinter
        # Neues modales Fenster erstellen
        self.root_2 = ctk.CTkToplevel(self.root)
        self.root_2.title("Settings")
        self.root_2.geometry("400x300")
        self.root_2.attributes("-topmost", True)

        # Aussehen-Label
        ctk.CTkLabel(self.root_2, text="Appirience", width=100, height=40, font=("Arial", 20, "bold")).place(x=150, y=10)

        # Thema-Auswahl
        appearance_box = ctk.CTkFrame(self.root_2, border_width=1, border_color="grey", width=300, height=150)
        appearance_box.place(x=50, y=50)
        
        ctk.CTkLabel(appearance_box, text="Theme:").place(x=10, y=10)
        self.theme_combobox = ctk.CTkComboBox(
            appearance_box, 
            values=["Dark", "Light"], 
            command=self.change_theme  # Neue Funktion für Theme-Auswahl
        )
        self.theme_combobox.place(x=100, y=10)
        self.theme_combobox.set(selected_theme)

        ctk.CTkLabel(appearance_box, text="Color-Theme:").place(x=10, y=60)
        self.color_combobox = ctk.CTkComboBox(
            appearance_box, 
            values=["Darkblue", "NightTrain", "Hades", "MoonlitSky","NeonBanana"], 
            command=self.change_color  # Neue Funktion für Farb-Auswahl
        )
        self.color_combobox.place(x=100, y=60)
        self.color_combobox.set(selected_color)

    def change_theme(self, selected_theme):
        ctk = customtkinter
        # Mapping von Themen
        theme_mapping = {"Dark": "dark", "Light": "light"}
        selected_theme = theme_mapping.get(selected_theme)
    
        # Erscheinungsbild ändern
        ctk.set_appearance_mode(selected_theme)
    
        # Subprozess ausführen
        command = f"cd .. && cd .. && cd set && python set.py -theme \"{selected_theme}\""
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        print(result.stdout)
        print(result.stderr)

    def change_color(self, selected_color):
        self.styles = load_themes()
        # Mappings für Farbthemen
        color_mapping = self.styles
        
        color_file = color_mapping.get(selected_color)
        
        if color_file:
            # Wenn es eine JSON-Datei ist, Pfad korrekt anpassen
            if ".json" in color_file:
                current_dir = os.path.dirname(os.path.abspath(__file__))
                src_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'src'))
                styles_dir = os.path.abspath(os.path.join(src_dir, 'styles'))
                color_file = os.path.join(styles_dir, color_file)

                # Alle Backslashes in Doppelslashes für Windows-Dateipfade
                color_file = color_file.replace("\\", "\\\\")

            try:
                # Verwenden von subprocess, falls ein externer Prozess benötigt wird
                command = f"cd .. && cd .. && cd set && python set.py -color \"{color_file}\""
                result = subprocess.run(command, shell=True, text=True, capture_output=True)
                
                # Ausgabe von Subprozess-Fehlern und -Ergebnissen
                print(result.stdout)
                if result.stderr:
                    print(f"Fehler: {result.stderr}")
            except Exception as e:
                print(f"Error executing subprocess: {e}")
            
            # Setze das Farbthema in CustomTkinter
            customtkinter.set_default_color_theme(color_file)

            self.reload_windows()  # Widgets neu erstellen

        else:
            print("Invalid color theme selected.")


    def reload_windows(self):

        # Lösche alle vorhandenen Widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Erstelle die Widgets neu
        self.__init__(self.root)  # Reinitialisiere die Klasse
        self.open_settings_window()


def main():
    root = customtkinter.CTk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()