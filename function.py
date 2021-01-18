# 함수 (p.150)
# 지금까지  - 표현식 <--> 앞으로 - 함수화
# 같은 내용을 반복 <--> 재사용
# 상수 : 변하지 않는 값 vs 함수 : 코드를 저장 vs 변수: 데이터를 저장하는 공간
# 함수정의
'''
1. 매개변수가 없는 함수
def 함수의 이름1():
    실행할 코드1
    실행할 코드2
    실행할 코드...

2. 매개변수가 있는 함수
매개변수(parameter, 파라미터) - 함수 내부에 데이터를 전달하는 변수
인수(argument) - 함수호출시 사용
def 함수의 이름2(매개변수):
    실행할 코드1
    실행할 코드2
    실행할 코드...

3. 결과값이 없는 함수
def 함수의 이름3(매개변수):
    print(실행할 코드)
함수의 이름1() <-- 함수를 호출, 실행
함수이름2(매개변수) <-- 함수의 호출, 매개변수로 함수 내부에 데이터를 전달
'''


# add - 숫자를 더하고 그 결과값을 알려주는 함수
# 함수 내부로 값을 전달 - 매개변수
# 함수 내부 --> 외부로 값을 전달 <-- return
# 반환값이 없는 단순 함수
# ↓ 함수의 정의 - 함수의 이름은 say_hello
# def say_hello_10_times():
#     for i in range(10):
#         print(f'안녕하세요 {i+1}번째 고객님!')
# #함수의 실행
# say_hello_10_times()


# 매개변수, 인수의 차이
def add(a, b):
    result = a + b
    return result


def sub(a, b):
    if a > b:
        result = a - b
    else:
        result = abs(a - b)
    return result


def mul(a, b):
    result = a * b
    return result


def div(a, b):
    result = a // b
    return result


def jegop(a):
    result = a**2
    return result

# 매개변수 갯수 --> typeError 발생(매개변수 갯수가 다를때)
result_jegop = jegop(5)
print('5의 제곱 : ', result_jegop)
result_add = add(10, 5)
result_sub = sub(7, 3)
result_mul = mul(3, 10)
result_div = div(20, 4)
print('10과 5의 합:' + str(result_add))
print('7과 3의 차:' + str(result_sub))
print('3과 10의 곱:' + str(result_mul))
print('20 나누기 4의 몫:' + str(result_div))

print('-'*100)


def new_add(a,b):
    print('%d, %d의 합은 %d입니다.' % (a, b, a+b))

result_new_add = new_add(9,8)
if result_new_add is None:
    print('result_new_add함수는 , 반환값이 없습니다.')