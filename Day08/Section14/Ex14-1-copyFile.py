'''
파일 복사
    원본 -> 버퍼 변수 (Memory) -> 복사본
'''
buffer_size = 1024 #1024byte -> 1KB
with open('../../Day07/Section13/hello.txt', 'rb') as source: # .. 상위 폴더로 가기
    with open('hello2.txt','wb') as copy:
        while True:
            buffer = source.read(buffer_size)
            if not buffer:
                break
            copy.write(buffer)
print('hello2.txt 파일이 복사되었습니다.')