# shutil_module.py

import shutil
import os

path = r'ch21\manage_file'

# 원본 파일 생성
src_file = f'{path}/original.txt'
with open(src_file, 'w') as f:
    f.write("this is a test file.")

# (1) 파일 복사
# copy()로 파일 복사
copy_file = f'{path}/copy.txt'
shutil.copy(src_file, copy_file)

copy2_file = f'{path}/copy2.txt'
shutil.copy2(src_file, copy2_file)


# (2) 디렉토리 
src = f'{path}/test_dir'
dst = f'{path}/copied_test_dir'

# 디렉토리 생성
if not os.path.exists(dst):
    os.mkdir(src)
    
# 디렉토리 전체 복사
if not os.path.exists(dst):
    shutil.copytree(src, dst)
    
    
print('3----------------------')
# (3) 파일 및 디렉토리 이동
src = f'{path}/copy.txt'
dst = f'{path}/copied_test_dir/copiedfile.txt'
if not os.path.exists(dst):
    shutil.move(src, dst)


print('4----------------------')
# (4) 파일 및 디렉토리 삭제
dir1 = f'{path}/test_dir'
dir2 = f'{path}/copied_test_dir'
shutil.rmtree(dir1)
shutil.rmtree(dir2)
