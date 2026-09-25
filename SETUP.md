# Setup

This project uses [`uv`](https://docs.astral.sh/uv/) for Python version and dependency management.

There are two setup scenarios:

1. **Initial project setup** — only needed when creating the project for the first time.
2. **Setup after cloning the repository** — use this when working on a new machine, WSL installation, Codespace, or other environment.

---

## 1. Initial Project Setup

> Only follow this section when creating the project from scratch.  
> If you cloned this repository, skip to [Setup After Cloning the Repository](#2-setup-after-cloning-the-repository).

### Install `uv`

If `uv` is not already installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart the terminal, or reload your shell configuration if needed:

```bash
source ~/.bashrc
```

Verify the installation:

```bash
uv --version
```

---

### Initialize the Project

From the project directory:

```bash
uv init
```

This creates the initial project files, including `pyproject.toml`.

---

### Install Required Libraries

Install the libraries needed for the first modules of ML Zoomcamp:

```bash
uv add numpy pandas scikit-learn seaborn jupyter
```

Add other libraries later as they become necessary during the course.

For example:

```bash
uv add matplotlib
```

Using `uv add` updates both the project dependencies and the lock file.

`uv` creates and manages the local `.venv` virtual environment automatically.

---

### Verify the Installation

Test the main libraries:

```bash
uv run python -c "import numpy, pandas, sklearn, seaborn; print('All libraries installed successfully')"
```

Verify Jupyter:

```bash
uv run jupyter --version
```

Check the Python version:

```bash
uv run python --version
```

---

## 2. Setup After Cloning the Repository

Use this section when setting up the project on a new machine, WSL installation, Codespace, or other development environment.

### Install Basic System Tools

On Ubuntu / WSL:

```bash
sudo apt update
sudo apt install -y git curl build-essential
```

---

### Clone the Repository

Move to the directory where you keep your projects:

```bash
mkdir -p ~/study-repos
cd ~/study-repos
```

Clone the repository:

```bash
git clone https://github.com/besteekmen/ML-ZoomCamp-Outputs.git
```

Git automatically creates the `ML-ZoomCamp-Outputs` directory.

Enter the repository:

```bash
cd ML-ZoomCamp-Outputs
```

---

### Install `uv`

If `uv` is not already installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart the terminal, or reload the shell:

```bash
source ~/.bashrc
```

Verify:

```bash
uv --version
```

---

### Install the Required Python Version

The repository contains a `.python-version` file specifying the Python version used by the project.

Install Python through `uv`:

```bash
uv python install
```

You can verify the selected version with:

```bash
uv run python --version
```

---

### Recreate the Project Environment

Do **not** run `uv init` or reinstall the dependencies manually after cloning.

The repository already contains:

- `pyproject.toml`
- `uv.lock`
- `.python-version`

Recreate the environment with:

```bash
uv sync
```

This creates the local `.venv` directory and installs the dependency versions defined by the project.

---

### Verify the Environment

Test the main libraries:

```bash
uv run python -c "import numpy, pandas, sklearn, seaborn; print('All libraries installed successfully')"
```

Verify Jupyter:

```bash
uv run jupyter --version
```

Check Python:

```bash
uv run python --version
```

If needed, check an individual package:

```bash
uv run python -c "import matplotlib; print(matplotlib.__version__)"
```

---

## 3. Working With the Environment

### Recommended: Run Commands Through `uv`

You do not need to activate the virtual environment manually.

For example:

```bash
uv run python
```

```bash
uv run jupyter lab
```

```bash
uv run jupyter notebook
```

```bash
uv run python script.py
```

---

### Optional: Activate the Virtual Environment

If you prefer to activate the environment manually:

```bash
source .venv/bin/activate
```

Verify that the project environment is active:

```bash
which python
```

The path should point to:

```text
.../ML-ZoomCamp-Outputs/.venv/bin/python
```

To leave the environment:

```bash
deactivate
```

Avoid hard-coded environment paths such as:

```text
/workspaces/ML-ZoomCamp-Outputs/.venv/bin/activate
```

because the repository may be located somewhere different on another machine.

---

## 4. Adding New Dependencies

As new libraries are needed during ML Zoomcamp, add them with:

```bash
uv add <package-name>
```

For example:

```bash
uv add xgboost
```

This:

- installs the package,
- updates `pyproject.toml`,
- updates `uv.lock`.

Prefer `uv add` over manually using `pip install` so that the project environment remains reproducible.

After pulling changes that modify `pyproject.toml` or `uv.lock`, run:

```bash
uv sync
```

---

## 5. Normal Workflow

Once the project is already set up, the usual workflow is:

```bash
cd ~/study-repos/ML-ZoomCamp-Outputs
git pull
```

Then continue working normally.

There is no need to run `uv sync` every time unless the dependencies or lock file have changed.

Useful commands:

```bash
uv run python
```

```bash
uv run jupyter lab
```

or, if the virtual environment is activated:

```bash
python
```

```bash
jupyter lab
```

---

## Project Files

Important environment-related files:

```text
ML-ZoomCamp-Outputs/
├── .venv/             # Local virtual environment (ignored by Git)
├── .python-version    # Python version used by the project
├── pyproject.toml     # Project configuration and dependencies
├── uv.lock            # Locked dependency versions
├── README.md
└── SETUP.md
```

Commit these files:

```text
.python-version
pyproject.toml
uv.lock
```

Do **not** commit:

```text
.venv/
```

The virtual environment should be recreated locally using:

```bash
uv sync
```
