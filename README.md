# Run On Anything

> A Python library that lets you run your Python project on any machine with Python installed.

---

## About

### What it does
Runs your Python files inside a virtual environment created with a specified Python version (3.0 to 3.14). Automatically installs dependencies from `requirements.txt`, `uv.lock`, or `pyproject.toml` if present.

### Why I built it
To avoid the "works on my machine" problem and allow anyone to run Python projects with minimal setup.

### Who it's for
Python developers who want to share their code and ensure it runs consistently across different machines.

---

## Built With

| Category | Tool |
| -------- | ---- |
| **Language** | Python |
| **Framework** | None (Library) |
| **Libraries** | setuptools |

---

## Getting Started

### Prerequisites

- Python 3.0+

### Installation

**Option 1: Install from Codeberg**
```bash
pip install git+https://codeberg.org/Ryan-Goosen/runOnAnything
```

**Option 2: Clone and install locally**
```bash
git clone https://codeberg.org/Ryan-Goosen/runOnAnything.git
cd runOnAnything
pip install .
```

---

## Usage

```python
from env_setup import run

# Run your main.py with Python 3.13
run("main.py", 3.13)
```

---

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

---

## Acknowledgments

- [othneildrew Best-README-Template](https://github.com/othneildrew/Best-README-Template)
