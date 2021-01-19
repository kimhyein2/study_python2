#p. 162 매개변수에 초기값 지정하기(기본 매개변수)
def say_myself(name, old, man=True):
    print('나의 이름은 %s 입니다.' % name)
    print('나의 나이는 %d 입니다.' % old)
    if man:
        print('남성입니다.')
    else:
        print('여성입니다.')

# 함수의 호출
say_myself('박응용', 27,False)

# 주의 p.163
# 매개변수의 기본값(=기본 매개변수)을 지정할 경우, 매개 변수보다 뒤에 위치해야한다.