#p.157 입력값이 몇개가 될지 모를때
# 입력값이 여러개일때

def add_num(a,b):
    return a+b
result = add_num(5, 9)
print('두수의 합 : ',result)

# 가변 매개변수
# args, values, items...변경이 가능하다
def add_many_num(*args):
    result = 0
    for i in args:
        result += i
    return result

multi_result = add_many_num(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('최종값 : ', multi_result)



# 158. 여러 매개변수를 곲셈한 결과
def add_calc(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for j in args:
            result *= j

    return result

final = add_calc('add', 1,2,3,4,5,6,7,8,9,10)
print(f'add 결과 {final}')

final = add_calc('mul', 8,9,10)
print(f'mul 결과 {final}')