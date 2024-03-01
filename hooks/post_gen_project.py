import sys
import subprocess


def main():
    print("Generating Python virtual enviroment")
    subprocess.run(["python", "-m", "venv", ".venv"])
    subprocess.run([".venv/bin/pip", "install", "-r", "requirements.txt"])
    print("Initializing git repository")
    subprocess.run(["git", "init"])
    subprocess.run(["git", "branch", "-m", "main"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Initial commit"])
    print("Done!")


if __name__ == '__main__':
    sys.exit(main())
