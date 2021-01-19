#p. 156 매개변수 지정하여 호출하기
# 인수 : 함수를 호출할 때 함수에 (매개변수로) 넘기는 데이터 def add(a,b)
# 매개변수 : 함수를 호출할 때 함수에 전달되는 데이터 값 / 함수 정의문
# 기본매개변수 : 매개변수의 기본값을 지정하는 것
# 가변매개변수(*) : 매개변수의 마지막 위치(다른 매개변수가, 가변매개변수 뒤에 올수 없다.)
# 키워드 매개변수(**) : 매개변수의 기본값을 지정하고, 딕셔너리 타입으로 반환
# 매개변수 기본값 지정 <--> 기본 매개변수
# def add(a, b=10):
#     return a + b
# a = 3
# result = add(a)
# print('두 수의 합: ', result)
# args --> 리스트나 튜플처럼, 여러값이 일렬로 받는~
# def add_many(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
# final = add_many(10,20,30,40,50)
# print(final)
#
# # ex > 사각형의 넓이를 구하는 공식(수학) <--> 함수
# def get_rectangle(x, y):
#     return x*y
#
# rect = get_rectangle(10,50)
# print('사각형의 넓이 : ',rect)
#
# # 원의 넓이 구하는 함수
# import math # math 모듈을 불러오기 - 내장함수, 표준함수
# print(math.pi)
# def get_circle(pi, r):
#     return pi*(r**2)
# result = get_circle(math.pi,5)
# print('원의 면적 : ',result)

import random
#list comprehension /리스트 내포
# list_a = [x for x in range(1, 11)]
# print(list_a)
# def get_squared(num):
#     return num ** 2
# list_a_result = map(get_squared, list_a)
# print(list_a_result)
# for item in list_a_result:
#     print(item)
# #패킹, 언패킹
# def func1(x, y):
#     return x+y, x-y
#
# value1,value2 = func1(10, 20)
# print(value1, value2)
# #패킹(packing)
# def say_hello(n=3, *args):
#     for i in n:
#         for msg in args:
#             print(msg)
# say_hello('안녕','반가워')

# filter() 함수
# list_b = [1,2,3,4,5]
# def odd(num):
#     if num %2 ==1:
#         return True
# list_b_result = filter(odd, list_b)
# print(tuple(list_b_result))
#
# tuple_a = (x for x in range(10))
# print(tuple(tuple_a))
#
# list_c = [x for x in range(10) if x % 2 ==0]
# print(list(list_c))
# return - (1) 반환값 / 돌려주는 값 (2) 중단 - 함수의 사용중단
def say_nick(nick):
    if nick == '바보':
        return
    print('나의 별명은 %s 입니다.' % nick)