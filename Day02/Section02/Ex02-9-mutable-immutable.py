'''
mutable - 메모리 값을 변경 가능 객체
리스트, 세트, 딕셔너리
'''

me = [1,2,3]
print(id(me)) #
me.append(4)
print(id(me))

'''
immutable - 메모리 값 변경 불가
정수, 실수, 문자열, 튜플
'''

me = 10
print(id(me))
me +=1
print(id(me))