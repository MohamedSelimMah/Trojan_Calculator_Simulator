import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_CACHE_PATH = os.path.join(BASE_DIR, "sim_cache")
HACKED_FOLDER = os.path.join(os.path.expanduser("~"), "Desktop", "You_Got_Hacked")

os.makedirs(SIM_CACHE_PATH, exist_ok=True)
os.makedirs(HACKED_FOLDER, exist_ok=True)