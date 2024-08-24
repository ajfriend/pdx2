from pathlib import Path

def _get_if_file(s: str) -> str:
    path = Path(s)

    if path.is_file():
        with open(s) as f:
            s = f.read()

    return s
