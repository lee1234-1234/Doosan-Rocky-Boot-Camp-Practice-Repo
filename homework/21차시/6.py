import os

folder_path = "sample_folder"

if os.path.exists(folder_path):
    file_list = os.listdir(folder_path)

    for item in file_list:
        print(item)
else:
    print("폴더가 존재하지 않습니다.")