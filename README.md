# Comandos de UV - Commands of UV

Lista corta de comandos importantes de `uv` para el dia a dia - Short list of important `uv` commands for everyday use:

- `uv --version`: muestra la version instalada - shows the installed version.
- `uv help`: ayuda general - general help.
- `uv help <comando>`: ayuda de un comando especifico - help for a specific command.
- `uv init`: crea un nuevo proyecto en el directorio actual - creates a new project in the current directory.
- `uv venv`: crea un entorno virtual (`.venv`) - creates a virtual environment (`.venv`).
- `uv venv --python 3.12`: crea venv con una version de Python - creates venv with a Python version.
- `uv pip install <paquete>`: instala paquetes con `pip` via `uv` - installs packages with `pip` via `uv`.
- `uv pip install -r requeriments.txt`: instala dependencias desde archivo - installs dependencies from file.
- `uv pip list`: lista paquetes instalados - lists installed packages.
- `uv pip freeze`: muestra dependencias fijadas para exportar - shows pinned dependencies for export.
- `uv add <paquete>`: agrega una dependencia al proyecto (pyproject) - adds a dependency to the project (pyproject).
- `uv remove <paquete>`: elimina una dependencia del proyecto - removes a dependency from the project.
- `uv sync`: instala dependencias del proyecto y sincroniza el entorno - installs project dependencies and syncs the environment.
- `uv lock`: genera/actualiza el archivo de bloqueo - generates/updates the lock file.
- `uv run <comando>`: ejecuta un comando usando el entorno del proyecto - runs a command using the project environment.
- `uv run python main.py`: ejemplo de ejecucion - execution example.
- `uv python install 3.12`: instala una version de Python - installs a Python version.
- `uv python list`: lista versiones de Python disponibles - lists available Python versions.
- `uv python pin 3.12`: fija la version de Python del proyecto - pins the project's Python version.
- `uv cache dir`: muestra la ubicacion de la cache - shows cache location.
- `uv cache clean`: limpia la cache - cleans the cache.
