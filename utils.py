"""Utility functions."""
import os, json, hashlib, logging, time
from pathlib import Path
from typing import Any, Dict

logger = logging.getLogger(__name__)

def setup_logging(level: str = "INFO"):
    logging.basicConfig(level=getattr(logging, level.upper()), format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

def load_config(path: str) -> Dict[str, Any]:
    with open(path) as f:
        if path.endswith((".yaml", ".yml")):
            import yaml; return yaml.safe_load(f)
        return json.load(f)

def retry(fn, max_attempts: int = 3, delay: float = 1.0):
    last = None
    for i in range(max_attempts):
        try: return fn()
        except Exception as e:
            last = e
            if i < max_attempts - 1: time.sleep(delay * (2 ** i))
    raise last

def chunk_list(lst, size):
    for i in range(0, len(lst), size): yield lst[i:i+size]

def ensure_dir(path: str): Path(path).mkdir(parents=True, exist_ok=True)

def hash_text(text: str) -> str: return hashlib.sha256(text.encode()).hexdigest()[:16]
