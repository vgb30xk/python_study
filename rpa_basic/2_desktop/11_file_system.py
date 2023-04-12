# 파일 기본
import os
# print(os.getcwd())
# os.chdir("rpa_basic")
# print(os.getcwd())
# os.chdir("..")
# print(os.getcwd())
# os.chdir("../..")
# print(os.getcwd())
# os.chdir("c:/")
# print(os.getcwd())

# 파일 경로 만들기
# file_path = os.path.join(os.getcwd(), "my_file.txt")
# print(file_path)


# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"C:\Users\Administrator\Desktop\parkcoding\my_file.txt"))

# 파일 정보 가져오기
# import time
# import datetime

# # 파일의 생성 날짜
# ctime = os.path.getctime("README.md")
# print(ctime)

# # 날짜 정보를 strftime 을 통해서 연월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime("README.md")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 마지막 접근 날짜
# atime = os.path.getatime("README.md")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# file_path = "README.md"

# # 파일 크기 (바이트 단위)
# size = os.path.getsize(file_path)
# print(size)

# 파일 목록 가져오기
# print(os.listdir())
# print(os.listdir("rpa_basic"))

# 파일 목록 가져오기(하위 폴더 모두 포함)
# result = os.walk(".")
# # print(result)

# for root, dirs, files in result:
#     print(root, dirs, files)
#     print()

# 만약 어떤 폴더내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# result = []

# for root, dirs, files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root, name))


# print(result)

# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면
# import fnmatch
# pattern = "*.py"
# result = []
# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):
#             result.append(os.path.join(root, name))

# print(result)

# 주어진 경로가 파일인지, 폴더인지
# print(os.path.isdir("rpa_basic"))
# print(os.path.isfile("rpa_basic"))

# print(os.path.isdir("README.me"))
# print(os.path.isfile("chromedriver.exe"))

# # 만약에 지정된 경로에 해당되는 파일/ 폴더가 없다면
# print(os.path.isfile("chromeㅇㅇㅇdriver.exe"))

# 주어진 경로가 존재하는지?
# if os.path.exists("README.md"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("파일 또는 폴더가 존재하지 않습니다.")

# 파일 만들기
# open("new_file.txt", "a").close()

# 파일명 변경하기
# os.rename("new_file.txt", "adad_file.txt")

# 파일삭제하기
# os.remove("나바바_file.txt")

# 폴더 만들기
# os.mkdir("new_folder")
# os.mkdir("c:/Users/Administrator/Desktop/parkcoding")

# os.makedirs("new_folder/a/b/c")

# 폴더명 변경하기
# os.rename("new_folder", "adad_fil")

# 폴더 지우기
# os.rmdir("adad_fil")

# 폴더 안의 모든 폴더 및 파일 지우기
import shutil
# shutil.rmtree("adad_fil")

# 파일 복사하기
# # 어떤 파일을 폴더 안으로 복사하기
# shutil.copy("README.md", "test_folder")

# # 어떤 파일을 폴더 안에 새로운 파일 이름으로 복사하기
# shutil.copy("README.md", "test_folder/copid_README.md")

# shutil.copyfile("README.md", "test_folder")
# shutil.copy2("README.md", "test_folder/copy2.md")

# copy, copufile: 메타정보 복사 X
# copy2         : 메타정보 복사 O

# 폴더 복사
# shutil.copytree("test_folder", "test_folder2")

# 폴더 이동
# shutil.move("test_folder", "test_folder2")
# shutil.move("test_folder2", "test_folder1")
