# p.164 함수 안에서 변수의 효력 범위
# 전역변수, 지역변수

# a = 1
'''
def vartest(a):
    a = a + 1
    print("내부 a", id(a))

vartest(3)
print(a)
# print(a, id(a))
'''

# p.165 Return 사용하기(1)
# a = 1
# def vartest(a):
#     a = a + 1
#     print(a, id(a))
#     return a
# a = vartest(a)
# print(a, id(a))
# p.166 global 사용하기(2)
'''
a = 1
print('처음 a', id(a))

def vartest():
    #전역 변수 a를 사용
    global a
    a = a + 1
    print(a, id(a))

vartest()
print(a, id(a)) 
'''
# swap() 함수
x = 5
y = 3
print(id(x), id(y))
def swap(a, b):
    return b, a
# def swap(a, b):
#     temp = a
#     a = b
#     b = temp


x, y = swap(x,y)
print(x,y)
print(id(x),id(y))