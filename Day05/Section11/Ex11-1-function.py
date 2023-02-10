'''
함수(function)
하나의 특별한 목적의 작업을 수행하기 위해
독립적으로 설계된 프로그램 코드의 집합.

def 함수이름 (매개변수)
    코드 실행문
    return 반환값
'''

#welcome() 함수 정의(실행 X)

def welcome(): #매개변수가 없고, return도 없다
    print('Hello Python')
    print('Nice to meet you')

welcome() # 함수 호출 실행

#매개변수가 있고, 리턴 X
def introduce(name, age):
    print('내 이름은 {}이고, 나이는 {}입니다'.format(name, age))
introduce('김시윤', 23)

#가변 매개변수 함수
def show(*args):
    for item in args:
        print(item)

show('python','java','C++')

#반환(return) 값이 있는 함수
def address(): #매개변수 x, return O
    str ='우편번호 12345\n'
    str += '서울시 영등포구 여의도동'
    return str

result = '''우편번호 12345
서울시 영등포구 여의도동'''
print(result)

result =address()
print(result)

#매개변수 O 리턴 O
def plus (num1, num2):
    return num1 + num2

result =plus(5, 7)
print(result)
print(plus(2, 3))

area = 0
def rMove():
    global area
    area += 1

def lMove():
    global area
    area -= 1

rMove()
rMove()
rMove()
rMove()
lMove()
lMove()
print('유닛이 오른쪽으로 {}칸 이동했습니다'.format(result))
