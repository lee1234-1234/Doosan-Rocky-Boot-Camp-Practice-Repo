from pathlib import Path

folder_path = Path("Doosan")

if folder_path.exists():
    for file in folder_path.iterdir():
        if file.is_file() and file.suffix == ".txt":
            print(file.name)
else:
    print("폴더가 존재하지 않습니다.")