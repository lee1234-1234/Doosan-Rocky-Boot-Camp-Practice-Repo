# pathlib_module.py
# Path 클래스를 사용하여 경로를 객체로 다루기
from pathlib import Path

# 현재 작업 디렉토리 확인
print(Path.cwd())

print("------------------")
# 2 경로 생성 및 조작
folder = "./ch21/classify_file"
path = Path(folder)
print(path)

# '/' 연산자는 경로 결합 연산자로,
# pathlib.Path 객체에서 지원
print(path / "file.txt")     # 폴더와 파일 경로 결합

print("------------------")
# 3 디렉토리 및 파일 존재 여부 확인
file = "./ch21/classify_file/file.txt"
path = Path(file)

print(path.exists())
print(path.is_file())
print(path.is_dir())

print("------------------")
new_folder = "./ch21/classify_file/new_folder"
path = Path(new_folder)
path.mkdir(exist_ok=True)
path.rmdir()

print("------------------")
file = "./ch21/classify_file/new_folder"
file_path = Path(file)
file_path.touch()
file_path.unlink()