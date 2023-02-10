'''
Casting
변수에 유형을 지정하려는 경우 캐스팅으로 가능
'''

# 정수형
x = int(1)
print(x)
y = int(2.8) # 실수를 정수형으로 print하면 소수점 뒤에가 사라짐
print(y)
z = int("3")
print(type(z))
print(x+z)

# 실수형
x = float(1)
print(x)
z = float("3")
print(z)

#문자형
x = str(1)
y = str(2)
print(x)
print(x+y)

#아스키코드 변환
a = ord('A')
print(a)
b =chr(65)
print(b)
