import os
import json
import shutil
from datetime import datetime

def load_config(file_name="config.json"):
    with open (file_name, "r", encoding="utf-8") as f:
        return json.load(f)
    
def ensure_target_folders(base_path, extension_map):
    target_folders = set(extension_map.values())
    for folder in target_folders:
        full_path = os.path.join(base_path, folder)
        os.makedirs(full_path, exist_ok=True)
        
def move_files(config):
    source = config["source_folder"]
    ext_map = config["extension_map"]

    with open("log.txt", "a", encoding="utf-8") as log:
        for file_name in os.listdir(source):
            full_path = os.path.join(source, file_name)


            if os.path.isfile(full_path):
                _, ext = os.path.splitext(file_name)

                if ext in ext_map:
                    dest_folder = ext_map[ext]
                    dest_path = os.path.join(source, dest_folder, file_name)

                    try:
                        shutil.move(full_path, dest_path)
                        log.write(f"[{datetime.now()}] Pārvietots: {file_name} → {dest_folder}\n")
                    except Exception as e:
                        log.write(f"[{datetime.now()}] Kļūda ar {file_name}: {e}\n")

if __name__ == "__main__":
    config = load_config()
    ensure_target_folders(config["source_folder"], config["extension_map"])
    move_files(config)