import os

# Đường dẫn tới thư mục Scripts của môi trường conda clone
SCRIPTS_PATH = r".\.conda\Scripts"

# Đường dẫn Python thực tế trong env mới
PYTHON_PATH = r".\.conda\python.exe"

def create_bat_wrapper(exe_file):
    base = os.path.splitext(exe_file)[0]
    bat_file = base + ".bat"
    command = f'"{PYTHON_PATH}" "{exe_file}" %*\n'
    
    with open(bat_file, "w") as f:
        f.write(command)
    print(f"Tạo: {bat_file}")

def main():
    for file in os.listdir(SCRIPTS_PATH):
        if file.endswith(".exe"):
            exe_path = os.path.join(SCRIPTS_PATH, file)
            create_bat_wrapper(exe_path)

if __name__ == "__main__":
    main()