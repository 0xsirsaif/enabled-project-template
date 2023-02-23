from pathlib import Path
import importlib
from core.backend.src.main import app as core_app


def load_app():
    apps = []
    for app in Path("apps").iterdir():
        if app.is_dir() and app.name not in ["core"]:
            try:
                app = importlib.import_module(f"apps.{app.name}.backend.src.app")
                apps.append(app)
            except ModuleNotFoundError:
                pass

    for app in apps:
        core_app.include_router(app.app)
