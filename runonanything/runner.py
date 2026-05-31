import platform
import subprocess
import sys
import os

from pathlib import Path


class Runner:

    def __init__(self, script_path, python_version=None, requirements=None):
        self.os_name = self._check_user_os()
        
        self.script_path = Path(script_path).resolve()
        self.project_directory = self.script_path.parent
        self.requirements = self.project_directory / "requirements.txt"
        self.venv_directory = self.project_directory / ".venv"
        self.venv_executable = ""

        self.python_version = python_version or f"{sys.version_info.major}.{sys.version_info.minor}"
        self.user_python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        
    def _check_user_os(self):
        try: 
            current_os = platform.system().lower()
            if current_os == "windows":
                return "Windows"
            elif current_os == "linux":
                return "Linux"
            elif current_os == "darwin":
                return "Mac"
            else:
                raise ValueError("Unknown OS")

        except ValueError:
            print("Unknown OS, library only works on Windows | MacOS | Linux")


    def _python_version_matches_system(self):
        sys_major, sys_minor, sys_micro = sys.version_info[:3]

        parts = self.python_version.split('.')
        target_major = int(parts[0])
        target_minor = int(parts[1]) if len(parts) > 1 else 0
        target_micro = int(parts[2]) if len(parts) > 2 else 0

        return (sys_major == target_major and
                sys_minor == target_minor and
                sys_micro == target_micro)

    def _create_venv(self, python_executable):
        if not self.venv_directory.exists():    
            try:
                subprocess.run([python_executable, "-m", "venv", str(self.venv_directory)], capture_output=True, check=True)
                print("Venv created successfully")
            except subprocess.CalledProcessError as e:
                print(f"Failed to create virtual environment: {e.stderr}")
                sys.exit(1)
        else:
            print(f"Virtual environment already exists at {self.venv_directory}")
        
        self.venv_executable = self.venv_executable = self.venv_directory / "Scripts" / "python.exe" if self.os_name == "Windows" else self.venv_directory / "bin" / "python"


    def _get_pyenv_root(self):
        return Path.home() / ".pyenv"

    def _is_pyenv_installed(self):
        return (self._get_pyenv_root() / "bin" / "pyenv").exists() 

    def _install_pyenv(self):
        print("Installing pyenv...")
        if self.os_name == "Windows":
            # pyenv-win installation via PowerShell
            cmd = (
                'powershell -Command "& {'
                'Invoke-WebRequest -UseBasicParsing -Uri '
                '"https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" '
                '-OutFile install-pyenv-win.ps1; '
                '.\\install-pyenv-win.ps1; '
                'Remove-Item install-pyenv-win.ps1}"'
            )
            subprocess.run(cmd, shell=True, check=True)
        else: 
            subprocess.run("curl -fsSL https://pyenv.run | bash", shell=True, check=True)

    def _install_desired_python_version(self):
        try:
            install_result = subprocess.run(["pyenv", "install", "-s", self.python_version], capture_output=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to install Python {self.python_version}: {e.stderr.decode()}")
            sys.exit(1)

    def _add_pyenv_to_path(self):
        pyenv_root = self._get_pyenv_root()
        os.environ["PYENV_ROOT"] = str(pyenv_root)
        new_path = f"{pyenv_root}/bin:{pyenv_root}/shims:{os.environ.get('PATH', '')}"
        os.environ["PATH"] = new_path

    def _get_venv_python_path(self):
        result = subprocess.run(["pyenv", "prefix", self.python_version], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Could not locate Python {self.python_version}: {result.stderr}")
            sys.exit(1)
    
        python_path = Path(result.stdout.strip()) / "bin" / "python"
        return python_path

    def _install_requirements(self):
        print("Installing requirements...")
        subprocess.run([self.venv_executable, "-m", "pip", "install", "-r", str(self.requirements)], check=True)

    def _ask_continue_no_requirements(self):
        print(f"No requirements.txt found in {self.project_directory}")
        answer = input("Continue without installing dependencies? (y/N): ").strip().lower()
        return answer in ('y', 'yes')

    def _handle_requirements(self):
        if self.requirements.exists():
            self._install_requirements()
        else:
            if not self._ask_continue_no_requirements():
                print("Aborted by user.")
                sys.exit(1)
            
            
    def run(self):
        if self._python_version_matches_system():
            venv_path = self._create_venv(sys.executable)
        else:
            if not self._is_pyenv_installed():
                self._install_pyenv()
        
            self._add_pyenv_to_path()
                
            self._install_desired_python_version()   
                    
            self._create_venv(self._get_venv_python_path())
        
        self._handle_requirements()
        args = [str(self.venv_executable), str(self.script_path)] 
        result = subprocess.run(args)
        return result.returncode
        
