import json
import base64
import zlib
import csv

def decompress_notes(notes_blob):
    try:
        notes_blob_decoded = base64.b64decode(notes_blob)
        decompressed_notes = zlib.decompress(notes_blob_decoded).decode()
        return json.loads(decompressed_notes)
    except Exception as e:
        print("Failed to decompress notes:", e)
        return None

def read_toolbox_notes(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print("Failed to read Toolbox notes from file:", e)
        return None

# Function to save notes to CSV
def save_notes_to_csv(file_path, notes):
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            # writer.writerow(['Username', 'Note Text'])
            for username, usernotes in notes.items():
                for note in usernotes['ns']:
                    writer.writerow([username, note['n']])
        print("Notes saved to", file_path)
    except Exception as e:
        print("Failed to save notes to CSV:", e)

# File paths
file_path = "notes.txt"
csv_file_path = "notes.csv"

# Read Toolbox notes from file
toolbox_notes = read_toolbox_notes(file_path)

# Decompress notes if present
if toolbox_notes:
    notes_blob = toolbox_notes.get('blob')
    if notes_blob:
        decompressed_notes = decompress_notes(notes_blob)
        if decompressed_notes:
            print("Decompressed notes:")
            for user, notes in decompressed_notes.items():
                print(f"User: {user}, Notes: {notes}")
            # Save notes to CSV
            save_notes_to_csv(csv_file_path, decompressed_notes)
        else:
            print("No decompressed notes found.")
    else:
        print("No notes blob found.")
else:
    print("No Toolbox notes found in the file.")
