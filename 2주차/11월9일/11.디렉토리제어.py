import os
print(os.getcwd())
"""
os.chdir(path) :작업디렉토리를 path로 변경
../ : 상위 디렉토리, ../../ : 2계 상위디렉트로

os.mkdir(path) :디렉토리 생성
os.rmdir(path) :디렉토리 삭제
os.listdir(path) :디렉토리 파일 목록 리스트로 반환
os.path.isfile(paht) :파일이 존재하면 true, 아니면 false
os.path.isdir(path) :path의 디렉토리가 존재하면 true, 아니면 false"""