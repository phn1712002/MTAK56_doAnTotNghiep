import json, os 

def load_json(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)