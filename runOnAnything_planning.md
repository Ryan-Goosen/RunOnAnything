# Run On Anything

---

## Project Identity

| Field | Value |
| ----- | ----- |
| **Name** | Run On Anything |
| **Project ID** | ROA-2025-045 |
| **Owner** | Ryan Goosen |
| **Date Created** | 2025-01-01 |
| **Last Updated** | 2026-05-02 |

---

## Vision & Purpose

**Elevator Pitch:**
A Python library that runs your Python project on any machine with Python installed, avoiding the "works on my machine" problem.

**Long-Term Vision:**
A widely-used library for Python environment management, supporting multiple package managers and Python versions seamlessly.

**Success Metrics:**
- [x] Virtual environment creation
- [x] Dependency auto-installation
- [x] Support for requirements.txt, uv.lock, pyproject.toml
- [ ] Run program directly from run() function
- [ ] Comprehensive testing

---

## Tech Stack

| Category | Tools / Languages |
| -------- | ----------------- |
| **Core Language** | Python |
| **Framework** | None (Library) |
| **Libraries** | setuptools |
| **Tools** | VS Codium |
| **Version Control** | [Codeberg](https://codeberg.org/Ryan-Goosen/runOnAnything) |

---

## Current State

**Phase:** Needs Testing
**Progress:** 80%

**Recent Wins:**
- [x] UV virtual environment creation
- [x] Auto-install from requirements.txt
- [x] Auto-install from uv.lock
- [x] Auto-install from pyproject.toml
- [x] Pip and UV installation detection

**Blockers:**
- [ ] Need comprehensive testing across platforms
- [ ] Run function needs refinement

---

## Roadmap

### Main Objectives

1. **Core Functionality** *(Complete)*
   - [x] Virtual environment setup
   - [x] Dependency detection and installation
   - [x] Python version specification

2. **Testing Phase** *(Current)*
   - [ ] Test on Windows
   - [ ] Test on Linux
   - [ ] Test on macOS
   - [ ] Various project structures

3. **Enhancement** *(Next)*
   - [ ] Run program directly from run() without wrapper
   - [ ] Support for conda environments
   - [ ] Better error handling

### Immediate Next Steps
1. Create test suite
2. Test on clean Windows VM
3. Test on clean Linux VM

---

## Project Structure

```
/runOnAnything
├── env_setup.py         # Main library code
├── setup.py             # Package configuration
├── readme_graphics/     # Logo assets
└── LICENSE
```

---

## Notes & Decisions

**Key Choices:**
- Uses UV for fast dependency management
- Supports multiple dependency file formats
- Simple API: run(file_name, python_version)

**Backlog / Ideas:**
- Add conda support
- Create CLI interface
- Add configuration file support

**Debug Log:**

---

## Visuals

[Attach or link to mockups, screenshots, or diagrams]
