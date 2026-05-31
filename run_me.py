from runonanything import Runner
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: run_me.py <script_path> [python_version]")
        print("Example: run_me.py test.py 3.9")
        sys.exit(1)

    script_path = sys.argv[1]
    python_version = sys.argv[2] if len(sys.argv) > 2 else None

    runner = Runner(script_path, python_version=python_version)
    exit_code = runner.run()
    sys.exit(exit_code)

if __name__ == "__main__":
    main()