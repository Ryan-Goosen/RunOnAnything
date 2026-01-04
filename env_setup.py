import os
import subprocess

from platform import system
from sys import version_info, executable


def check_if_pip_is_installed():
    return_code = subprocess.call(["pip", "--version"])
    return return_code == 0

def install_pip():
    subprocess.call([executable, "-m", "ensurepip"])
    print("\nPIP has been installed.")

def check_uv_is_installed():
    output = subprocess.getstatusoutput([executable, '-m', 'pip', 'list'])
    print(output)
    output = output[1].split('\n')
    for item in output[2:]:
        if item.startswith("uv"):
            print("\nUV is already installed.")
            return True
    return False

def install_uv():
    subprocess.call([executable, '-m', 'pip', 'install', 'uv'])
    print("\nUV has been installed.")

def create_venv(version):
    subprocess.call([executable, "-m", "uv", "venv", "--python", str(version), ".venv"])
    print('\nVirtual Environment Created.')


def install_dependencies(virtual_environment):
    req_file = "requirements.txt"
    pp_file = "pyproject.toml"
    lock_file = "uv.lock"
    try:
        if os.path.exists(pp_file):
            print("Found pyproject.toml.")
            if os.path.exists(lock_file):
                print("Found uv.lock. Installing from lockfile...")
                subprocess.call([virtual_environment, "uv", "pip", "sync", lock_file])
            else:
                print("No lockfile found. Installing from pyproject.toml...")
                subprocess.call([virtual_environment,"uv", "pip", "install"])

        elif os.path.exists(req_file):
            print("No pyproject.toml found. Falling back to requirements.txt...")
            subprocess.call([virtual_environment,"uv", "pip", "install", "-r", req_file])
        else:
            print("No dependency files found. Continuing without installing packages.")
    except subprocess.CalledProcessError as e:
        print(f"Dependencies installation failed: {e}")

def activate_venv(file_name):
    global python_executable
    subprocess.call([python_executable, file_name])

def get_venv_python():
    return os.path.join(".venv", "Scripts", "python.exe") if system() == "Windows" else os.path.join(".venv", "bin", "python")

def run(file_name, version):
    global python_executable
    if not check_if_pip_is_installed():
        install_pip()
    if not check_uv_is_installed():
        install_uv()
    if not os.path.exists(".venv"):
        create_venv(version)

    python_executable = get_venv_python()
    install_dependencies(python_executable)
    activate_venv(file_name)


if __name__ == "__main__":
    return 0;
