import sys
import json
import os

def main():
    # Argumente parsen
    args = {}
    keys_to_delete = []
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-dldir" and i + 1 < len(sys.argv):
            args["dldir"] = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "-wd" and i + 1 < len(sys.argv):
            args["wd"] = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "-theme" and i + 1 < len(sys.argv):
            args["theme"] = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "-color" and i + 1 < len(sys.argv):
            args["color"] = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "-del" and i + 1 < len(sys.argv):
            keys_to_delete.append(sys.argv[i + 1])
            i += 2
        else:
            print(f"Unbekanntes Argument: {sys.argv[i]}")
            sys.exit(1)

    # Vorhandene Einstellungen laden
    settings = {}
    if os.path.exists("set.json"):
        with open("set.json", "r") as json_file:
            try:
                settings = json.load(json_file)
            except json.JSONDecodeError:
                print("Fehler beim Laden der vorhandenen Einstellungen. Datei könnte beschädigt sein.")
                sys.exit(1)

    # Neue Argumente anwenden
    settings.update(args)

    # Angegebene Schlüssel löschen
    for key in keys_to_delete:
        if key in settings:
            del settings[key]
            print(f"Schlüssel '{key}' wurde gelöscht.")
        else:
            print(f"Schlüssel '{key}' nicht gefunden und konnte nicht gelöscht werden.")

    # Ausgabe der aktuellen Einstellungen
    print("Aktuelle Einstellungen:")
    for key, value in settings.items():
        print(f"  {key}: {value}")

    # Speichern in set.json
    with open("set.json", "w") as json_file:
        json.dump(settings, json_file, indent=4)
    print("Einstellungen wurden in set.json gespeichert.")

if __name__ == "__main__":
    main()
