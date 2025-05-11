import os
import json
import shutil
from datetime import datetime

#config faila nolasīšana
def load_config(file_name="config.json"):
    with open (file_name, "r", encoding="uts-8") as f:
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
