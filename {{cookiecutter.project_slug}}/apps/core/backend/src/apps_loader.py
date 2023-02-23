from pathlib import Path
import importlib


def get_sub_apps():
    apps = []
    for app in Path(Path.cwd()).iterdir():
        if app.is_dir() and app.name not in ["core", "__pycache__"]:
            try:
                app = importlib.import_module(f"{app.name}.backend.src.app")
                apps.append(app)
            except ModuleNotFoundError as e:
                print(f"ModuleNotFoundError: {e}")
                pass
    return apps
