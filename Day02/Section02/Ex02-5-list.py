'''
단일 변수에 여러 항목을 저장하는데 사용된다.
List항목은 순서가 지정되고 변경 가능하며 중복값 허용
List에는 다양한 데이터 유형이 포함될 수 있다.
'''

thislist = ["피카츄","라이츄","꼬부기"]
print(thislist)
print(thislist[0])
#List길이
print(len(thislist))

#List 데이터유형
list1 = ["피카츄","라이츄","꼬부기"]
list2 = [1,2,3,4,5]
list3 = [True,False,False]
#다양한 유형 포함가능
list4 =["abc",34,"Flase",40]

#항목접근
thislist= ["피카츄","라이츄","꼬부기"]
print(thislist[1])

#변경
thislist[1] ="잠만보"
print(thislist)

#항목변경 2개
thislist = ["피카츄","라이츄","꼬부기","파이리","버터플","야도란"]
thislist [1:3] = ["울먹이", "메타몽"]
print(thislist)

#항목추가
thislist = ["피카츄","라이츄","꼬부기"]
thislist.append("파이리")
print(thislist)

#항목추가 - 인덱스 번호로 추가
thislist = ["피카츄","라이츄","꼬부기"]
thislist.insert(1, "잠만보")
print(thislist)

#항목 값으로 제거
thislist = ["피카츄","라이츄","파이리"]
thislist.remove("라이츄")
print(thislist)

#항목을 지정된 인덱스로 제거
thislist = ["피카츄","라이츄","파이리"]
thislist.pop(2)
print(thislist)


# 마지막 값 제거
thislist = ["피카츄","라이츄","파이리","잠만보"]
thislist.pop()
print(thislist)

# 목록 삭제
thislist = ["피카츄","라이츄","파이리"]
thislist.clear()
print(thislist)

#확장
thislist = ["피카츄","라이츄","파이리"]
thislist.extend(["버터플","야도란"])
print(thislist)

# 객체 삭제
# del thislist  #값만 삭제하는 게 아니라 메모리 자체를 삭제시킴
# print(thislist)