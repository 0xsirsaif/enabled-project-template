from main import app
from pathlib import Path
import importlib


def load_app():
    for path in Path("../../../apps").iterdir():
        if path.is_dir():
            try:
                plugin = importlib.import_module(f"apps.{path.name}.main")
                app.include_router(plugin.router, prefix=f"/{path.name}")
                print(f"Loaded app: {path.name} \u2713")
            except ModuleNotFoundError:
                pass