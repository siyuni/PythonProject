member_list =[]
with open('회원명단.csv', 'rt', encoding='UTF-8')as file:
    file.readline() # 첫 줄 제거
    while True:
        line = file.readline()
        if not line:
            break
        member = line.split(',') # list로 반환
        member[0] = member[0].strip('"') #양쪽 "" 제거
        member[2] = member[2].strip('\n') #양쪽 들여쓰기 제거

        member_list.append(member)

print(member_list)
