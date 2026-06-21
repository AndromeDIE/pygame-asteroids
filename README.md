# PyGame Asteroids

This repo is part of the backend developer course from boot.dev

You control a triangle, dodging incredibly hazardous circle-shaped circles.
Game states are automatically logged in a file called `game_state.jsonl`.

Due to pygame not running smoothly on Python 3.14, the project is made in 3.13 and managed via venv and astral-uv.

To run the project open your UNIX-Shell of choice (WSL works too) and install astral-uv via
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then create a virtual environment within the project root via
```
uv venv
```

and activate the virtual environment via
```
source .venv/bin/activate
```

Finally, while you're at the project root, start the game with
```
uv run main.py
```
