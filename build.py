import subprocess

def build():
    print("Building executable...")
 
    command = [
        "pyinstaller",
        "--onefile",
        "--name=bb", 
        "--icon=icon\\icon.ico",  
        "src\\main.py", 
    ]
    
    subprocess.run(command, check=True)

if __name__ == "__main__":
    build()