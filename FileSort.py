import os
import json
import shutil

#config faila nolasīšana
def load_config(file_name="config.json"):
    with open (file_name, "r", encoding="uts-8") as f:
        return json.load(f)
def ensure_target_folders(base_path, extension_map):