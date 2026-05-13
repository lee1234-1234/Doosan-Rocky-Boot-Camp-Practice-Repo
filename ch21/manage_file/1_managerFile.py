import os

def find_txt_files(folder_path):
    txt_files = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            txt_files.append(file_path)

    return txt_files


folder_path = r"ch21\manage_file"

result = find_txt_files(folder_path)
print(result)