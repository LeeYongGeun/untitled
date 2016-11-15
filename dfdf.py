# import random as rn #말 줄이기
# a = rn.randint(1,9)
# print(a)
#
# from random import randint #random패키지중에 randint라는 함수만 불러옴(메모리 적제 줄임으로서 실행속도 향상)
# a = randint(1,9)
# print (a)
#from random import* 앞에 모듈name을 쓰지않ㄱ 함수를 바로 쓸 수 있음

#package디렉토리를 만들때 __init__.py 파일을 만들면 패키지로 인식
def myadd(a, b):
    return a+b
