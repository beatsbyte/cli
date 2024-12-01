import subprocess
import os

def build():
    print("Building executable...")
    
    icon_path = os.path.join("icon", "icon.ico")
    src_path = os.path.join("src", "main.py")

    command = [
        "pyinstaller",
        "--onefile",
        "--name=bb", 
        f"--icon={icon_path}",  
        f"{src_path}", 
    ]
    
    subprocess.run(command, check=True)

if __name__ == "__main__":
    build()