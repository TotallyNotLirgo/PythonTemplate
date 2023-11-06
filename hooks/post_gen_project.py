import sys, subprocess

def main():
    print("Generating Python virtual enviroment")
    subprocess.run(["python", "-m", "venv", ".venv"])
    subprocess.run([".venv/bin/pip", "install", "-r", "requirements.txt"])
    

if __name__ == '__main__':
    sys.exit(main())