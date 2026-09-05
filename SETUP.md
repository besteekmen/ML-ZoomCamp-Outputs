# Setup

## 1. Install `uv`

If `uv` is not already installed in the Codespace terminal:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart the terminal, then verify:

```bash
uv --version
```

---

## 2. Initialize the Project

Initialize the Python project:

```bash
uv init
```

This creates the `pyproject.toml` file.

---

## 3. Install Required Libraries

Install the libraries needed for the course:

```bash
uv add numpy pandas scikit-learn seaborn jupyter
```

`uv` automatically creates the `.venv` environment and installs the dependencies.

---

## 4. Verify the Installation

Test the installed libraries:

```bash
uv run python -c "import numpy, pandas, sklearn, seaborn; print('All libraries installed successfully')"
```

Verify Jupyter:

```bash
uv run jupyter --version
```

---

## Project Files

After setup, the important files are:

```text
├── .venv/          # Virtual environment (ignored by Git)
├── pyproject.toml  # Project configuration and dependencies
├── uv.lock         # Locked dependency versions
└── README.md
```

Commit `pyproject.toml` and `uv.lock` to Git.
While working on github codespace, after reopening, only run `uv run python` to use the created venv.
